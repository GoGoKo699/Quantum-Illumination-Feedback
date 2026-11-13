"""Plot the exact leading pilot-allocation ratio, not finite-kappa data.

Run from any working directory. The SVG is written to
figures/pilot_fraction.svg relative to the repository root.
"""

from math import sqrt
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


OPTIMAL_FRACTION = 2 - sqrt(2)
OPTIMAL_RATIO = 12 - 8 * sqrt(2)
DESTINATION = Path(__file__).resolve().parents[1] / "figures" / "pilot_fraction.svg"


def policy_ratio(fraction):
    """Leading exponent divided by the phase-informed OPA coefficient."""
    if not 0 <= fraction <= 1:
        raise ValueError("The pilot fraction must lie between zero and one.")
    if fraction <= 2 / 3:
        return 4 * fraction * (1 - fraction) / (2 - fraction)
    return 1 - fraction / 2


def build_figure():
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 11,
            "mathtext.fontset": "dejavusans",
            "svg.fonttype": "none",
            "svg.hashsalt": "quantum-illumination-pilot-fraction-v1",
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "savefig.facecolor": "white",
        }
    )
    teal = "#087F8C"
    dark = "#243746"
    gray = "#687680"
    fig = plt.figure(figsize=(11.8, 7.2))
    ax = fig.add_axes((0.105, 0.245, 0.855, 0.585))

    fractions = sorted(
        set([i / 1000 for i in range(1001)] + [2 / 3, OPTIMAL_FRACTION])
    )
    ratios = [policy_ratio(fraction) for fraction in fractions]
    ax.plot(
        fractions,
        ratios,
        color=teal,
        linewidth=3,
        label=r"Two-stage OPA policy: $R(f)$",
        zorder=3,
    )
    ax.axhline(
        0.5,
        color=gray,
        linewidth=1.6,
        linestyle=(0, (6, 4)),
        label=r"Balanced fixed settings: $1/2$",
        zorder=2,
    )
    ax.vlines(
        OPTIMAL_FRACTION,
        0,
        OPTIMAL_RATIO,
        color=teal,
        linewidth=1.1,
        linestyle=(0, (2, 4)),
        alpha=0.45,
        zorder=2,
    )
    ax.scatter(
        [OPTIMAL_FRACTION],
        [OPTIMAL_RATIO],
        s=75,
        color=teal,
        edgecolor="white",
        linewidth=1.5,
        zorder=4,
    )
    ax.annotate(
        "Optimum within this policy\n"
        r"$f_* = 2-\sqrt{2} \approx 0.5858$"
        "\n"
        r"$R_* = 12-8\sqrt{2} \approx 0.6863$",
        xy=(OPTIMAL_FRACTION, OPTIMAL_RATIO),
        xytext=(0.045, 0.96),
        textcoords="axes fraction",
        ha="left",
        va="top",
        color=dark,
        fontsize=11.5,
        linespacing=1.55,
        arrowprops={
            "arrowstyle": "-",
            "color": teal,
            "linewidth": 1.1,
            "connectionstyle": "arc3,rad=0.08",
            "shrinkA": 8,
            "shrinkB": 8,
        },
        bbox={"facecolor": "white", "edgecolor": "none", "pad": 4},
    )

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([0, 0.2, 0.4, 0.6, 0.8, 1])
    ax.set_xticklabels(["0", "0.2", "0.4", "0.6", "0.8", "1"])
    ax.set_yticks([0, 0.25, 0.5, 0.75, 1])
    ax.set_yticklabels(["0", "0.25", "0.50", "0.75", "1"])
    ax.set_xlabel(r"Pilot fraction $f$ of all signal–idler pairs", labelpad=12, color=dark)
    ax.set_ylabel(r"Leading exponent ratio $R(f)$", labelpad=12, color=dark)
    ax.tick_params(axis="both", colors=gray, length=4, pad=6)
    ax.grid(axis="y", color="#E6EBEE", linewidth=0.8, zorder=0)
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color("#A8B3BA")
    ax.legend(
        loc="lower right",
        bbox_to_anchor=(0.985, 0.045),
        frameon=False,
        fontsize=11,
        labelcolor=dark,
        handlelength=3.2,
        labelspacing=0.8,
    )

    fig.text(
        0.105,
        0.955,
        "Pilot allocation and the leading error exponent",
        ha="left",
        va="top",
        fontsize=20,
        fontweight="medium",
        color=dark,
    )
    fig.text(
        0.105,
        0.90,
        "Weak-reflectivity ratio to phase-informed OPA; fixed signal brightness, background, and gain",
        ha="left",
        va="top",
        fontsize=11.5,
        color=gray,
    )
    fig.text(
        0.105,
        0.115,
        r"$R(f)=\dfrac{4f(1-f)}{2-f}$ for $0\leq f\leq 2/3$;"
        r"      $R(f)=1-f/2$ for $2/3\leq f\leq1$.",
        ha="left",
        va="center",
        fontsize=11.5,
        color=dark,
    )
    fig.text(
        0.105,
        0.052,
        r"Limit order: $N\to\infty$ at fixed $\kappa$, followed by $\kappa\to0$. "
        "The curve is analytic, not finite-reflectivity data.",
        ha="left",
        va="center",
        fontsize=10.5,
        color=gray,
    )
    return fig


def main():
    fig = build_figure()
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(
        DESTINATION,
        format="svg",
        metadata={
            "Date": None,
            "Creator": "Quantum-Illumination-Feedback: verification/plot_policy.py",
            "Title": "Exact weak-reflectivity pilot-allocation ratio",
            "Description": (
                "Leading error-exponent ratio to phase-informed OPA. "
                "R(f)=4f(1-f)/(2-f) for f<=2/3 and R(f)=1-f/2 otherwise. "
                "The optimum is f=2-sqrt(2), R=12-8sqrt(2). "
                "Balanced fixed settings give ratio 1/2."
            ),
        },
    )
    plt.close(fig)
    print(f"Saved analytic pilot-allocation plot: {DESTINATION}")


if __name__ == "__main__":
    main()
