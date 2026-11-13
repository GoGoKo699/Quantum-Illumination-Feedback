"""Exact geometric large-deviation minimization; numerical corroboration only.

The exact transcript and weak-reflectivity proofs are in science/error_exponent.md.
The global finite-reflectivity certificate is in science/finite_reflectivity.md.
Run from the repository root: python verification/check_adaptive_rate.py
This computes the minimax rate inf_{z,theta} max(I0,I1theta), not Monte Carlo.
"""

import json
from pathlib import Path

import numpy as np
from scipy.optimize import minimize


def geometric_rate(z, mean):
    if z < 0 or mean <= 0:
        return np.inf
    if z == 0:
        return np.log1p(mean)
    delta = z - mean
    return z * np.log1p(delta / mean) - (z + 1) * np.log1p(delta / (mean + 1))


def model(n=0.001, background=10.0):
    a = np.sqrt(n * (n + 1))
    b = np.sqrt(background * (background + 1))
    gain = b / (b - a)
    null = gain * n + (gain - 1) * (background + 1)
    signal = 2 * np.sqrt(gain * (gain - 1) * n * (n + 1))
    mean_shift = (gain - 1) * n
    fisher = signal**2 / (null * (1 + null))
    classical = n / (np.sqrt(background + 1) + np.sqrt(background)) ** 2
    return gain, null, signal, mean_shift, fisher, classical


def solve(kappa, starts=24):
    n, background = 0.001, 10.0
    gain, null, signal, mean_shift, fisher, classical = model(n, background)
    fraction = 2 - np.sqrt(2)
    amplitude = signal * np.sqrt(kappa)
    norm = kappa * fisher

    def rates(v):
        ux, uy, um, theta = v[:4]
        angle = np.arctan2(uy, ux)
        zx, zy, zm = null + amplitude * np.array([ux, uy, um])
        mus = null + mean_shift * kappa + amplitude * np.cos(theta - np.array([0, np.pi / 2, angle]))
        p0 = (fraction / 2) * (geometric_rate(zx, null) + geometric_rate(zy, null))
        p0 += (1 - fraction) * geometric_rate(zm, null)
        p1 = (fraction / 2) * (geometric_rate(zx, mus[0]) + geometric_rate(zy, mus[1]))
        p1 += (1 - fraction) * geometric_rate(zm, mus[2])
        return np.array([p0, p1]) / norm

    def feasible(v):
        return v[4] - rates(v)

    f = fraction
    h = 1 - f / 2
    u = np.sqrt(f / (2 * (1 - f)))
    a = f / 4 + (1 - f) * u**2 / 2
    radius = a / (u * h)
    candidates = []
    lower = max(-3.0, -null / amplitude + 1e-6)
    bounds = [(lower, 3)] * 3 + [(-4 * np.pi, 4 * np.pi), (0, 1)]
    for theta in np.linspace(0, 2 * np.pi, starts, endpoint=False):
        for sign in [-1, 1]:
            angle = theta + sign * np.arccos(u)
            initial = np.array([radius * np.cos(angle), radius * np.sin(angle), radius, theta, 0.1])
            opt = minimize(
                lambda v: v[4], initial, method="SLSQP", bounds=bounds,
                constraints=[{"type": "ineq", "fun": feasible}],
                options={"ftol": 2e-10, "maxiter": 600, "eps": 1e-5},
            )
            actual = rates(opt.x)
            if opt.success and min(feasible(opt.x)) >= -2e-8:
                candidates.append((max(actual), opt.x, actual))
    if not candidates:
        raise RuntimeError("No successful minimization")
    score, v, actual = min(candidates, key=lambda row: row[0])
    return {
        "kappa": kappa, "n": n, "background": background, "gain": gain,
        "pilot_fraction": fraction, "fisher": fisher,
        "rate": float(score * norm), "rate_over_kappa": float(score * fisher),
        "ratio_to_optimum_known_phase_classical": float(score * fisher / classical),
        "gaussian_normalized_rate": float((12 - 8 * np.sqrt(2)) / 8),
        "normalized_exact_rate": float(score), "normalized_rates_at_saddle": actual.tolist(),
        "scaled_means_and_phase": v[:4].tolist(), "successful_starts": len(candidates),
        "starts": 2 * starts,
        "scope": "Multistart constrained optimization corroborates the exact geometric rate; not a global numerical certificate.",
    }


if __name__ == "__main__":
    results = [solve(kappa) for kappa in [0.1, 0.01, 0.001, 0.0001]]
    path = Path(__file__).with_name("adaptive_rate_checks.json")
    path.write_text(json.dumps(results, indent=2) + "\n")
    for row in results:
        print(json.dumps({k: row[k] for k in ["kappa", "rate_over_kappa", "ratio_to_optimum_known_phase_classical", "normalized_exact_rate", "successful_starts"]}))
