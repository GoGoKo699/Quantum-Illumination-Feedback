# Classical illumination at a mean-energy budget

[Scientific route](README.md) · [Model](model.md) · [Finite-reflectivity separation](finite_reflectivity.md)

The quantum receiver learns the target phase from its own data. The comparison below gives a classical transmitter's receiver the true phase and arbitrary collective reception. It also permits arbitrary randomization of signal energy subject only to its mean. The resulting ceiling is therefore a deliberately favorable classical benchmark.

Natural logarithms are used. The channel and matched background are those of [the model](model.md), with $`n,B>0`$ and $`0\lt \kappa\lt 1`$.

## Preparation class and theorem

For each $`N`$, allow any fixed preparation

```math
\rho_{SI}^{(N)}
=\int P_N(d\lambda)\,
|\alpha(\lambda)\rangle\langle\alpha(\lambda)|_S
\otimes\sigma_I(\lambda),
\qquad
\int\|\alpha(\lambda)\|^2P_N(d\lambda)\le Nn.
```

Here $`\alpha`$ is an arbitrary complex $`N`$-vector, $`P_N`$ is a positive probability measure, and $`\sigma_I(\lambda)`$ is any retained state independent of target presence. The distribution can depend on $`N`$ and on the known parameters. Signal energy can be unbounded in individual realizations; no higher moment is required. The transmitter is chosen before target interaction.

This class includes all joint signal–idler states with a nonnegative **Glauber–Sudarshan P representation**, and is slightly larger because the label-conditioned idler need not be classical. It does not include every state whose signal marginal is classical: the signal marginal of a two-mode squeezed vacuum is itself thermal, but the entangled joint state has no displayed conditional-coherent product decomposition.

Define

```math
C_B=(\sqrt{B+1}-\sqrt B)^2,
\qquad z=\frac{B}{B+1},
\qquad d_B=\frac{|\log z|z^{1/4}}{\sqrt{2(1-z)}}.
```

**Classical detection theorem.** For every allowed preparation and every receiver, even when supplied with the true phase, the equal-prior error satisfies

```math
P_{e,N}\ge\frac14
\exp\left[-C_B\kappa Nn-d_B\sqrt{\kappa Nn}\right].
```

Consequently every allowed transmitter/receiver sequence obeys

```math
\limsup_{N\to\infty}-\frac1N\log P_{e,N}
\le\kappa nC_B.
```

A deterministic coherent transmitter attains this exponent when the phase is supplied. Thus

```math
E_{\mathrm{cl}}=\kappa nC_B
```

is the exact phase-informed classical optimum for this fixed-transmitter class. Giving away the phase can only improve the classical side; the same ceiling also bounds its unknown-phase worst-case task.

