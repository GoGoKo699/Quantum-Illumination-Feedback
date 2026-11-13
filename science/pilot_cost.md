# Why a vanishing pilot fraction can fail

[Scientific route](README.md) · [Model](model.md) · [Positive-fraction exponent](error_exponent.md)

Consistent phase estimation does not by itself imply an exponentially reliable detection decision. For the specified one-output OPA receiver, a single pilot event proves the difference exactly.

The theorem below concerns fixed brightness and gain, two pilot settings, and one frozen main-stage phase. The final classical decision may use **every** individual count and all stage labels. Restricting the final decision to sample means is unnecessary for the obstruction.

## The exact blind direction

Use the [model's notation](model.md):

$$
q=Gn+(G-1)(B+1),\quad
b=2\sqrt{G(G-1)n(n+1)},\quad c=(G-1)n,
$$

$$
\mu_\theta(\phi)=q+b\sqrt\kappa\cos(\theta-\phi)+c\kappa,
\qquad
\mu_{\max}=q+b\sqrt\kappa+c\kappa.
$$

For every fixed $0<\kappa<1$, the mismatch

$$
\delta_\kappa=\arccos\left(-\frac{c\sqrt\kappa}{b}\right)
$$

exists in $(0,\pi)$, because

$$
\frac cb=\frac12\sqrt{\frac{(G-1)n}{G(n+1)}}<\frac12.
$$

At $\theta-\phi=\delta_\kappa$, the main output has mean exactly $q$. A geometric law is determined by its mean, so **the entire count distribution equals the target-absent distribution**. This is stronger than vanishing of a first-order score.

## An event that selects the blind setting

Let the two pilot block sizes be $m_{x,N},m_{y,N}>0$, and let

$$
M_N=m_{x,N}+m_{y,N}
$$

be the **total** number of pilot pairs. The two fixed phases are $0$ and $\pi/2$, and the phase estimate is

$$
\widehat\phi_N
=\operatorname{Arg}\big[(Z_x-q)+i(Z_y-q)\big].
$$

Consider the event $A_N$ that all pilot counts vanish. Both sample means are then zero, so the commanded phase is always

$$
\phi_0=\operatorname{Arg}(-q-iq)=-3\pi/4,
$$

independently of $N$ and the pilot block sizes. This centered vector is nonzero, so the rule at the estimator's origin plays no role here.

The event probabilities are exactly

$$
P_0(A_N)=(1+q)^{-M_N},
$$

$$
P_\theta(A_N)
=[1+\mu_\theta(0)]^{-m_{x,N}}
[1+\mu_\theta(\pi/2)]^{-m_{y,N}}.
$$

Each is at least $(1+\mu_{\max})^{-M_N}$. Choose the single fixed true phase

$$
\theta_* =\phi_0+\delta_\kappa\pmod{2\pi}.
$$

Conditional on $A_N$, all $N-M_N$ main observations have precisely the same joint distribution under $H_0$ and $H_{1,\theta_*}$.

## A lower bound for every final decision

Write $a=P_0(A_N)$ and $a_*=P_{\theta_*}(A_N)$, and let $Q$ be the common conditional main-record distribution. A possibly randomized decision $d_N$ contributes at least

$$
\frac12\int\big[a\,d_N+a_*(1-d_N)\big]dQ
\ge\frac12\min(a,a_*)
$$

to its symmetric error at $\theta_*$. Therefore

$$
\boxed{
R_N(\theta_*;d_N)
\ge\frac12(1+\mu_{\max})^{-M_N}.
}
$$

The unequal probabilities of the pilot event have already been included. A decision that recognizes those probabilities still cannot make both contributions smaller than their weighted overlap. The bound holds with the full pilot record retained and with arbitrary subsequent classical processing.

Taking a supremum over phases and an infimum over final decisions preserves the bound. If $M_N=o(N)$, then

$$
0\le\liminf_{N\to\infty}-\frac1N\log R_N^*
\le\limsup_{N\to\infty}-\frac1N\log R_N^*
\le\lim_{N\to\infty}
\frac{M_N\log(1+\mu_{\max})+\log2}{N}=0.
$$

Thus the worst-phase exponent is zero. The same fixed phase $\theta_*$ works for every $N$ with positive pilot blocks; this is not an obstruction that needs the physical phase to change with sample size.

## Boundary cases and other phase rules

Bounded positive pilot counts are covered by the exact bound. With no pilots, declare a fixed default phase $\phi_{\mathrm{default}}$ and choose its blind phase $\phi_{\mathrm{default}}+\delta_\kappa$: the whole record is then identical under the two hypotheses and its equal-prior error is $1/2$. If a sequence alternates between zero and positive pilot budgets, the per-$N$ worst-phase exponent is still zero, without asserting that two different defaults share a common pointwise blind phase.

The same per-$N$ minimax argument applies to any deterministic pilot-to-phase map: the all-zero record selects a definite setting, which has a blind target phase. If that map changes with $N$, the corresponding blind phase need not be fixed. The stronger fixed-phase statement above is for the declared argument rule.

## What the theorem says about calibration

For a positive pilot fraction, the all-zero event is exponentially rare on the same $N$ scale as the detection error. The [full-transcript calculation](error_exponent.md) accounts for it and all other pilot records, and yields a positive exponent and an optimal split within the stated policy.

The result does not apply to every phase-adaptive optical receiver. It requires fixed brightness and gain, a single frozen main setting, and **only one counted OPA output**. Continued phase exploration, two-output counting, different optical measurements or growing pilot energy can alter the statistics. A vanishing fraction of samples also need not be a vanishing fraction of energy when pilots become brighter. In particular, this theorem does not refute the phase-conjugate proposal of Jonsson et al. or the transmittance-estimation theorem of Gong–Bash; their distinctions are recorded in [related work](../references/RELATED_WORK.md).
