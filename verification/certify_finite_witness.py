"""Certify the finite-reflectivity exponent witness with rational intervals.

This evaluates the analytic global lower bound in science/finite_reflectivity.md,
not a local optimizer or a finite-sample error simulation. Every operation,
including square roots, uses outward-rounded exact rational bounds.

Run with the Python standard library only:
    python verification/certify_finite_witness.py

The output JSON records exact rational endpoints. Decimal fields are for
readability; the assertions compare rational endpoints directly.
"""

from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction
from math import isqrt
from pathlib import Path
import json


PRECISION_BITS = 160
DENOMINATOR = 1 << PRECISION_BITS


def floor_grid(value):
    value = Fraction(value)
    return Fraction((value.numerator * DENOMINATOR) // value.denominator, DENOMINATOR)


def ceil_grid(value):
    value = Fraction(value)
    return Fraction(-((-value.numerator * DENOMINATOR) // value.denominator), DENOMINATOR)


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    @classmethod
    def bounds(cls, lo, hi):
        lo, hi = Fraction(lo), Fraction(hi)
        if lo > hi:
            raise ValueError("Reversed interval")
        return cls(floor_grid(lo), ceil_grid(hi))

    @classmethod
    def exact(cls, value):
        return cls.bounds(Fraction(value), Fraction(value))

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Interval) else Interval.exact(value)

    def __add__(self, other):
        other = self.coerce(other)
        return self.bounds(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return self.bounds(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        products = [a * b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return self.bounds(min(products), max(products))

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError("Denominator interval contains zero")
        return self * self.bounds(1 / other.hi, 1 / other.lo)

    def __rtruediv__(self, other):
        return self.coerce(other) / self

    def square(self):
        if self.lo <= 0 <= self.hi:
            return self.bounds(0, max(self.lo**2, self.hi**2))
        return self.bounds(min(self.lo**2, self.hi**2), max(self.lo**2, self.hi**2))

    def sqrt(self):
        if self.lo < 0:
            raise ValueError("Square root of an interval with a negative endpoint")
        # For rational x>=0, isqrt(floor(x*D^2)) equals floor(sqrt(x)*D).
        low_integer = isqrt((self.lo.numerator * DENOMINATOR**2) // self.lo.denominator)
        high_integer = isqrt((self.hi.numerator * DENOMINATOR**2) // self.hi.denominator) + 1
        return self.bounds(Fraction(low_integer, DENOMINATOR), Fraction(high_integer, DENOMINATOR))

    def record(self):
        with localcontext() as ctx:
            ctx.prec = 38
            lo_decimal = str(Decimal(self.lo.numerator) / Decimal(self.lo.denominator))
            hi_decimal = str(Decimal(self.hi.numerator) / Decimal(self.hi.denominator))
        return {
            "lower_exact": str(self.lo),
            "upper_exact": str(self.hi),
            "lower_decimal_for_display": lo_decimal,
            "upper_decimal_for_display": hi_decimal,
        }


def certificate():
    n = Interval.exact(Fraction(1, 1000))
    background = Interval.exact(10)
    kappa = Interval.exact(Fraction(1, 10))
    sqrt_two = Interval.exact(2).sqrt()
    fraction = 2 - sqrt_two
    gaussian_rate = (3 - 2 * sqrt_two) / 2
    root_signal = (n * (n + 1)).sqrt()
    root_background = (background * (background + 1)).sqrt()
    gain = root_background / (root_background - root_signal)
    q = gain * n + (gain - 1) * (background + 1)
    b = 2 * (gain * (gain - 1) * n * (n + 1)).sqrt()
    c2 = (gain - 1) * n
    t = kappa.sqrt()
    epsilon = c2 * t / b
    delta = b * t + c2 * kappa
    maximum_mean = q + delta
    shifted_radius = gaussian_rate.sqrt() - epsilon / sqrt_two
    classical_coefficient = n / ((background + 1).sqrt() + background.sqrt()).square()
    exponent_lower = b.square() * kappa / (maximum_mean * (1 + maximum_mean)) * shifted_radius.square()
    ratio_lower = exponent_lower / (kappa * classical_coefficient)
    fisher = b.square() / (q * (1 + q))
    asymptotic_ratio = fisher * gaussian_rate / classical_coefficient

    # These strict rational comparisons establish every condition used to
    # simplify the general inside/outside bound to the displayed witness.
    checks = {
        "gain_is_finite_and_above_one": gain.lo > 1,
        "pilot_fraction_is_between_zero_and_two_thirds": 0 < fraction.lo and fraction.hi < Fraction(2, 3),
        "pilot_weight_is_the_smallest_stage_weight": (fraction / 2).hi < (1 - fraction).lo,
        "outside_cost_coefficient_exceeds_gaussian_rate": (fraction / 4).lo > gaussian_rate.hi,
        "all_target_means_are_positive_at_certificate_point": (q + c2 * kappa - b * t).lo > 0,
        "shifted_radius_is_positive": shifted_radius.lo > 0,
        "certified_ratio_exceeds_1_1926": ratio_lower.lo > Fraction(11926, 10000),
    }
    if not all(checks.values()):
        raise AssertionError(checks)

    quantities = {
        "gain": gain,
        "null_mean": q,
        "amplitude_coefficient": b,
        "quadratic_mean_shift": c2,
        "pilot_fraction": fraction,
        "gaussian_minimax_rate": gaussian_rate,
        "maximum_mean": maximum_mean,
        "fisher_information": fisher,
        "classical_exponent_coefficient": classical_coefficient,
        "finite_kappa_exponent_lower_bound": exponent_lower,
        "finite_kappa_ratio_lower_bound": ratio_lower,
        "weak_reflectivity_ratio": asymptotic_ratio,
    }
    return {
        "inputs_exact": {"n": "1/1000", "background": "10", "kappa_endpoint": "1/10"},
        "arithmetic": {"kind": "exact rational intervals with outward dyadic rounding", "precision_bits": PRECISION_BITS},
        "claim": (
            "For the declared receiver and the matched-background model, "
            "E_kappa/(kappa*C_cl) > 1.1926 for every 0 < kappa <= 1/10. "
            "The interval is extended from its endpoint by the monotonicity "
            "of the analytic lower-bound ratio, not by sampling kappa."
        ),
        "scope": "Fixed-kappa, large-N exponent certificate; not a finite-N probability bound or a global receiver optimum.",
        "checks": checks,
        "quantities": {name: value.record() for name, value in quantities.items()},
    }


if __name__ == "__main__":
    result = certificate()
    destination = Path(__file__).with_name("finite_witness_certificate.json")
    destination.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({
        "all_rational_checks_passed": all(result["checks"].values()),
        "certified_ratio_interval": result["quantities"]["finite_kappa_ratio_lower_bound"],
        "certified_exponent_lower_interval": result["quantities"]["finite_kappa_exponent_lower_bound"],
        "output": str(destination),
    }, indent=2))
