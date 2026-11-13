# Finite-reflectivity advantage and gain optimization

[Scientific route](README.md) · [Model](model.md) · [Error-exponent proof](error_exponent.md) · [Classical limit](classical_limit.md) · [Verification](../verification/README.md)

The exact transcript exponent admits a global lower bound at a specified nonzero reflectivity. For the example below, it certifies a strict advantage throughout $0<\kappa\le0.1$, without estimating a Taylor remainder or assuming that a numerical optimizer found the global minimum.

Use $q,b,c$ from the [count model](model.md#one-pair-one-counted-output), and let $e(f)$ be the [solved Gaussian minimax coefficient](error_exponent.md#allocation-law). Thus

$$
\alpha=\frac f4,\qquad \beta=\frac{1-f}{2},\qquad
f_*=2-\sqrt2,\qquad e_*=\frac{3-2\sqrt2}{2}.
$$

Throughout this page $E_f(\kappa)$ denotes the exact fixed-$\kappa$, large-sample exponent, with $n,B,G$ held fixed. It is not a finite-sample probability prediction. Equation labels beginning with F are local to this page; E labels refer to the [transcript proof](error_exponent.md).

## 1. A global finite-reflectivity lower bound

The weak-reflectivity expansion is not needed to certify a finite operating point. This section bounds the exact minimization [Eq. E22](error_exponent.md#exact-variational-exponent), retaining its asymmetric phase dependence and the lifted origin.

Let

$$
t=\sqrt\kappa,\quad \varepsilon=\frac{ct}{b},\quad
\Delta=bt+ct^2=bt(1+\varepsilon),\quad
D_+=(q+\Delta)(1+q+\Delta),
\tag{F1}
$$

and keep $w_{\min}=\min\{f/2,1-f\}$. For every $0<\kappa<1$,

$$
\boxed{\quad
E_f(\kappa)\ge
\frac{b^2\kappa}{D_+}
\min\left\{
\frac{w_{\min}}2(1+\varepsilon)^2,
\left(\sqrt{e(f)}-\frac{\varepsilon}{\sqrt2}\right)_+^2
\right\}.
\quad}
\tag{F2}
$$

Here $x_+=\max\{x,0\}$. This is a rigorous bound on all count types and all true phases, not a bound confined to a numerically found saddle.

**Proof.** The integral form of the rate is

$$
d(z\Vert\mu)=\int_\mu^z\frac{z-s}{s(1+s)}\,ds.
\tag{F3}
$$

Whenever $0\le z\le q+\Delta$ and $0<\mu\le q+\Delta$, it follows, including $z=0$ by continuity, that

$$
d(z\Vert\mu)\ge\frac{(z-\mu)^2}{2D_+}.
\tag{F4}
$$

If any observed mean exceeds $q+\Delta$, monotonicity of $d(z\Vert q)$ above $q$, followed by (F4) at $z=q+\Delta$, gives

$$
\max\{I_0,I_\theta\}\ge I_0\ge\frac{w_{\min}\Delta^2}{2D_+}.
\tag{F5}
$$

For all remaining transcripts, the observed means and every target mean lie in the one-sided box $[0,q+\Delta]^3$. Target means are strictly positive by [the model identity](model.md#one-pair-one-counted-output). Normalize the observed means as in [Eq. E37](error_exponent.md#normalized-means), and set $L_0=\alpha(x_1^2+x_2^2)+\beta y^2$. Applying (F4) gives

$$
I_0\ge\frac{b^2\kappa}{D_+}L_0,
\qquad
I_\theta\ge\frac{b^2\kappa}{D_+}L_{1,\varepsilon},
\tag{F6}
$$

where, before expanding in polar coordinates,

$$
L_{1,\varepsilon}
=\alpha(x_1-\cos\theta-\varepsilon)^2
+\alpha(x_2-\sin\theta-\varepsilon)^2
+\beta[y-\cos(\theta-\phi)-\varepsilon]^2.
\tag{F7}
$$

Write $L_1=L_{1,0}$ for the unshifted quadratic form. The vector removed on setting $\varepsilon=0$ has squared weighted norm
$\varepsilon^2(2\alpha+\beta)=\varepsilon^2/2$. The triangle inequality therefore implies

$$
\sqrt{\max\{L_0,L_{1,\varepsilon}\}}
\ge\sqrt{\max\{L_0,L_1\}}-\frac{\varepsilon}{\sqrt2}
\ge\sqrt{e(f)}-\frac{\varepsilon}{\sqrt2}.
\tag{F8}
$$

This holds also at zero pilot radius with every lifted angle. Combining the interior bound (F6)–(F8) with (F5), and minimizing over the complete space in [Eq. E22](error_exponent.md#exact-variational-exponent), proves (F2). There is no rotational-symmetry assumption in this argument. In particular, the same $c\kappa$ shift in the two differently oriented pilot means is explicitly included in (F7).

For the optimizing fraction, $f_*<2/3$, so $w_{\min}=f_*/2$, and $w_{\min}/2=f_*/4>e_*$. The first entry of the minimum in (F2) is at least $e_*$, whereas the second is at most $e_*$. Consequently

$$
\boxed{\quad
E_{f_*}(\kappa)\ge
\frac{b^2\kappa}{(q+\Delta)(1+q+\Delta)}
\left(\sqrt{e_*}-\frac{c\sqrt\kappa}{b\sqrt2}\right)_+^2,
\qquad 0<\kappa<1.
\quad}
\tag{F9}
$$

This lower bound is particularly useful because its comparison to the known-phase classical coefficient involves only elementary algebra and square roots. Its ratio to a fixed positive coefficient times $\kappa$ decreases with $\kappa$ while the bracket remains positive: the denominator increases and the positive bracket decreases. A certificate at $\kappa_0$ therefore also certifies every $0<\kappa\le\kappa_0$.

## 2. Gain optimization and an explicit finite operating interval

### 2.1 Optimizing the leading OPA information

Set $\lambda=(G-1)/G\in(0,1)$. Direct simplification of $J_G=b^2/[q(1+q)]$ gives

$$
J_G=
\frac{4n(n+1)\lambda}
{[n+(B+1)\lambda][n+1+B\lambda]}.
\tag{F10}
$$

Its reciprocal, apart from the positive numerator constant, is

$$
\frac{n(n+1)}\lambda+B(B+1)\lambda
+nB+(n+1)(B+1).
\tag{F11}
$$

If $B>n$, the minimizer is interior:

$$
\lambda_* =\sqrt{\frac{n(n+1)}{B(B+1)}},\qquad
G_* =\frac{\sqrt{B(B+1)}}{\sqrt{B(B+1)}-\sqrt{n(n+1)}},
\tag{F12}
$$

and

$$
J_*=
\frac{4n(n+1)}
{[\sqrt{(B+1)(n+1)}+\sqrt{Bn}]^2}.
\tag{F13}
$$

If $B\le n$, the leading coefficient increases with $G$ and has no finite maximizing gain; its supremum over fixed gains is

$$
\sup_{G>1}J_G=\frac{4n(n+1)}{(n+B+1)^2},
\qquad G\to\infty.
\tag{F14}
$$

This distinction matters if the formula is stated outside the bright-background regime. The main theorem holds at each fixed finite gain. Neither (F14) nor the weak-reflectivity expansion asserts that an unbounded-gain apparatus is a free physical resource.

### 2.2 Finite witness

Take

$$
n=\frac1{1000},\qquad B=10,\qquad G=G_*,\qquad f=f_*.
\tag{F15}
$$

For comparison, denote the phase-informed optimal coherent-state coefficient by

$$
C_{\rm cl}=\frac{n}{(\sqrt{B+1}+\sqrt B)^2}.
\tag{F16}
$$

The [classical-converse theorem](classical_limit.md) establishes this phase-informed exponent coefficient for the full stated classical transmitter class; (F16) is the benchmark input used here. The exact certificate (F9) gives, at $\kappa_0=1/10$,

$$
\frac{E_{f_*}(\kappa_0)}{\kappa_0 C_{\rm cl}}
\ge 1.1926527308\ldots > 1.1926.
\tag{F17}
$$

The bracket in (F9) is positive. Monotonicity stated after (F9) proves the same conservative factor $1.1926$ for every $0<\kappa\le1/10$. This is an analytic global certificate for the fixed-$\kappa$, large-$N$ exponent, independent of optimizing the exact rate numerically. It is not a finite-$N$ bound of the form $P_e\le\exp(-NE_f(\kappa))$ without a prefactor.

For orientation, the parameter values and limiting comparison are

| Quantity | Value |
|---|---:|
| $G_*$ | 1.003025748160108 |
| $q$ | 0.03428625550934725 |
| $b$ | 0.003485936439666308 |
| $c$ | 0.000003025748160108 |
| $J_*$ | 0.0003426716041750589 |
| $J_*e_*$ | 0.00002939657619807511 |
| $C_{\rm cl}$ | 0.00002382303659696906 |
| $J_*e_*/C_{\rm cl}$ | 1.233955884608563 |

The accompanying [certificate script](../verification/certify_finite_witness.py) evaluates (F9) with outward-rounded rational interval arithmetic, including all square roots, and checks the conservative inequality in (F17). The printed decimal is not the basis of the certification; the [stored certificate](../verification/finite_witness_certificate.json) records exact rational endpoints. The optional [multistart diagnostic](../verification/check_adaptive_rate.py) for [Eq. E22](error_exponent.md#exact-variational-exponent) gives a larger ratio near 1.21480 at $\kappa=0.1$; that diagnostic is compatible with (F17), but it is not needed for the theorem.
