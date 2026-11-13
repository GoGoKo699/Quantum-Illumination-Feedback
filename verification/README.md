# Reproducing the calculations

Run the commands below from the repository root. The required check uses only the Python standard library. Plotting and the optional numerical diagnostic use the versions in [requirements.txt](requirements.txt).

## Required: exact rational certificate

```bash
python3 verification/run_all.py
```

This calls `certificate()` in [certify_finite_witness.py](certify_finite_witness.py), checks its rational inequalities, and compares the resulting data with [finite_witness_certificate.json](finite_witness_certificate.json). It reproduces the arithmetic certificate without changing the committed output.

The certificate uses exact rational intervals with outward rounding on a 160-bit dyadic grid, including its square-root evaluations. At signal brightness `n = 1/1000`, background `B = 10`, and the declared gain and pilot fraction, it verifies the inequalities used in the bound

$$
\frac{E_\kappa}{\kappa C_{\rm cl}}>1.1926,
\qquad 0\lt \kappa\le\frac1{10},
\qquad
C_{\rm cl}=n\bigl(\sqrt{B+1}-\sqrt B\bigr)^2.
$$

The global bound and its monotonicity in reflectivity are proved in [finite_reflectivity.md](../science/finite_reflectivity.md). The script evaluates the endpoint inequalities with certified arithmetic; the extension to the whole interval follows from that analytic monotonicity argument. “Global” refers to the transcript/phase minimization for the specified receiver. It does not mean optimization over all possible receivers.

**A passing run reproduces the arithmetic, not the analytic proof.** The claimed quantity is the large-sample error exponent at fixed reflectivity, with the hypotheses and resources in [model.md](../science/model.md). It is not a finite-sample error probability. The classical comparison has its separate proof in [classical_limit.md](../science/classical_limit.md).

To regenerate the committed certificate deliberately:

```bash
python3 verification/certify_finite_witness.py
```

## Optional: exact-rate numerical diagnostic

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py --diagnostic
```

[check_adaptive_rate.py](check_adaptive_rate.py) minimizes the explicit geometric-count rate with multiple starting points at four reflectivities. It writes [adaptive_rate_checks.json](adaptive_rate_checks.json), including the fitted rate, saddle coordinates, and number of successful starts. The script can also be run directly:

```bash
python3 verification/check_adaptive_rate.py
```

This is a constrained numerical minimization, not a Monte Carlo simulation. Its best reported value is a diagnostic of the analytic result; a local optimizer cannot certify a global minimum. Solver behavior and the last digits can vary with platform, so `run_all.py` does not require exact agreement with the stored numerical JSON. The rational certificate is the required verification of the finite-reflectivity witness.

## Optional: regenerate the pilot-allocation figure

```bash
python3 verification/run_all.py --plot
```

Equivalently:

```bash
python3 verification/plot_policy.py
```

This regenerates [pilot_fraction.svg](../figures/pilot_fraction.svg) from the exact piecewise formula

$$
R(f)=
\begin{cases}
4f(1-f)/(2-f),&0\le f\le2/3,\\
1-f/2,&2/3\le f\le1.
\end{cases}
$$

The ordinate is the **weak-reflectivity leading exponent ratio to phase-informed OPA**, with sample size first tending to infinity at fixed reflectivity. The marked optimum is `f* = 2 − √2`, with `R* = 12 − 8√2`; the horizontal reference `1/2` is balanced fixed-setting OPA. The figure contains no finite-reflectivity optimizer data. The derivation is in [error_exponent.md](../science/error_exponent.md).

Both optional tasks can be requested together with `--diagnostic --plot`. The exact rational certificate runs first in every case. The declared dependencies are NumPy 2.3.5, SciPy 1.17.0, and Matplotlib 3.10.8; the SVG has a white background, editable text, fixed element identifiers, and no generation timestamp.

## Optional: check GitHub's mathematical display

The [hosted mathematics guide](hosted_math/README.md) documents a browser-based comparison between the formulas in an exact Git revision and their actual GitHub rendering, including table cells. It captures both desktop and narrow layouts for visual inspection. This checks a different question from the arithmetic certificate: whether the scientific expressions survive the hosting renderer with their operands, relations and structure intact.
