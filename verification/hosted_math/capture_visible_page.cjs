#!/usr/bin/env node
'use strict';
// Supplemental, read-only viewport captures. The canonical full-page comparison
// remains the required check; this script neither alters the DOM nor hides chrome.
const fs = require('node:fs');
const path = require('node:path');
const cp = require('node:child_process');
const crypto = require('node:crypto');
const {VIEWPORTS, waitForHostedMath} = require('./capture_hosted_math.cjs');
const sha256 = bytes => crypto.createHash('sha256').update(bytes).digest('hex');

async function main() {
  const [root, captureDirectory, outputDirectory, extra] = process.argv.slice(2);
  if (!root || !captureDirectory || !outputDirectory || extra)
    throw new Error('Usage: capture_visible_page.cjs CHECKOUT FULL_CAPTURE_DIR EMPTY_OUTPUT_DIR');
  const reportBytes = fs.readFileSync(path.join(captureDirectory, 'hosted-report.json'));
  const report = JSON.parse(reportBytes);
  if (report.status !== 'pass' || report.diagnostic_only ||
      !/^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(report.repository) ||
      !/^[a-f0-9]{40}$/.test(report.revision))
    throw new Error('Require a passing complete pinned report');
  const git = args => cp.execFileSync('git', ['--no-replace-objects', ...args],
    {cwd: root, encoding: 'utf8'}).trim();
  if (git(['rev-parse', report.revision + '^{tree}']) !== report.tree)
    throw new Error('Report tree does not match the local pinned commit');
  const pagePath = 'learning/milestones.md';
  const boundary = report.boundaries.find(item => item.path === pagePath);
  const source = cp.execFileSync('git', ['show', report.revision + ':' + pagePath], {cwd: root});
  const url = `https://github.com/${report.repository}/blob/${report.revision}/${pagePath}`;
  if (!boundary || boundary.url !== url || boundary.source_sha256 !== sha256(source) ||
      !Number.isInteger(boundary.source_expressions))
    throw new Error('Missing or inconsistent milestone source binding');
  const output = path.resolve(outputDirectory);
  if (fs.existsSync(output) && (fs.lstatSync(output).isSymbolicLink() || fs.readdirSync(output).length))
    throw new Error('Use a new empty output directory');
  fs.mkdirSync(output, {recursive: true});
  const {chromium} = require('playwright');
  const browser = await chromium.launch({headless: true});
  const observations = [];
  try {
    for (const viewport of VIEWPORTS) {
      const page = await browser.newPage({viewport});
      try {
        const response = await page.goto(url, {waitUntil: 'domcontentloaded', timeout: 60000});
        if (response?.status() !== 200 || page.url() !== url)
          throw new Error('The exact public pinned page was not returned');
        const article = page.locator('article.markdown-body').first();
        await article.waitFor({state: 'visible', timeout: 30000});
        await page.evaluate(async () => {
          for (let y = 0, steps = 0; y < document.body.scrollHeight && steps < 200; y += 900, steps++) {
            window.scrollTo(0, y);
            await new Promise(resolve => setTimeout(resolve, 50));
          }
        });
        await waitForHostedMath(article, boundary.source_expressions);
        for (const requestedY of [0, 700]) {
          await page.evaluate(y => window.scrollTo({top: y, behavior: 'instant'}), requestedY);
          await page.waitForTimeout(1000);
          await page.evaluate(() => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve))));
          const position = await page.evaluate(() => ({x: window.scrollX, y: window.scrollY}));
          const filename = `milestones-${viewport.width}-y${requestedY}.png`;
          await page.screenshot({path: path.join(output, filename), fullPage: false, timeout: 30000});
          const bytes = fs.readFileSync(path.join(output, filename));
          observations.push({path: pagePath, url, source_sha256: boundary.source_sha256,
            viewport, requested_scroll_y: requestedY, actual_scroll: position,
            observed_at: new Date().toISOString(), screenshot: filename,
            sha256: sha256(bytes), size_bytes: bytes.length});
        }
      } finally {await page.close();}
    }
    fs.writeFileSync(path.join(output, 'viewport-report.json'), JSON.stringify({
      schema_version: 1, kind: 'supplemental_hosted_viewports', repository: report.repository,
      revision: report.revision, tree: report.tree, source_report_sha256: sha256(reportBytes),
      browser: browser.version(), captured_at: new Date().toISOString(), observations,
      limits: 'Unmodified ordinary viewport screenshots for human inspection; not a structural or scientific verdict.'
    }, null, 2) + '\n');
  } finally {await browser.close();}
}
main().catch(error => {console.error(String(error)); process.exitCode = 1;});
