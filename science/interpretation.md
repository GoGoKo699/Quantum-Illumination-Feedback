# Phase feedback and its resource meaning

[Scientific route](README.md) · [Model](model.md) · [Related work](../references/RELATED_WORK.md)

## What the feedback changes

The OPA extracts a phase-sensitive signal–idler correlation. A predetermined pump phase can be nearly blind to an unknown target phase. Two balanced predetermined quadratures remove that directional blind spot, but divide the leading information between directions. Learning a direction and then measuring along it concentrates later measurements where the correlation is useful.

This is a classical control step between otherwise separate pair measurements. The decision retains the pilot record because those outcomes both reveal the setting and contain evidence about whether a target is present. Treating the estimated phase as exact would discard the probability of the wrong setting—the mechanism that determines the answer.

## The paid allocation law

Let

$$
J_G=\frac{4G(G-1)n(n+1)}{q(1+q)}.
$$

The phase-informed OPA exponent has leading coefficient $\kappa J_G/8$. The [adaptive theorem](error_exponent.md) retains a fraction

$$
R(f)=
\begin{cases}
\dfrac{4f(1-f)}{2-f},&0<f\le 2/3,\\[4pt]
1-f/2,&2/3\le f<1.
\end{cases}
$$

Its maximum is

$$
f_*=2-\sqrt2\approx0.585786,
\qquad R(f_*)=12-8\sqrt2\approx0.686292.
$$

The endpoint $f=1$ is the balanced two-setting receiver with no refinement stage, retaining one half of the phase-informed leading coefficient. A fixed single phase has zero worst-phase exponent at any fixed reflectivity because of an exact blind direction. The limit $f\downarrow0$ is consistent with the stronger [sublinear-pilot obstruction](pilot_cost.md).

The optimum spends about 58.6% of the pairs on pilots. This is not wasted data: all pilot counts enter the final likelihood. A calibration procedure can be consistent with far fewer samples, while still having rare errors too probable for an exponentially reliable detection test. The allocation law balances those rare errors against the loss of aligned main-stage measurements.

The value $f_*$ optimizes the leading coefficient of **this** two-stage policy. It is not a universal optimal allocation for every adaptive measurement or every finite reflectivity.

## A benchmark favorable to classical illumination

The [classical theorem](classical_limit.md) permits arbitrary fixed mixtures of multimode coherent signals, arbitrary retained states correlated with their classical preparation labels, arbitrary global reception, and the true target phase. Only the total mean signal energy is bounded by $Nn$.

Its optimal phase-informed exponent is

$$
E_{\rm cl}=\kappa n C_B,
\qquad
C_B=(\sqrt{B+1}-\sqrt B)^2.
$$

For $n=0.001$ and $B=10$, optimizing the leading OPA gain gives

$$
\lim_{\kappa\downarrow0}\frac{E_{f_*}(\kappa)}{E_{\rm cl}}
=1.2339558846\ldots.
$$

The [finite-reflectivity certificate](finite_reflectivity.md) also proves a strict gap at $\kappa=0.1$. Thus the constructive advantage survives charging the phase-learning uses, against a classical baseline that pays no phase-learning cost. It is an advantage in a large-sample detection exponent at equal transmitted energy, not an unqualified percentage improvement in finite-sample accuracy.

In the further low-brightness, high-background limit the ratio approaches $24-16\sqrt2\approx1.372583$. The complete collective quantum-illumination optimum and its larger known-phase enhancement are different receiver questions.

## What must remain in the claim

| Assumption or resource | Meaning for the result |
|---|---|
| One common static phase | The early estimate remains relevant to every later pair; phase drift is a different model. |
| Known reflectivity and background | The final likelihood is calibrated to these parameters; jointly learning them would require another analysis. |
| Matched background | Vacuum transmission has no target-dependent noise shadow. |
| Ideal retained idlers and photon counting | The stated exponent is for the specified optical/count model. |
| Stable local pump and controllable phase | The receiver has its own phase reference, although the target phase is unknown. |
| Full pilot record and fixed brightness | All $N$ signal uses and their $Nn$ mean signal photons are included. |
| No coherence between different pairs | Classical feedback replaces a collective receiver for this achievable advantage; each idler still requires round-trip storage. |
| Fixed classical transmitter comparison | Signal states are selected before target interaction; adaptive signal-energy allocation is outside that comparator. |

The pilot-failure theorem is particularly narrow: it concerns a single frozen phase and **one counted OPA output**. Counting another output, continuing phase exploration, changing pilot energy with sample size, or using a different optical measurement can change the conclusion. Earlier phase-conjugate receivers and two-output estimation schemes are therefore not refuted by this theorem.

## The additional scientific step

Phase learning before local reception, OPA hardware, fixed-measurement error exponents and classical controlled sensing are established ingredients. The additional step is the complete adaptive-transcript calculation: it counts rare wrong settings, gives the allocation law, and establishes a strict classical-benchmark separation for an explicit pairwise receiver. The [related-work account](../references/RELATED_WORK.md) identifies the nearest proposals and the limits of this comparison.