The coherent coefficient and the preparation-label comparison are established ingredients of [Tan et al. and Nair–Gu](../references/RELATED_WORK.md#classical-benchmark). The proof below makes the mean-energy and energy-randomization quantifiers explicit through a direct testing converse.

## A one-mode thermal testing bound

Let $`h(\rho,\sigma)`$ be the optimal equal-prior quantum error, and put

```math
\rho=\tau_B,
\qquad \sigma_x=D(\sqrt x)\tau_BD(\sqrt x)^\dagger,
\qquad h_B(x)=h(\rho,\sigma_x),\qquad x\ge0.
```

Thermal phase invariance makes the displacement's phase irrelevant to $`h_B`$. We prove the finite-energy inequality

```math
h_B(x)\ge\frac14 e^{-C_Bx-d_B\sqrt x}.
```

### Spectral reduction

For spectral decompositions $`\rho=\sum_i\lambda_i|u_i\rangle\langle u_i|`$ and $`\sigma=\sum_j\nu_j|v_j\rangle\langle v_j|`$, introduce the Nussbaum–Szkoła distributions

```math
p_{ij}=\lambda_i|\langle u_i|v_j\rangle|^2,
\qquad q_{ij}=\nu_j|\langle u_i|v_j\rangle|^2.
```

For any effect $`0\le T\le I`$ that decides the second hypothesis, decompose $`I=T+(I-T)`$ and use $`|a+b|^2\le2|a|^2+2|b|^2`$. Summing gives

```math
\begin{aligned}
\sum_{ij}\min(p_{ij},q_{ij})
&\le2\mathrm{Tr}(\rho T^2)
+2\mathrm{Tr}\big[\sigma(I-T)^2\big]\\
&\le2\mathrm{Tr}(\rho T)
+2\mathrm{Tr}\big[\sigma(I-T)\big].
\end{aligned}
```

The last expression is four times that decision's symmetric error. All sums are nonnegative, so monotone convergence establishes the same statement for the countable thermal spectra. Taking the optimal decision yields

```math
h(\rho,\sigma)\ge\frac14\sum_{ij}\min(p_{ij},q_{ij}).
```

This is the lower bound on error needed for the converse. It does not use a Chernoff *upper* bound as a converse. The spectral construction is attributed to [Nussbaum–Szkoła](../references/RELATED_WORK.md#testing-foundations).

### Exact thermal affinity

Since $`\tau_B=(1-z)z^{a^\dagger a}`$, for $`0\lt s\lt 1`$,

```math
Z_x(s)=\mathrm{Tr}(\rho^s\sigma_x^{1-s})
=e^{-xc_z(s)},
\qquad
c_z(s)=\frac{1+z-z^s-z^{1-s}}{1-z}.
```

One direct derivation normalizes each thermal power. Its occupation is $`z^s/(1-z^s)`$, while the overlap of two thermal states of occupations $`B_1,B_2`$, displaced relative to each other by energy $`x`$, is

```math
\frac{1}{1+B_1+B_2}
\exp\left[-\frac{x}{1+B_1+B_2}\right].
```

The overlap follows from a Gaussian integral in the coherent-state representation. The normalization factors of the two powers cancel its prefactor, giving $`Z_x(s)`$ above.

Also $`Z_x(s)=\sum_{ij}p_{ij}^s q_{ij}^{1-s}`$. Define the geometric-mean tilt

```math
r_{ij}=\frac{\sqrt{p_{ij}q_{ij}}}{Z_x(1/2)},
\qquad L_{ij}=\log\frac{p_{ij}}{q_{ij}}.
```

Zero-overlap terms have zero weight. Because $`B>0`$, both thermal states have full support. The moment-generating function of $`L`$ is $`Z_x(1/2+t)/Z_x(1/2)`$, finite for $`|t|\lt 1/2`$. Differentiation and symmetry around $`1/2`$ therefore give

```math
\mathbb E_rL=0,
\qquad
\mathrm{Var}_rL
=\frac{2x\sqrt z(\log z)^2}{1-z},
\qquad
c_z(1/2)=C_B.
```

Using $`\min(p,q)=\sqrt{pq}\,e^{-|\log(p/q)|/2}`$, Jensen's inequality and Cauchy–Schwarz imply

```math
\begin{aligned}
\sum_{ij}\min(p_{ij},q_{ij})
&=Z_x(1/2)\,\mathbb E_r e^{-|L|/2}\\
&\ge Z_x(1/2)e^{-\mathbb E_r|L|/2}\\
&\ge e^{-C_Bx-\sqrt{\mathrm{Var}_rL}/2}
=e^{-C_Bx-d_B\sqrt x}.
\end{aligned}
```

Together with the spectral reduction this proves the one-mode error bound, including $`x=0`$ by continuity.

## Revealing the preparation label

Give the receiver the complete label $`\lambda`$ as well as the true target phase. This can only reduce the minimum error. Conditional on the label, the retained idler is identical under both hypotheses and supplies no further information about target presence.

The thermal product $`\tau_B^{\otimes N}`$ is invariant under passive mode mixing. A label-dependent passive unitary concentrates the known displacement vector into one return mode. With $`S_\lambda=\|\alpha(\lambda)\|^2`$, the conditional discrimination problem is exactly the one-mode problem with $`x=\kappa S_\lambda`$, tensored with $`N-1`$ identical, irrelevant thermal modes.

The genie-aided error is therefore $`\mathbb E h_B(\kappa S_\lambda)`$. The original error is at least this quantity. Applying the one-mode bound and then two Jensen inequalities gives

```math
\begin{aligned}
P_{e,N}
&\ge\frac14\mathbb E e^{-C_B\kappa S_\lambda-d_B\sqrt{\kappa S_\lambda}}\\
&\ge\frac14e^{-C_B\kappa\mathbb ES_\lambda-d_B\mathbb E\sqrt{\kappa S_\lambda}}\\
&\ge\frac14e^{-C_B\kappa\mathbb ES_\lambda-d_B\sqrt{\kappa\mathbb ES_\lambda}}\\
&\ge\frac14e^{-C_B\kappa Nn-d_B\sqrt{\kappa Nn}}.
\end{aligned}
```

The first Jensen step uses convexity of the exponential. The second uses $`\mathbb E\sqrt S\le\sqrt{\mathbb ES}`$. Only the finite mean-energy budget is needed. In particular, rare large-energy realizations cannot evade this bound, even when their distribution changes with $`N`$.

## Matching coherent achievability

The quantum Chernoff trace inequality, whose original proof covers infinite-dimensional states, gives

```math
h_B(x)\le\frac12\mathrm{Tr}(\sqrt\rho\sqrt{\sigma_x})
=\frac12e^{-C_Bx}.
```

This is an **upper** bound on the attainable error. It is used here only for achievability, after the converse has been established separately. A coherent transmitter of deterministic total energy $`Nn`$ therefore attains exponent $`\kappa nC_B`$. See [Audenaert et al.](../references/RELATED_WORK.md#testing-foundations) for the trace inequality.

## Scope of the comparison

The theorem allows a global receiver and an arbitrarily complicated fixed classical mixture. It also gives that receiver the exact phase. The positive result for [the adaptive quantum receiver](finite_reflectivity.md) is consequently a strict separation from this whole class at the same mean signal energy.

Feedback-dependent **transmission**, hypothesis-dependent energy allocation, and alternative energy conventions would require their own operational benchmark. None is silently included in this fixed-preparation theorem. The idler and pump assumptions on the quantum side remain as stated in [the model](model.md).
