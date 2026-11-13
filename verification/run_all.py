"""Reproduce the rational certificate, with optional numerics and plotting.

The default path requires only the Python standard library and compares the
deterministic certificate with its committed JSON. This reproduces arithmetic;
it is not a proof checker for the associated mathematical arguments.
"""

import argparse
import json
from pathlib import Path
import subprocess
import sys


DIRECTORY = Path(__file__).resolve().parent


def verify_certificate():
    sys.dont_write_bytecode = True
    from certify_finite_witness import certificate

    actual = certificate()
    committed_path = DIRECTORY / "finite_witness_certificate.json"
    expected = json.loads(committed_path.read_text(encoding="utf-8"))

    if not actual["checks"] or not all(actual["checks"].values()):
        raise SystemExit("FAIL: a required rational inequality did not pass.")
    if actual != expected:
        raise SystemExit(
            "FAIL: regenerated certificate differs from "
            "verification/finite_witness_certificate.json."
        )

    print("PASS: exact rational certificate matches the committed JSON.", flush=True)
    print(f"Rational inequalities checked: {len(actual['checks'])}.", flush=True)
    ratio = actual["quantities"]["finite_kappa_ratio_lower_bound"]
    print(
        "Certified ratio lower endpoint (decimal display): "
        + ratio["lower_decimal_for_display"],
        flush=True,
    )
    print(
        "This reproduces the arithmetic certificate. The analytic proof and "
        "its assumptions are in science/finite_reflectivity.md and science/model.md.",
        flush=True,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--diagnostic",
        action="store_true",
        help="rerun optional multistart optimization and update its numerical JSON",
    )
    parser.add_argument(
        "--plot",
        action="store_true",
        help="regenerate figures/pilot_fraction.svg from the analytic ratio",
    )
    args = parser.parse_args()
    verify_certificate()

    if args.diagnostic:
        print(
            "Optional diagnostic: multistart optimization is not a global certificate.",
            flush=True,
        )
        subprocess.run(
            [sys.executable, str(DIRECTORY / "check_adaptive_rate.py")], check=True
        )
    if args.plot:
        print("Plotting the exact weak-reflectivity policy ratio.", flush=True)
        subprocess.run(
            [sys.executable, str(DIRECTORY / "plot_policy.py")], check=True
        )


if __name__ == "__main__":
    main()
