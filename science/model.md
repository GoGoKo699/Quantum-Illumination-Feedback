# Model, measurements, and detection task

[Scientific route](README.md) · [Error exponent](error_exponent.md) · [Resource interpretation](interpretation.md)

## The question

Quantum illumination uses correlations between a transmitted signal and a retained idler to detect a noisy, weak reflection. A phase-sensitive receiver needs a suitable phase setting, but the target's phase is usually unknown. This project asks whether **classical feedback between separate pair measurements** can retain a strict detection advantage when every phase-learning use is charged to the experiment.

The phase is one unknown constant across the experiment. This differs from a phase redrawn independently on each use and from a target whose reflectivity fluctuates. The receiver below has one phase update and measures only one output of an optical parametric amplifier (OPA). Its statistics permit a complete calculation of rare calibration failures.

## Signal and channel

Fix a signal brightness $n>0$, a return background $B>0$, a power reflectivity $0<\kappa<1$, and an OPA gain $G>1$. These four parameters are known. Each of $N$ independent signal–idler pairs is a two-mode squeezed vacuum,

$$
|\psi_n\rangle_{SI}
=\frac{1}{\sqrt{n+1}}
\sum_{j=0}^{\infty}
\left(\frac{n}{n+1}\right)^{j/2}|j\rangle_S|j\rangle_I.
$$

Both marginal occupations equal $n$, and the source phase convention gives

$$
\langle a_S a_I\rangle=\sqrt{n(n+1)},\qquad
\langle a_S^\dagger a_I\rangle=0.
$$

Under $H_0$ the returned mode is an independent thermal state with occupation $B$. Under $H_{1,\theta}$,

$$
a_R=e^{i\theta}\sqrt{\kappa}\,a_S+\sqrt{1-\kappa}\,a_E,
\qquad
\langle a_E^\dagger a_E\rangle=\frac{B}{1-\kappa}.
$$

The environments are independent between uses. The unknown parameter $\theta\in[0,2\pi)$ is common to all uses. The retained idler is ideal. Thus

$$
\langle a_R^\dagger a_R\rangle_{1,\theta}=B+\kappa n,
\qquad
\langle a_Ra_I\rangle_{1,\theta}
=e^{i\theta}\sqrt{\kappa n(n+1)}.
$$

This is the standard **matched-background convention**: vacuum illumination produces the same return under both hypotheses. There is no passive background shadow to detect. The thermal occupation assigned to the environment specifies this hypothesis model; the analysis does not infer a freely available target signature from a changed background. See [Tan et al. and Nair–Gu](../references/RELATED_WORK.md#classical-benchmark).

## One pair, one counted output

At pump phase $\phi$, the measured OPA output is

$$
c_\phi=\sqrt{G}\,a_I+e^{i\phi}\sqrt{G-1}\,a_R^\dagger.
$$

It is a zero-mean Gaussian mode with $\langle c_\phi c_\phi\rangle=0$, hence a thermal mode. Its photon count is exactly geometric:

$$
p_\mu(k)=\frac{\mu^k}{(1+\mu)^{k+1}},\qquad k=0,1,2,\ldots.
$$

Define

$$
q=Gn+(G-1)(B+1),\qquad
b=2\sqrt{G(G-1)n(n+1)},\qquad c=(G-1)n.
$$

The null mean is $q$, and the alternative mean is

$$
\mu_\theta(\phi)
=q+b\sqrt{\kappa}\cos(\theta-\phi)+c\kappa.
$$

All means are strictly positive. In particular,

$$
q+c\kappa-b\sqrt{\kappa}
=\left[\sqrt{Gn}-\sqrt{(G-1)\kappa(n+1)}\right]^2
+(G-1)(B+1-\kappa)>0.
$$

The OPA apparatus, this count law, and its phase-informed detection advantage are inherited from [Guha–Erkmen (2009)](../references/RELATED_WORK.md#opa-receiver). The contribution concerns the complete adaptive record under an unknown phase.

## Paid pilot protocol

Choose a fixed pilot fraction $0<f<1$. Use $m_x=m_y=\lfloor fN/2\rfloor$ pairs at phases $0$ and $\pi/2$, respectively. Thus

$$
\frac{m_x}{N}\longrightarrow\frac f2,\qquad
\frac{m_y}{N}\longrightarrow\frac f2.
$$

Let $Z_x$ and $Z_y$ be the two photon-count sample means. Set

$$
\widehat\phi
=\operatorname{Arg}\big[(Z_x-q)+i(Z_y-q)\big],
$$

with the declared value $0$ when both centered means vanish. Measure all remaining $m_0=N-m_x-m_y$ pairs at that one phase. Their sample mean is $Z_0$.

The final decision uses the likelihood of **all three groups**, including the data-dependent commanded phase. The three count sums and their group sizes are sufficient: within each group the product of geometric probabilities depends only on the sum, and the command is a deterministic function of the first two sums. No quantum system connects measurements of different pairs.

An exact generalized likelihood-ratio test chooses $H_1$ when

$$
\sup_{\theta\in[0,2\pi)}
\frac{P_{1,\theta}(S_x,S_y,S_0)}{P_0(S_x,S_y,S_0)}\ge1.
$$

Either fixed decision at equality has the same exponent. The exact transcript probabilities, the phase-estimator singularity, and a polynomial-grid implementation of the likelihood search are treated in [the exponent proof](error_exponent.md).

## Error convention and order of limits

For a final decision rule $0\le d_N\le1$—the probability of deciding $H_1$—write

$$
\alpha_N=\mathbb E_0 d_N,\qquad
\beta_N(\theta)=\mathbb E_{1,\theta}(1-d_N),\qquad
R_N(d_N)=\frac{\alpha_N+\sup_\theta\beta_N(\theta)}2.
$$

Let $R_{N,f}^*$ be the infimum of this risk over classical decision rules **after the specified receiver protocol**. Natural logarithms define the per-pair exponent

$$
E_f(\kappa)=\lim_{N\to\infty}-\frac1N\log R_{N,f}^*.
$$

The limit exists, and the full-record generalized likelihood-ratio test attains it. This is an optimum over final decisions for a given optical protocol, not an optimum over all adaptive quantum receivers.

The weak-reflectivity theorem takes $N\to\infty$ at each fixed $\kappa$, **then** $\kappa\downarrow0$ with $n,B,G,f$ fixed. Its leading coefficient is optimized over $f$ and $G$. A separate [global bound at fixed reflectivity](finite_reflectivity.md) supplies a strict example without sending $\kappa$ to zero. Both statements concern large-sample exponents, rather than a finite-sample error prediction without prefactors.

## Charged and assumed resources

Every one of the $N$ transmitted modes has mean energy $n$ photons, including pilots, so the total mean signal energy is $Nn$. The source also produces the retained idler energy. The classical comparison uses the same signal budget and allows a stronger receiver with the true phase supplied.

The optical receiver assumes ideal idler preservation over the round trip, pairwise mode matching, a stable local pump, known gain and count calibration, and ideal photon-number resolution. It performs one classical phase update. It does not require coherence between different pairs; the physical storage and delay of the individual idlers remain part of the apparatus. Pump energy, bandwidth, propagation delay and classical computation are not converted into a total-energy or elapsed-time advantage. The [interpretation](interpretation.md) keeps these resource boundaries alongside the result.
