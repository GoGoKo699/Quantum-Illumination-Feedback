# Check the mathematics displayed by GitHub

The scientific arithmetic check is [one directory up](../README.md). This optional browser check compares the mathematical expressions in an exact Git revision with the expressions actually rendered on its public GitHub pages. It covers inline, display and table-cell mathematics at desktop and narrow widths, and saves screenshots for visual inspection.

## Run a representative probe

Use Node.js 18 or later, Python 3.10 or later, Git, Playwright 1.56.1 and MathJax 3.2.1. Install the browser dependencies in a temporary directory outside this repository. Set `NODE_PATH` to that directory's `node_modules`.

```bash
node verification/hosted_math/probe_hosted_math.cjs \
  --root /absolute/path/to/checkout \
  --repository GoGoKo699/Quantum-Illumination-Feedback \
  --revision FULL_40_CHARACTER_COMMIT \
  --page README.md \
  --output /absolute/path/to/new-probe-directory
```

The revision must exist in the local Git object database and on GitHub. The output directory must be new or empty. A probe checks one page and cannot establish complete repository coverage.

## Capture the complete source

```bash
node verification/hosted_math/capture_hosted_math.cjs \
  --root /absolute/path/to/checkout \
  --repository GoGoKo699/Quantum-Illumination-Feedback \
  --revision FULL_40_CHARACTER_COMMIT \
  --output /absolute/path/to/new-capture-directory
```

By default, the collector checks every tracked Markdown page in the pinned revision at widths 1440 and 760. It compiles source expressions as a reference, opens the actual public GitHub pages in a fresh unsigned-in browser, compares accessible mathematical structure and geometry, and writes `hosted-report.json`, source inventories, screenshots and captured HTML. The local compilation alone is not a hosted check. Inspect the screenshots alongside the source for legibility and non-mathematical layout.

The [repository workflow](../../.github/workflows/hosted-math.yml) runs on pull requests from this same repository, checks out the exact proposed commit and uses read-only repository permissions. Its artifacts expire after 14 days. A successful run establishes the reported source and viewport coverage at that time; it does not prove the science, replace visual inspection, or guarantee future renderer behavior.

For an interrupted capture, preserve the failed attempt. An explicit `--resume-from /absolute/path/to/previous-capture` may reuse passing receipts only when the exact revision, page scope, runtime, contract, artifact hashes and freshness checks match. Policy or authentication failures require their actual resolution; a retry does not change access permissions.
