# Complete-transcript error exponent

[Scientific route](README.md) · [Model](model.md) · [Finite-reflectivity certificate](finite_reflectivity.md) · [Pilot cost](pilot_cost.md) · [Verification](../verification/README.md)

The specified one-update OPA receiver has an exact large-sample minimax exponent, attained by the generalized likelihood-ratio test on the complete record. This page proves that statement directly from count probabilities, resolves the phase-estimator origin and the count lattice, and then solves the weak-reflectivity allocation law.

The optical count model and OPA architecture are inherited from [Guha–Erkmen](../references/RELATED_WORK.md#opa-receiver). The [model page](model.md) supplies the physical assumptions and resource contract. The result here optimizes the final decision for this receiver; it does not optimize all adaptive measurements. Equation labels beginning with E belong to this page; labels beginning with F belong to the [finite-reflectivity proof](finite_reflectivity.md).

## 1. Experiment, policy, and precise claim

### 1.1 Exact count model

Each input is an independent two-mode squeezed-vacuum signal–idler pair of mean occupation $`n>0`$ per mode. The background brightness is $`B>0`$. Under target absence, the returned mode is thermal of mean $`B`$, independent of the idler. Under target presence,

```math
a_R=e^{i\theta}\sqrt\kappa\,a_S+\sqrt{1-\kappa}\,a_E,
\qquad \langle a_E^\dagger a_E\rangle=\frac{B}{1-\kappa},
\qquad 0\lt \kappa\lt 1.
\tag{E1}
```

Thus the background contribution is matched under the two hypotheses. The target phase $`\theta\in\mathbb T=\mathbb R/(2\pi\mathbb Z)`$ is an unknown constant for the whole experiment. The quantities $`n,B,\kappa`$, and the chosen OPA gain $`G>1`$ are known. No additional signal energy or target-phase reference is supplied.

At pump phase $`\phi`$, measure the photon number of

```math
c_\phi=\sqrt G\,a_I+e^{i\phi}\sqrt{G-1}\,a_R^\dagger.
\tag{E2}
```

Its reduced state is a zero-mean, phase-insensitive one-mode Gaussian state, hence a thermal state. The count distribution is exactly

```math
p_\mu(k)=\frac{\mu^k}{(1+\mu)^{k+1}},\qquad k\in\mathbb N_0.
\tag{E3}
```

Define

```math
q=Gn+(G-1)(B+1),\quad
b=2\sqrt{G(G-1)n(n+1)},\quad c=(G-1)n,
\tag{E4}
```

and

```math
\mu_\theta(\phi)=q+b\sqrt\kappa\cos(\theta-\phi)+c\kappa.
\tag{E5}
```

The null mean is $`q`$, and the target mean at setting $`\phi`$ is $`\mu_\theta(\phi)`$. All these means are strictly positive for the parameters in (E1):

```math
q+c\kappa-b\sqrt\kappa
=\left[\sqrt{Gn}-\sqrt{\kappa(G-1)(n+1)}\right]^2
+(G-1)(B+1-\kappa)>0.
\tag{E6}
```

Let

```math
J_G=\frac{b^2}{q(1+q)}.
\tag{E7}
```

This is the directional Fisher information for the amplitude parameter $`\sqrt\kappa`$ at the null, for a phase-aligned OPA measurement. Here it will enter through an exact large-deviation calculation, not through an assumption that local Fisher information determines an adaptive error exponent.

### 1.2 The fixed-fraction policy

Fix $`0\lt f\lt 1`$. For a total of $`N`$ pairs, set

```math
m_{p,N}=\lfloor fN/2\rfloor,\qquad m_{0,N}=N-2m_{p,N}.
\tag{E8}
```

For sufficiently large $`N`$, all three stage sizes are positive. Measure $`m_{p,N}`$ pairs at phase zero and $`m_{p,N}`$ pairs at phase $`\pi/2`$. Write their count sums as $`S_x,S_y`$ and their averages as $`Z_x,Z_y`$. Set

```math
\widehat\phi_N=\operatorname{Arg}\big[(Z_x-q)+i(Z_y-q)\big].
\tag{E9}
```

The receiver assigns phase $`0`$ at an exactly zero vector, as declared in the [model](model.md#paid-pilot-protocol). The proof works for any deterministic value there. Measure the remaining $`m_{0,N}`$ pairs at the phase $`\widehat\phi_N`$, and denote their sum and average by $`S_0,Z_0`$.

All pairs and all observed counts are retained. The three sums are sufficient for every hypothesis: conditional on them, the distribution of the ordered counts within each stage is uniform and independent of $`\theta`$. In particular, the deterministic feedback setting introduces no extra likelihood factor.

For a realized transcript, let $`P_{0,N}(s)`$ and $`P_{\theta,N}(s)`$ denote its mass under absence and presence. The decision rule is the generalized likelihood-ratio test (GLRT)

```math
\delta_N(s)=1\quad\Longleftrightarrow\quad
\sup_{\theta\in\mathbb T}\frac{P_{\theta,N}(s)}{P_{0,N}(s)}\ge1.
\tag{E10}
```

The output one means target present. Either deterministic tie convention in (E10) gives the exponent below.

Define the symmetric worst-phase risk

```math
R_N(\delta_N)
=\frac12\left[P_{0,N}(\delta_N=1)
+\sup_{\theta\in\mathbb T}P_{\theta,N}(\delta_N=0)\right].
\tag{E11}
```

The supremum is taken at each $`N`$. The proof will also provide a matching phase fixed independently of $`N`$; the result therefore does not rely on allowing the physical phase to drift with sample size.

### 1.3 Main theorem

For fixed $`n,B>0`$, $`G>1`$, $`0\lt f\lt 1`$, and every fixed $`0\lt \kappa\lt 1`$, the limit

```math
E_f(\kappa)=\lim_{N\to\infty}-\frac1N\log R_N(\delta_N)
=\lim_{N\to\infty}-\frac1N\log R_{N,f}^*
\tag{E12}
```

exists and has the exact variational representation in (E22) below. Here $`R_{N,f}^*`$ is the infimum over final classical decisions for this same optical protocol, as in the [model definition](model.md#error-convention-and-order-of-limits). No other classical decision rule applied to this same measurement transcript has a larger worst-phase exponent. At fixed $`n,B,G,f`$,

```math
E_f(\kappa)=\kappa J_G e(f)+O_{n,B,G,f}(\kappa^{3/2}),
\tag{E13}
```

where

```math
e(f)=
\begin{cases}
\dfrac{f(1-f)}{2(2-f)},&0\lt f\le2/3,\\[4pt]
\dfrac{2-f}{16},&2/3\le f\lt 1.
\end{cases}
\tag{E14}
```

The largest leading coefficient within this policy family occurs at

```math
f_*=2-\sqrt2,\qquad
e_*=\frac{3-2\sqrt2}{2},\qquad
8e_*=12-8\sqrt2.
\tag{E15}
```

Equation (E13) takes $`N\to\infty`$ first at fixed $`\kappa`$, then $`\kappa\downarrow0`$. It is not a joint-limit theorem. The [finite-reflectivity proof](finite_reflectivity.md#1-a-global-finite-reflectivity-lower-bound) gives a separate, explicit lower bound at nonzero $`\kappa`$.

## 2. Exact transcript probabilities and a lifted state space

### 2.1 Geometric type masses

For $`M\ge1`$ independent geometric counts of mean $`\mu>0`$, their sum has mass

```math
Q_{M,\mu}(s)
=\binom{s+M-1}{M-1}\frac{\mu^s}{(1+\mu)^{s+M}}.
\tag{E16}
```

Define the geometric rate function

```math
d(z\Vert\mu)
=z\log\frac z\mu-(z+1)\log\frac{z+1}{\mu+1},
\qquad z\ge0,
\tag{E17}
```

with the continuous convention at zero. For every $`M,s,\mu`$,

```math
\frac{M}{(M+s)(M+s+1)}e^{-M d(s/M\Vert\mu)}
\le Q_{M,\mu}(s)
\le e^{-M d(s/M\Vert\mu)}.
\tag{E18}
```

To verify (E18), use
$`\binom{M+s-1}{s}=M\binom{M+s}{s}/(M+s)`$, together with the elementary binary-type bounds
$`e^{(M+s)h(s/(M+s))}/(M+s+1)\le\binom{M+s}{s}\le e^{(M+s)h(s/(M+s))}`$.
Here $`h(p)=-p\log p-(1-p)\log(1-p)`$ is binary entropy, with $`0\log0=0`$.
The lower binary-type bound follows because the probability of $`s`$ under a binomial distribution of size $`M+s`$ and success probability $`s/(M+s)`$ is a mode and is at least $`1/(M+s+1)`$. This argument includes $`s=0`$.

On a bounded set $`s/M\le L`$, the lower prefactor in (E18) is at least

```math
\big[(1+L)(M(1+L)+1)\big]^{-1}.
\tag{E19}
```

The bounds are uniform in the mean; all dependence on the mean is in the displayed rate.

### 2.2 Retaining the angle at the pilot origin

The map in (E9) is discontinuous at $`(q,q)`$. It is therefore inappropriate simply to apply a contraction theorem to the three means and ignore that point. Introduce the closed lifted space

```math
\mathcal X=\left\{(z_x,z_y,z_0,\phi)\in[0,\infty)^3\times\mathbb T:
(z_x-q,z_y-q)=r(\cos\phi,\sin\phi)\text{ for some }r\ge0\right\}.
\tag{E20}
```

At $`r=0`$, all angles are included. This is a device for taking limits of actual transcripts, not an additional physical control or randomization. Every member of $`\mathcal X`$ is approximable by actual count types for every sufficiently large $`N`$:

- If $`r>0`$, round $`m_{p,N}z_x,m_{p,N}z_y,m_{0,N}z_0`$ to nonnegative integers. The resulting means converge, and their pilot angle converges to $`\phi`$.
- If $`r=0`$, first replace the pilot means by $`q+m_{p,N}^{-1/2}\cos\phi`$ and $`q+m_{p,N}^{-1/2}\sin\phi`$, then round their sums. The rounding changes each mean by $`O(m_{p,N}^{-1})`$, so the angle error is $`O(m_{p,N}^{-1/2})`$. Both means are positive eventually. Round the main sum as before.

The approximating pilot vector in the second case is nonzero for all sufficiently large $`N`$. Its existence makes the assigned value at the exact origin irrelevant to the exponent. The argument also handles boundary values $`z_j=0`$.

On $`\mathcal X`$, define the continuous rate functions

```math
\begin{aligned}
I_0(w)&=\frac f2d(z_x\Vert q)+\frac f2d(z_y\Vert q)
+(1-f)d(z_0\Vert q),\\
I_\theta(w)&=\frac f2d(z_x\Vert\mu_\theta(0))
+\frac f2d(z_y\Vert\mu_\theta(\pi/2))
+(1-f)d(z_0\Vert\mu_\theta(\phi)).
\end{aligned}
\tag{E21}
```

Write $`I_*(w)=\min_{\theta\in\mathbb T}I_\theta(w)`$. Compactness of the phase circle makes this a continuous function. The exact exponent in (E12) is

<a id="exact-variational-exponent"></a>

```math
\boxed{\quad
E_f(\kappa)
=\min_{w\in\mathcal X}\max\{I_0(w),I_*(w)\}
=\min_{w\in\mathcal X,\,\theta\in\mathbb T}
\max\{I_0(w),I_\theta(w)\}.
\quad}
\tag{E22}
```

The equality of the two expressions follows because $`I_0`$ is independent of $`\theta`$. The minima are attained: the objective is continuous and at least $`I_0`$, whose sublevel sets are compact in the three means; the two phase circles are compact as well. Indeed, $`d(z\Vert q)\to\infty`$ as $`z\to\infty`$, and all three stage weights are positive.

## 3. Proof of the fixed-reflectivity exponent

### 3.1 The exact likelihood identity

Replace the weights $`f/2,f/2,1-f`$ in (E21) by $`m_{p,N}/N,m_{p,N}/N,m_{0,N}/N`$, and denote the resulting functions by $`I_{0,N},I_{\theta,N},I_{*,N}`$. Conditional on the pilot sums, the main sum has distribution $`Q_{m_{0,N},\mu_\theta(\phi)}`$. Therefore

```math
P_{\theta,N}(s)
=Q_{m_{p,N},\mu_\theta(0)}(s_x)
Q_{m_{p,N},\mu_\theta(\pi/2)}(s_y)
Q_{m_{0,N},\mu_\theta(\phi(s))}(s_0).
\tag{E23}
```

The analogous null expression uses mean $`q`$ in all three factors. Their combinatorial factors are identical and cancel. Exactly, including the rounded stage sizes,

```math
\frac1N\log\frac{P_{\theta,N}(s)}{P_{0,N}(s)}
=I_{0,N}(w(s))-I_{\theta,N}(w(s)).
\tag{E24}
```

The GLRT thus accepts the target precisely when $`I_{0,N}\ge I_{*,N}`$. No iid composite-hypothesis Chernoff formula has been used.

### 3.2 Uniform exponential control of the tails

For this fixed $`\kappa`$, all conditional means lie in a compact positive interval. Choose $`\overline\mu\ge\max\{q,q+c\kappa+b\sqrt\kappa\}`$ and

```math
0\lt \lambda\lt \log(1+1/\overline\mu),\qquad
K(\lambda)=-\log\big[1-\overline\mu(e^\lambda-1)\big].
\tag{E25}
```

The geometric moment-generating function and Markov's inequality give, for a stage of size $`M`$,

```math
\Pr(Z>L)\le e^{-M[\lambda L-K(\lambda)]}.
\tag{E26}
```

For the main stage this bound is first applied conditionally on the pilots; the right-hand side is independent of the realized setting. Hence the same bound holds unconditionally, uniformly in $`\theta`$. For large $`N`$, each stage has at least $`Nw_{\min}/2`$ observations, where

```math
w_{\min}=\min\{f/2,1-f\}>0.
\tag{E27}
```

A union bound shows that the probability that any mean exceeds $`L`$, under either hypothesis and every phase, is at most

```math
3e^{-NT(L)},\qquad T(L)=\frac{w_{\min}}2[\lambda L-K(\lambda)]\longrightarrow\infty.
\tag{E28}
```

### 3.3 GLRT upper bound on the risk

On the bounded set $`\max_jz_j\le L`$, the rate functions with rounded weights converge to (E21) uniformly in the transcript and phase, at order $`O_L(N^{-1})`$. There are at most $`(NL+1)^3`$ possible triple sums there.

For a type on which the test accepts the target, (E18) and (E24) give

```math
P_{0,N}(s)\le e^{-NI_{0,N}(w)}
=e^{-N\max\{I_{0,N}(w),I_{*,N}(w)\}}.
\tag{E29}
```

For a type on which it rejects, $`I_{*,N}>I_{0,N}`$, and for every true phase,

```math
P_{\theta,N}(s)\le e^{-NI_{\theta,N}(w)}
\le e^{-N\max\{I_{0,N}(w),I_{*,N}(w)\}}.
\tag{E30}
```

The same inequalities hold with the other tie convention. Combining them with the bounded type count and (E28), and choosing $`L`$ with $`T(L)>E_f(\kappa)+1`$, gives

```math
R_N(\delta_N)
\le (NL+1)^3e^{-N[E_f(\kappa)-O_L(N^{-1})]}
+3e^{-NT(L)}.
\tag{E31}
```

This is uniform in the true phase, and proves $`\liminf_N-N^{-1}\log R_N\ge E_f(\kappa)`$.

### 3.4 A matching converse at one fixed phase

Choose a minimizer $`(w_*,\theta_*)`$ of the last expression in (E22). Approximate $`w_*`$ by actual types $`s_N`$ using Section 2.2, holding $`\theta_*`$ fixed. The rates with rounded weights converge at these types to $`I_0(w_*)`$ and $`I_{\theta_*}(w_*)`$. Their means remain bounded, so the product of the lower bounds (E18) is a polynomial prefactor times the corresponding exponential rate.

For any, possibly randomized, decision rule based on the transcript,

```math
R_N\ge\frac12\min\{P_{0,N}(s_N),P_{\theta_*,N}(s_N)\}
\ge e^{-N[E_f(\kappa)+o(1)]}.
\tag{E32}
```

The first inequality follows by considering the contribution from this one type to the two errors: if the probability of declaring presence at this type is $`a`$, that contribution is $`aP_0(s_N)+(1-a)P_{\theta_*}(s_N)\ge\min\{P_0(s_N),P_{\theta_*}(s_N)\}`$. Sufficiency extends the statement to rules given all individual counts. This proves the matching exponent bound and optimality of the GLRT exponent for the specified measurement policy.

The phase $`\theta_*`$ can depend on the fixed physical parameters and on $`\kappa`$, but not on $`N`$. For the GLRT, its individual symmetric risk has exponent exactly $`E_f(\kappa)`$, by (E31) and (E32). For every other fixed phase the lower limit of its risk exponent is at least $`E_f(\kappa)`$. This supplies the stated worst-phase quantifiers without exchanging a pointwise limit and an infimum.

### 3.5 A finite phase grid is sufficient

The continuous maximization in (E10) is not necessary for its exponent. Use the grid $`\{2\pi j/N:0\le j\lt N\}`$. On $`z_j\le L`$,

```math
\left|\partial_\theta d(z\Vert\mu_\theta(\phi))\right|
\le \frac{b\sqrt\kappa(L+\overline\mu)}
{\underline\mu(1+\underline\mu)},
\tag{E33}
```

where $`\underline\mu>0`$ bounds the means below. Thus the grid minimum of $`I_{\theta,N}`$ differs from its continuous minimum by at most $`C_L/N`$. The proof of (E29)–(E31) changes by only a constant exponential factor $`e^{C_L}`$ on this bounded set; (E28) still controls the complement. The converse (E32) applies to every rule. Consequently an $`O(N)`$-point phase grid gives the same exponent. This is an asymptotic computation bound, not a finite-sample error approximation.

## 4. Uniform weak-reflectivity reduction

Set $`t=\sqrt\kappa`$. The only local expansion needed is the following elementary consequence of the explicit rate function. For each fixed $`M\lt \infty`$, uniformly over $`|x|\le M`$ and $`|a|\le1`$,

```math
d(q+btx\Vert q+bta+ct^2)
=\frac{J_Gt^2}{2}(x-a)^2+O_M(t^3).
\tag{E34}
```

With the second argument $`q`$, use $`a=0`$ and omit the quadratic shift. The expansion follows because $`d`$ is smooth near $`(q,q)`$, its value and first derivatives vanish there, and its quadratic term is $`(z-\mu)^2/[2q(1+q)]`$.

It remains to show that this local expansion controls the global minimization (E22). Choose any bounded normalized transcript with nonzero pilot radius, for example a pilot vector $`(1/2,0)`$, main coordinate $`1/2`$, and $`\theta=\phi=0`$. In physical coordinates, $`z_j=q+btx_j`$. Its objective is at most $`Ct^2`$. Every minimizer of (E22) therefore has $`I_0\le Ct^2`$. Since all stage weights are positive,

```math
d(z_j\Vert q)\le C't^2\quad\text{for each }j.
\tag{E35}
```

The rate $`d(\cdot\Vert q)`$ has a unique zero at $`q`$, is coercive, and has second derivative

```math
\frac{\partial^2}{\partial z^2}d(z\Vert q)=\frac1{z(1+z)}.
\tag{E36}
```

First (E35) forces every $`z_j`$ into a fixed small neighborhood of $`q`$; then the positive lower curvature in that neighborhood gives $`|z_j-q|\le C''t`$. Thus all minimizing normalized coordinates

<a id="normalized-means"></a>

```math
(x_1,x_2,y)=\frac{(z_x-q,z_y-q,z_0-q)}{bt}
\tag{E37}
```

lie in one bounded set, independent of sufficiently small $`t`$. This is the required exclusion of remote saddles.

The lifted angle is still retained. Write

```math
(x_1,x_2)=r(\cos\phi,\sin\phi),\qquad r\ge0,
\qquad u=\cos(\theta-\phi)\in[-1,1].
\tag{E38}
```

Uniformly on the bounded relevant set, (E34) gives

```math
\begin{aligned}
\frac{I_0}{J_Gt^2}&=L_0+O(t),&
L_0&=\frac f4r^2+\frac{1-f}{2}y^2,\\
\frac{I_\theta}{J_Gt^2}&=L_1+O(t),&
L_1&=\frac f4(r^2+1-2ru)+\frac{1-f}{2}(y-u)^2.
\end{aligned}
\tag{E39}
```

The error is uniform also at $`r=0`$, because $`\phi`$ is an explicit compact variable, rather than the value of a discontinuous map. Conversely, every bounded normalized lifted state is physically feasible for all sufficiently small $`t`$, since $`q>0`$. The Gaussian minimizer identified below is bounded and has positive radius. Uniform convergence of the objectives on the bounded relevant set therefore proves

```math
E_f(\kappa)
=J_G\kappa\min_{r\ge0,\,y\in\mathbb R,\,|u|\le1}\max\{L_0,L_1\}
+O(\kappa^{3/2}).
\tag{E40}
```

The argument is uniform in all angles. In particular, an explicit rotated Gaussian witness supplies the same leading upper bound for the simple test at any prescribed true phase. Together with (E31), this also gives the same leading coefficient uniformly for the individual-phase risks, in the sense of their lower and upper large-$`N`$ exponent limits. The exact finite-$`\kappa`$ problem need not be rotation invariant: the two pilot axes and the common $`c\kappa`$ shift are retained throughout (E21)–(E22).

## 5. Exact solution of the Gaussian minimax problem

Set

```math
\alpha=\frac f4,\qquad \beta=\frac{1-f}{2},\qquad
h=\alpha+\beta=\frac{2-f}{4}.
\tag{E41}
```

For negative $`u`$, replace $`(u,y)`$ by $`(-u,-y)`$. This leaves $`L_0`$ unchanged and decreases $`L_1`$ by $`4\alpha r|u|`$. It therefore suffices to consider $`u\ge0`$.

For fixed $`u\ge0`$, introduce
$`v=(\sqrt\alpha r,\sqrt\beta y)`$ and $`w=(\sqrt\alpha,\sqrt\beta)`$. Then

```math
L_0=\|v\|^2,\qquad
L_1=\|v-uw\|^2+\alpha(1-u^2).
\tag{E42}
```

An orthogonal component of $`v`$ relative to $`w`$ raises both rates. If its scalar projection on $`w`$ is negative, replacing $`v`$ by zero lowers both rates. Otherwise projection onto $`w`$ respects $`r\ge0`$. Thus a minimizing vector has $`r=y=a\ge0`$, and the fixed-angle problem becomes

```math
\min_{a\ge0}\max\{ha^2,h(a-u)^2+\alpha(1-u^2)\}.
\tag{E43}
```

Let $`v_0=u^2`$. If $`v_0\le f/2`$, the second term at its minimum $`a=u`$ is at least the first term, and the value is $`\alpha(1-v_0)`$. If $`v_0\ge f/2`$, the minimizer is the intersection of the two quadratics,

```math
a=\frac{\alpha+\beta v_0}{2h\sqrt{v_0}},
\tag{E44}
```

and the value is

```math
g_f(v_0)=
\begin{cases}
\alpha(1-v_0),&0\le v_0\le f/2,\\[3pt]
\dfrac{(\alpha+\beta v_0)^2}{4hv_0},&f/2\le v_0\le1.
\end{cases}
\tag{E45}
```

The first branch decreases to the second. On the second branch, differentiating
$`(\alpha^2/v_0+2\alpha\beta+\beta^2v_0)/(4h)`$ gives its unique unconstrained minimizer $`v_0=\alpha/\beta=f/[2(1-f)]`$. This point always lies above $`f/2`$. It lies at or below one exactly when $`f\le2/3`$. Therefore

<a id="allocation-law"></a>

```math
\min g_f=
\begin{cases}
\alpha\beta/h=\dfrac{f(1-f)}{2(2-f)},&0\lt f\le2/3,\\[5pt]
h/4=\dfrac{2-f}{16},&2/3\le f\lt 1,
\end{cases}
\tag{E46}
```

as asserted.

For $`f\le2/3`$, an explicit minimizer is

```math
u=\sqrt{\alpha/\beta},\qquad
r=y=\frac{\sqrt{\alpha\beta}}h>0.
\tag{E47}
```

For $`f\ge2/3`$, use $`u=1`$ and $`r=y=1/2`$. In both cases $`r=y\le1/2`$. For any desired true phase $`\theta`$, choose $`\phi=\theta-\arccos u`$; hence the same local value is available at every phase. No minimizer used for the matching leading bound lies at the pilot origin.

Differentiating the first branch of (E46) yields

```math
e'(f)=\frac{f^2-4f+2}{2(2-f)^2};
\tag{E48}
```

the second branch is strictly decreasing. This proves the global optimum (E15) within the prescribed split-and-freeze policy.

The endpoint $`f=1`$ can be defined separately by measuring all pairs at the two balanced predetermined phases, without a main stage. The same two-dimensional type argument gives $`E_1(\kappa)=\kappa J_G/16+O(\kappa^{3/2})`$, matching the continuous limit of (E14). The formula as $`f\downarrow0`$ tends to zero. The proof above is for fixed positive $`f`$, and does not justify inserting a sequence $`f_N\downarrow0`$ into its remainder; the [sublinear-pilot obstruction](pilot_cost.md) is a separate theorem.
