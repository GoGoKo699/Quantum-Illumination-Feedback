# Milestones from optical ingredients to phase-feedback reliability

[Learning route](README.md) · [Anchor-to-project bridge](bridge.md) · [Scientific account](../science/README.md)

This map has **30 milestones: 12 background/preliminaries and 18 narrative/innovation**. The first phase builds from an individual optical mode, through states and measurements, to the complete illumination experiment and its performance criterion. The second builds from the paid feedback rule and its probability law, through the exact and local proofs, to the classical comparison, finite-reflectivity certificate, calibration obstruction, and physical meaning of the whole contribution.

The allocation follows that scientific structure. The optical ingredients require a common foundation, while the central result requires more steps to connect adaptive control, rare-event statistics, and a comparison that charges every transmitted pair. The map identifies the load-bearing ideas; the linked scientific pages retain the specialist derivations.

The sole educational anchor is Jeffrey H. Shapiro, *The Quantum Illumination Story* (2020), in the selected [author version arXiv:1910.12277v4](https://arxiv.org/abs/1910.12277v4), dated 23 December 2019. Page and equation pointers below refer to that version's numbered PDF pages. The review supplies optical and detection context. Where a milestone concerns the adaptive transcript or another project derivation, its anchor pointer is contextual; the linked project proof supplies the result.

The notation is the project's: $N$ is the total number of pairs, $n$ their fixed signal brightness, $B$ the matched return background, and $\kappa$ the power reflectivity. In the two-stage protocol, $0\lt f\lt 1$. The two equal pilot groups each have $m_{p,N}$ pairs; their total is $M_N=2m_{p,N}$ in the fixed-fraction protocol. The main group has $m_{0,N}=N-M_N$ pairs. The target phase is one unknown constant throughout the experiment. The large-sample limit at fixed reflectivity precedes the weak-reflectivity limit.

## Background/preliminaries — M01–M12

<a id="m01"></a>

### M01 — Optical modes and counted energy

**Phase:** Background/preliminaries.

**Central question:** What physical object does one use of the illumination experiment represent?

**Understanding target:** Relate a signal or idler mode, its annihilation operator, its number states, and its mean photon number. Distinguish one mode's occupation from the number of independent signal–idler pairs.

**Dependencies and story role:** No earlier milestone is required. This identifies the local objects from which the source, channel, and receiver are assembled.

**Conceptual connection:** Counting modes and counting photons are different operations; both are needed to interpret the total signal budget and the per-pair error exponent.

**Sources:** Anchor: [pp. 3–4, Eqs. (8)–(10)](https://arxiv.org/pdf/1910.12277v4#page=3), and [p. 12, Eqs. (B1)–(B2)](https://arxiv.org/pdf/1910.12277v4#page=12). Project: [signal and channel](../science/model.md#signal-and-channel).

<a id="m02"></a>

### M02 — Coherent and thermal states

**Phase:** Background/preliminaries.

**Central question:** How can two optical states with the same mean energy carry different information?

**Understanding target:** Distinguish a coherent displacement from a zero-mean thermal fluctuation, and separate a state's amplitude, occupation, and photon-count distribution. Recognize that specifying mean energy alone does not specify the source state.

**Dependencies and story role:** Builds on [M01](#m01). It introduces the contrasting states used for the classical signal, background, and measured OPA output.

**Conceptual connection:** The detection problem compares states with different correlations or displacements while keeping the transmitted-energy accounting explicit.

**Sources:** Anchor: [p. 4, Gaussian-state moments](https://arxiv.org/pdf/1910.12277v4#page=4), and [p. 12, Eqs. (B3)–(B4)](https://arxiv.org/pdf/1910.12277v4#page=12). Project: [signal and channel](../science/model.md#signal-and-channel), [one counted output](../science/model.md#one-pair-one-counted-output), and [thermal testing model](../science/classical_limit.md#a-one-mode-thermal-testing-bound).

<a id="m03"></a>

### M03 — What the TMSV pair supplies

**Phase:** Background/preliminaries.

**Central question:** What distinguishes an entangled signal–idler pair from two thermal beams?

**Understanding target:** Connect the paired number-state expansion of a two-mode squeezed vacuum to its thermal marginals and phase-sensitive signal–idler correlation. Distinguish a classical marginal from a classical joint preparation.

**Dependencies and story role:** Uses [M01](#m01) and [M02](#m02). It adds the correlation resource before introducing target loss and noise.

**Conceptual connection:** The signal alone has thermal statistics; the useful resource is in the joint state and the receiver's access to the retained idler.

**Sources:** Anchor: [p. 12, Eq. (B3)](https://arxiv.org/pdf/1910.12277v4#page=12), and [pp. 4–5, Eqs. (11)–(14)](https://arxiv.org/pdf/1910.12277v4#page=4). Project: [TMSV source](../science/model.md#signal-and-channel) and [classical preparation class](../science/classical_limit.md#preparation-class-and-theorem).

<a id="m04"></a>

### M04 — The matched-background return

**Phase:** Background/preliminaries.

**Central question:** Which feature of the returned light is evidence for a target?

**Understanding target:** Track the signal through loss, a common phase shift, and thermal noise. Explain why the environment occupation is chosen so that vacuum illumination has the same return under both hypotheses, and distinguish the return occupation from the signal–idler correlation.

**Dependencies and story role:** Uses [M02](#m02) and [M03](#m03). It turns the source into a specified two-hypothesis physical experiment.

**Conceptual connection:** Matching the background removes a passive noise-shadow cue, leaving a comparison about illumination and reception under the stated channel.

**Sources:** Anchor: [p. 5, return-mode transformation and Eq. (14)](https://arxiv.org/pdf/1910.12277v4#page=5). Project: [signal and channel](../science/model.md#signal-and-channel), including its explicit bath convention and common-phase assumption.

<a id="m05"></a>

### M05 — Turning correlation into an OPA count signal

**Phase:** Background/preliminaries.

**Central question:** How does a pairwise optical operation make the correlation observable?

**Understanding target:** Explain how the OPA mixes the idler with the conjugated return, how the pump phase selects a correlation quadrature, and why counting one output can reveal target presence.

**Dependencies and story role:** Uses [M03](#m03) and [M04](#m04). It introduces the actual receiver component before discussing its statistical performance.

**Conceptual connection:** The operator $c_\phi$ describes an optical mode, while the scalar $c$ in the output mean is a coefficient. Keeping that distinction connects the hardware transformation to the count model.

**Sources:** Anchor: [pp. 5–6, OPA discussion and Eqs. (15)–(16)](https://arxiv.org/pdf/1910.12277v4#page=6), with [p. 12, Appendix C](https://arxiv.org/pdf/1910.12277v4#page=12) for correlation quadratures. Project: [one pair, one counted output](../science/model.md#one-pair-one-counted-output).

<a id="m06"></a>

### M06 — Exact geometric photon counts

**Phase:** Background/preliminaries.

**Central question:** What probability law replaces the optical state after measurement?

**Understanding target:** Relate a zero-mean, phase-insensitive Gaussian output to a thermal state and its geometric count law. Explain why its mean determines the whole one-output distribution, rather than merely its first moment.

**Dependencies and story role:** Uses [M02](#m02) and [M05](#m05). It establishes the classical statistical building block used throughout the proof.

**Conceptual connection:** The exact law permits both a full likelihood calculation and an exact blind-direction argument; a signal-to-noise summary alone would not provide either.

**Sources:** Anchor context: [p. 6, counted OPA output and Eqs. (15)–(16)](https://arxiv.org/pdf/1910.12277v4#page=6). Project derivation: [exact count model, Eqs. E3–E6](../science/error_exponent.md#11-exact-count-model).

<a id="m07"></a>

### M07 — Phase sensitivity and directional blindness

**Phase:** Background/preliminaries.

**Central question:** Why can a useful correlation become invisible at an unsuitable receiver phase?

**Understanding target:** Read the dependence on $\cos(\theta-\phi)$ in the measured mean and distinguish the unknown target phase from the controlled pump phase. Relate phase alignment to the accessible correlation quadrature.

**Dependencies and story role:** Uses [M04](#m04), [M05](#m05), and [M06](#m06). It identifies the nuisance parameter that motivates feedback.

**Conceptual connection:** A common unknown phase is information that can be learned across pairs; a phase redrawn on each pair defines a different experiment.

**Sources:** Anchor: [p. 6, assumptions following Eq. (17)](https://arxiv.org/pdf/1910.12277v4#page=6), and [p. 10, phase-information comparison](https://arxiv.org/pdf/1910.12277v4#page=10). Project: [measured mean](../science/model.md#one-pair-one-counted-output) and [what feedback changes](../science/interpretation.md#what-the-feedback-changes).

<a id="m08"></a>

### M08 — A classical comparator with the same signal budget

**Phase:** Background/preliminaries.

**Central question:** Against which preparations and resources should a quantum advantage be compared?

**Understanding target:** Identify the class of coherent-signal mixtures with label-conditioned retained states, the total mean signal budget $Nn$, and the phase-informed collective receiver allowed on the classical side. Distinguish that class from a condition on the signal marginal alone.

**Dependencies and story role:** Uses [M02](#m02), [M03](#m03), and [M04](#m04). It fixes the comparison before any receiver advantage is asserted.

**Conceptual connection:** A gain over one chosen classical detector is weaker than a gain over the complete stated preparation and reception class.

**Sources:** Anchor: [pp. 2–3, classical-state comparison and Eqs. (4)–(7)](https://arxiv.org/pdf/1910.12277v4#page=2). Project: [preparation class and theorem](../science/classical_limit.md#preparation-class-and-theorem) and [charged resources](../science/model.md#charged-and-assumed-resources).

<a id="m09"></a>

### M09 — Symmetric detection with a common unknown phase

**Phase:** Background/preliminaries.

**Central question:** What does it mean for a detection rule to work for an unknown phase?

**Understanding target:** Distinguish false alarms, phase-dependent misses, symmetric risk, and the worst-phase supremum. Explain the difference between a known-phase binary problem, a phase-averaged problem, and this minimax problem with one static nuisance parameter.

**Dependencies and story role:** Uses [M04](#m04), [M07](#m07), and [M08](#m08). It combines the physical hypotheses with the exact decision criterion.

**Conceptual connection:** The classical side may be given the phase while the adaptive receiver must learn it; that asymmetry makes the eventual benchmark favorable to classical illumination.

**Sources:** Anchor context: [p. 10, ROC and phase-information discussion](https://arxiv.org/pdf/1910.12277v4#page=10). Project definition: [error convention and order of limits](../science/model.md#error-convention-and-order-of-limits), and [risk, Eq. E11](../science/error_exponent.md#12-the-fixed-fraction-policy).

<a id="m10"></a>

### M10 — Reliability exponents versus estimation accuracy

**Phase:** Background/preliminaries.

**Central question:** Why does an accurate phase estimate not automatically imply a good detection exponent?

**Understanding target:** Separate typical estimation error or asymptotic variance from the probability of rare misleading records. Interpret a per-pair error exponent and retain the order: large sample size at fixed reflectivity, then weak reflectivity at fixed receiver parameters.

**Dependencies and story role:** Uses [M06](#m06) and [M09](#m09). It introduces the global reliability requirement that the feedback analysis must satisfy.

**Conceptual connection:** A calibration event negligible for mean-square performance can still dominate an exponentially small detection error.

**Sources:** Anchor context: [p. 13, explanatory reference [12]](https://arxiv.org/pdf/1910.12277v4#page=13), and [p. 6, Eq. (17)](https://arxiv.org/pdf/1910.12277v4#page=6). Project: [limiting convention](../science/model.md#error-convention-and-order-of-limits) and [calibration distinction](../science/pilot_cost.md#what-the-theorem-says-about-calibration).

<a id="m11"></a>

### M11 — Geometric relative entropy and rare sample means

**Phase:** Background/preliminaries.

**Central question:** How is the probability cost of an atypical count average quantified?

**Understanding target:** Interpret $d(z\Vert\mu)$ as the geometric sample-mean rate, with a unique zero at the true mean and positive local curvature. Distinguish this exact large-deviation cost from a Gaussian approximation near the mean.

**Dependencies and story role:** Uses [M06](#m06) and [M10](#m10). It supplies the statistical language for rare pilot records and later global minimization.

**Conceptual connection:** The same count law supports both the exact nonquadratic rate and its controlled local quadratic limit; the latter must be justified over all relevant records.

**Sources:** Anchor context: [p. 6, photon counting and its exponent](https://arxiv.org/pdf/1910.12277v4#page=6). Project derivation: [geometric rate, Eq. E17](../science/error_exponent.md#21-geometric-type-masses), and [curvature, Eq. E36](../science/error_exponent.md#4-uniform-weak-reflectivity-reduction).

<a id="m12"></a>

### M12 — The complete illumination framework

**Phase:** Background/preliminaries.

**Central question:** How do the source, channel, receiver, budget, and error criterion fit together?

**Understanding target:** Assemble the known-phase illumination comparison and identify the changed question here: whether paid classical feedback between pair measurements retains advantage under one unknown static phase. Keep the classical, pairwise OPA, and collective receiver benchmarks distinct.

**Dependencies and story role:** Integrates [M05](#m05) and [M07](#m07)–[M11](#m11). It closes the background phase with the whole experiment rather than another isolated optical ingredient.

**Conceptual connection:** An enhanced correlation is only a possible resource; a complete advantage statement also needs an allowed receiver, a performance proof, and a matched comparison.

**Sources:** Anchor: [pp. 3–6, Eqs. (6)–(7), (14), and (17)](https://arxiv.org/pdf/1910.12277v4#page=3). Project: [the question](../science/model.md#the-question), [scientific dependencies](../science/README.md#the-logical-dependencies), and [benchmark interpretation](../science/interpretation.md#a-benchmark-favorable-to-classical-illumination).

## Narrative/innovation — M13–M30

<a id="m13"></a>

### M13 — Paying for the pilot stage

**Phase:** Narrative/innovation.

**Central question:** Which observations and photons belong to the feedback experiment?

**Understanding target:** Track two equal pilot groups of size $m_{p,N}=\lfloor fN/2\rfloor$, the remaining $m_{0,N}$ pairs, and their common fixed brightness. Explain why all $N$ pairs contribute both to the transmitted-energy budget and to the final evidence.

**Dependencies and story role:** Uses [M08](#m08) and [M12](#m12). It begins the new mechanism with its charged resources rather than assuming a free calibration stage.

**Conceptual connection:** The pilot fraction changes the information allocation within a single detection experiment; it is not a separate source of uncounted phase knowledge.

**Sources:** Anchor context: [p. 3, transmitted-energy comparison](https://arxiv.org/pdf/1910.12277v4#page=3). Project: [fixed-fraction policy, Eq. E8](../science/error_exponent.md#12-the-fixed-fraction-policy) and [resource accounting](../science/model.md#charged-and-assumed-resources).

<a id="m14"></a>

### M14 — The unshifted argument rule

**Phase:** Narrative/innovation.

**Central question:** Exactly how do the pilot counts choose the main receiver phase?

**Understanding target:** Interpret the argument of $(Z_x-q)+i(Z_y-q)$ as the commanded phase and preserve its declared centering at the null mean $q$. Distinguish the estimator's zero vector from a pilot record containing zero photons, and retain the assigned phase zero at the former.

**Dependencies and story role:** Uses [M07](#m07) and [M13](#m13). It makes the control policy explicit before any likelihood or accuracy claim.

**Conceptual connection:** The command depends on noisy data even under target absence. The proof must analyze that dependence, including misleading directions, rather than substitute the true target phase.

**Sources:** Anchor context: [p. 10, OPA phase-information requirement](https://arxiv.org/pdf/1910.12277v4#page=10). Project definition: [paid pilot protocol](../science/model.md#paid-pilot-protocol) and [Eq. E9](../science/error_exponent.md#12-the-fixed-fraction-policy).

<a id="m15"></a>

### M15 — Conditioning the adaptive transcript

**Phase:** Narrative/innovation.

**Central question:** How is the probability of the full record computed when a setting depends on earlier data?

**Understanding target:** Factor the joint record into the two pilot probabilities and the main probability conditional on those pilots. Explain why the last group is geometric at the realized setting and why the deterministic command adds no extra likelihood factor.

**Dependencies and story role:** Uses [M06](#m06) and [M14](#m14). It turns the optical feedback mechanism into an exact statistical experiment.

**Conceptual connection:** Conditional independence of later counts does not make the complete adaptive record an identically distributed sequence. The correct factorization preserves both the setting information and its probability cost.

**Sources:** Anchor context: [p. 6, OPA conditional means, Eq. (16)](https://arxiv.org/pdf/1910.12277v4#page=6). Project derivation: [exact likelihood identity, Eq. E23](../science/error_exponent.md#31-the-exact-likelihood-identity).

<a id="m16"></a>

### M16 — Sufficient sums and the complete likelihood

**Phase:** Narrative/innovation.

**Central question:** Why can three count sums retain all the evidence without discarding the pilots?

**Understanding target:** Explain sufficiency of the stage sums, the hypothesis-independent distribution of ordered records within a type, and cancellation of the negative-binomial multiplicities in the likelihood ratio. Connect the complete likelihood to the difference of null and target rate functions.

**Dependencies and story role:** Uses [M11](#m11) and [M15](#m15). It supplies the exact identity used by both the GLRT and the converse for arbitrary final decisions.

**Conceptual connection:** Compressing a sufficient record is compatible with retaining every observation's evidence; discarding the pilot likelihood is a different operation.

**Sources:** Anchor context: [p. 6, summed photon observable, Eq. (15)](https://arxiv.org/pdf/1910.12277v4#page=6). Project derivation: [sufficiency in the policy](../science/error_exponent.md#12-the-fixed-fraction-policy) and [Eq. E24](../science/error_exponent.md#31-the-exact-likelihood-identity).

<a id="m17"></a>

### M17 — The pilot origin and the count lattice

**Phase:** Narrative/innovation.

**Central question:** How can a discontinuous phase estimate have a controlled error exponent?

**Understanding target:** Explain why the limiting state retains an approach angle at zero pilot radius, and why this adds no physical randomization. Understand how actual integer count types approach every lifted origin angle with radial displacement larger than the lattice spacing.

**Dependencies and story role:** Uses [M14](#m14) and [M15](#m15). It resolves the singular control rule before the global asymptotic argument is assembled.

**Conceptual connection:** A receiver's value at one exact record and the neighboring rare records can have different roles. The closure needed for an exponent must describe physically attainable approximations.

**Sources:** Anchor context: [p. 6, phase-matching requirement following Eq. (17)](https://arxiv.org/pdf/1910.12277v4#page=6). Project derivation: [lifted state and lattice construction, Eqs. E20–E22](../science/error_exponent.md#22-retaining-the-angle-at-the-pilot-origin).

<a id="m18"></a>

### M18 — Exact count-type bounds

**Phase:** Narrative/innovation.

**Central question:** What justifies replacing transcript probabilities by exponential rates?

**Understanding target:** Relate a geometric block sum to its negative-binomial mass and bound that mass above and below by its exponential rate with polynomial factors. Understand why those factors vanish on the per-pair logarithmic scale.

**Dependencies and story role:** Uses [M11](#m11), [M16](#m16), and [M17](#m17). It supplies probability bounds for real count types, rather than assuming an iid Chernoff formula for an adaptive experiment.

**Conceptual connection:** The same bounds support a sum over possible error records and a lower bound from one carefully chosen record.

**Sources:** Anchor context: [p. 13, reference [12] and its iid scope](https://arxiv.org/pdf/1910.12277v4#page=13). Project derivation: [geometric type masses, Eqs. E16–E19](../science/error_exponent.md#21-geometric-type-masses).

<a id="m19"></a>

### M19 — Tails, compactness, and a global minimizer

**Phase:** Narrative/innovation.

**Central question:** Why can unbounded counts and a continuum of phases be controlled uniformly?

**Understanding target:** Connect a uniform geometric moment-generating-function bound to exponentially small tails, and connect the coercive null rate to compact relevant sets and an attained variational minimum. Keep the bound uniform in both the true phase and the realized command.

**Dependencies and story role:** Uses [M17](#m17) and [M18](#m18). It completes the analytic setting needed to turn local type estimates into a global theorem.

**Conceptual connection:** Restricting attention to a convenient bounded set becomes legitimate only after the excluded records have been bounded on the same exponential scale.

**Sources:** Anchor context: [p. 6, the photon-count detection problem](https://arxiv.org/pdf/1910.12277v4#page=6). Project derivation: [attainment following Eq. E22](../science/error_exponent.md#exact-variational-exponent) and [uniform tails, Eqs. E25–E28](../science/error_exponent.md#32-uniform-exponential-control-of-the-tails).

<a id="m20"></a>

### M20 — The exact minimax exponent and a fixed-phase converse

**Phase:** Narrative/innovation.

**Central question:** Why is the rate-function minimization the achievable worst-phase detection exponent?

**Understanding target:** Connect GLRT decision regions to a uniform upper bound on risk, and a single-type overlap to a converse at one phase fixed independently of $N$. Interpret the minimization of the larger of the two rate costs and the exponent-optimality of the GLRT for this specified optical protocol.

**Dependencies and story role:** Integrates [M09](#m09), [M16](#m16), [M18](#m18), and [M19](#m19). It closes the first full proof: the exact fixed-reflectivity experiment has an operational exponent.

**Conceptual connection:** A converse for every final decision and an attainable GLRT bound meet under the same measurement policy. They do not establish optimality over all adaptive receivers; a polynomial phase grid is sufficient for the stated exponent.

**Sources:** Anchor context: [p. 13, reference [12]](https://arxiv.org/pdf/1910.12277v4#page=13). Project proof: [variational formula, Eq. E22](../science/error_exponent.md#exact-variational-exponent), [GLRT risk bound](../science/error_exponent.md#33-glrt-upper-bound-on-the-risk), [fixed-phase converse](../science/error_exponent.md#34-a-matching-converse-at-one-fixed-phase), and [phase grid](../science/error_exponent.md#35-a-finite-phase-grid-is-sufficient).

<a id="m21"></a>

### M21 — Localizing the global weak-reflectivity problem

**Phase:** Narrative/innovation.

**Central question:** When is a quadratic approximation valid for the records that determine the error exponent?

**Understanding target:** Explain how an order-$\kappa$ trial value and domination by the null rate force all relevant sample means within order $\sqrt\kappa$ of $q$. Connect this localization to the uniform remainder of order $\kappa^{3/2}$ at fixed $n,B,G,f$.

**Dependencies and story role:** Uses [M11](#m11) and [M20](#m20). It derives a manageable local problem from the exact global theorem.

**Conceptual connection:** The Gaussian form is justified over all potentially minimizing records, including rare ones. A central-limit description of typical data alone would leave that gap open.

**Sources:** Anchor context: [p. 3, weak-signal exponent regimes, Eqs. (6)–(7)](https://arxiv.org/pdf/1910.12277v4#page=3). Project derivation: [uniform weak-reflectivity reduction, Eqs. E34–E40](../science/error_exponent.md#4-uniform-weak-reflectivity-reduction), with the [limiting convention](../science/model.md#error-convention-and-order-of-limits).

<a id="m22"></a>

### M22 — The two branches of the allocation law

**Phase:** Narrative/innovation.

**Central question:** Why does the leading exponent change form when the pilot fraction crosses two thirds?

**Understanding target:** Interpret the pilot radius, phase alignment, and main-stage fluctuation in the quadratic minimax problem. Explain the reduction to aligned scalar coordinates and the transition from an interior angular minimizer to the boundary at perfect alignment.

**Dependencies and story role:** Uses [M21](#m21). It solves the local geometry and explains the two branches of $e(f)$ rather than treating them as fitted formulas.

**Conceptual connection:** The exponent is determined by the most economical misleading record, whose geometry changes with the allocation. Treat $f=1$ as a separate balanced fixed-setting experiment, since the implemented two-stage policy has $0\lt f\lt 1$.

**Sources:** Anchor context: [p. 6, phase-informed OPA benchmark, Eq. (17)](https://arxiv.org/pdf/1910.12277v4#page=6). Project derivation: [Gaussian minimax solution, Eqs. E41–E47](../science/error_exponent.md#5-exact-solution-of-the-gaussian-minimax-problem).

<a id="m23"></a>

### M23 — The optimal paid pilot fraction

**Phase:** Narrative/innovation.

**Central question:** How much of this experiment should be allocated to learning the measurement direction?

**Understanding target:** Explain why $f_*=2-\sqrt2$ maximizes the leading exponent within the declared policy and why pilot outcomes remain useful detection data. Distinguish the retained fraction $12-8\sqrt2$ of phase-informed OPA performance from a ratio to the classical optimum.

**Dependencies and story role:** Uses [M13](#m13) and [M22](#m22). It converts the solved geometry into an explicit receiver allocation.

**Conceptual connection:** The approximately 58.6% pilot share pays for rare-setting reliability. It is neither a universal adaptive optimum nor an optimizer asserted for every finite reflectivity.

**Sources:** Anchor context: [p. 6, Eq. (17)](https://arxiv.org/pdf/1910.12277v4#page=6). Project: [allocation and derivative, Eqs. E46–E48](../science/error_exponent.md#allocation-law), [paid allocation interpretation](../science/interpretation.md#the-paid-allocation-law), and [allocation figure](../figures/pilot_fraction.svg).

<a id="m24"></a>

### M24 — Optimizing a fixed OPA gain

**Phase:** Narrative/innovation.

**Central question:** How does amplifier gain balance useful correlation against output fluctuations?

**Understanding target:** Connect the exact directional information $J_G$ to the source, background, and gain. Distinguish the finite leading-order optimum when $B>n$ from the unbounded-gain supremum when $B\le n$.

**Dependencies and story role:** Uses [M05](#m05), [M21](#m21), and [M23](#m23). It selects a concrete fixed receiver gain for the subsequent comparison.

**Conceptual connection:** Optimizing the weak-reflectivity coefficient over fixed gains is separate from taking gain to infinity inside the asymptotic proof or declaring pump resources free.

**Sources:** Anchor: [p. 6, low-gain discussion before Eq. (17)](https://arxiv.org/pdf/1910.12277v4#page=6). Project derivation: [gain optimization, Eqs. F10–F14](../science/finite_reflectivity.md#21-optimizing-the-leading-opa-information).

<a id="m25"></a>

### M25 — A classical ceiling uniform under energy randomization

**Phase:** Narrative/innovation.

**Central question:** Why can rare bright classical signals not evade the mean-energy benchmark?

**Understanding target:** Follow the preparation-label and phase genie, passive concentration to one displaced thermal mode, and a finite-energy error lower bound that survives averaging over arbitrary signal-energy distributions. Distinguish this converse from the Chernoff error upper bound used for matching coherent achievability.

**Dependencies and story role:** Uses [M08](#m08), [M10](#m10), [M12](#m12), and [M20](#m20). It establishes the comparator for the complete preparation class rather than one classical receiver.

**Conceptual connection:** The statistical proof must remain valid when the classical preparation changes with $N$ and has only a finite mean-energy constraint. The spectral and thermal-affinity arguments are substantive proof ingredients supplied by the project account.

**Sources:** Anchor context: [p. 3, Eq. (4) and classical optimality discussion](https://arxiv.org/pdf/1910.12277v4#page=3). Project proof: [one-mode bound](../science/classical_limit.md#a-one-mode-thermal-testing-bound), [preparation-label averaging](../science/classical_limit.md#revealing-the-preparation-label), and [matching coherent achievability](../science/classical_limit.md#matching-coherent-achievability).

<a id="m26"></a>

### M26 — A global bound at finite reflectivity

**Phase:** Narrative/innovation.

**Central question:** How can a strict gap be certified without relying on an unspecified asymptotic remainder?

**Understanding target:** Understand the split between a bounded count box and its complement, the geometric-curvature bound inside, the null-rate cost outside, and the triangle inequality controlling the common $c\kappa$ shift. Keep the exact asymmetric phase dependence and all lifted origin angles.

**Dependencies and story role:** Uses [M20](#m20), [M22](#m22), and [M25](#m25). It converts the local solution into a global lower bound for the exact fixed-reflectivity exponent.

**Conceptual connection:** “Global” refers to every transcript and phase for this receiver, not optimization over receiver architectures. A finite nonzero reflectivity still accompanies the large-sample limit.

**Sources:** Anchor context: [pp. 3–4, upper and lower performance bounds and Fig. 3](https://arxiv.org/pdf/1910.12277v4#page=3). Project proof: [finite-reflectivity bound, Eqs. F1–F9](../science/finite_reflectivity.md#1-a-global-finite-reflectivity-lower-bound).

<a id="m27"></a>

### M27 — The arithmetic witness and the numerical diagnostic

**Phase:** Narrative/innovation.

**Central question:** Which conclusions come from proof, certified arithmetic, and numerical minimization?

**Understanding target:** Separate the analytic global bound, its rational-interval evaluation, and a multistart saddle search. Interpret the certified exponent factor above 1.1926 for $n=0.001$, $B=10$, and $0\lt \kappa\le0.1$, with the declared gain and fraction, without converting it into a finite-sample accuracy percentage.

**Dependencies and story role:** Uses [M23](#m23)–[M26](#m26). It supplies an independently inspectable finite-parameter separation and the correct role of the supporting calculations.

**Conceptual connection:** Arithmetic verifies the endpoint inequalities; analytic monotonicity extends the certificate to the interval. A found numerical minimum is corroboration, not a global lower certificate.

**Sources:** Anchor context: [p. 4, Fig. 3](https://arxiv.org/pdf/1910.12277v4#page=4). Project: [finite witness, Eqs. F15–F17](../science/finite_reflectivity.md#22-finite-witness), [exact certificate](../verification/README.md#required-exact-rational-certificate), and [diagnostic scope](../verification/README.md#optional-exact-rate-numerical-diagnostic).

<a id="m28"></a>

### M28 — The all-zero pilot obstruction

**Phase:** Narrative/innovation.

**Central question:** Why can a sublinear pilot budget give zero worst-phase exponent even when all data are retained?

**Understanding target:** Explain how an all-zero record in two positive pilot blocks has centered vector $(-q,-q)$ and always commands phase $-3\pi/4$, and how a single fixed true phase makes the entire main count law equal to the null law. Relate the event's cost to the total pilot count $M_N$, yielding zero per-pair exponent when $M_N=o(N)$.

**Dependencies and story role:** Uses [M10](#m10), [M14](#m14), [M16](#m16), and [M20](#m20). It explains the reliability cost behind a positive pilot fraction, beyond the optimization calculation.

**Conceptual connection:** The obstruction applies to fixed brightness and gain, the declared argument rule, one frozen phase, and one counted OPA output. It neither discards pilot evidence nor establishes a no-go theorem for every adaptive receiver.

**Sources:** Anchor context: [p. 6, phase-matching assumptions](https://arxiv.org/pdf/1910.12277v4#page=6). Project proof: [blind direction](../science/pilot_cost.md#the-exact-blind-direction), [all-zero event](../science/pilot_cost.md#an-event-that-selects-the-blind-setting), and [decision-independent lower bound](../science/pilot_cost.md#a-lower-bound-for-every-final-decision).

<a id="m29"></a>

### M29 — Receiver resources and neighboring architectures

**Phase:** Narrative/innovation.

**Central question:** Which physical requirement does this feedback construction change, and which remain?

**Understanding target:** Distinguish no quantum coherence between different pairs from the retained idler's required round-trip storage. Keep known reflectivity and background, one common phase, ideal counting, a stable local pump, and fixed classical transmission explicit. Identify why two-output counting, continued adaptation, bright pilots, and collective reception can fall outside the obstruction.

**Dependencies and story role:** Integrates [M12](#m12), [M25](#m25), [M27](#m27), and [M28](#m28). It places the mathematical separation within its actual optical and resource model.

**Conceptual connection:** A per-energy detection exponent is distinct from total apparatus energy, time, or practical radar utility. Prior phase-learning architectures and stronger collective receivers remain part of the comparison.

**Sources:** Anchor: [pp. 6–8, receiver assumptions and practical limitations](https://arxiv.org/pdf/1910.12277v4#page=6). Project: [scope table](../science/interpretation.md#what-must-remain-in-the-claim), [calibration scope](../science/pilot_cost.md#what-the-theorem-says-about-calibration), and [neighboring receiver classes](../references/RELATED_WORK.md#fixed-measurements-feedback-and-collective-reception).

<a id="m30"></a>

### M30 — The complete contribution

**Phase:** Narrative/innovation.

**Central question:** What has the full feedback experiment established beyond its individual optical and statistical ingredients?

**Understanding target:** Connect one paid classical phase update, complete-record minimax reliability, the solved leading allocation, a uniform classical comparator, a finite-reflectivity certificate, and the sublinear-pilot obstruction into one claim. State the strict advantage while preserving its receiver, source, phase, energy, and limiting-order assumptions.

**Dependencies and story role:** Integrates [M20](#m20), [M23](#m23), and [M27](#m27)–[M29](#m29), returning to the framework in [M12](#m12). It closes the narrative at the level of the whole scientific result.

**Conceptual connection:** OPA hardware and learning a phase before reception are established ideas. The additional result is the charged, full-transcript reliability law and its demonstrated separation; it does not require a claim of universal adaptive optimality or the full collective illumination advantage.

**Sources:** Anchor: [pp. 3–7, the Gaussian illumination and receiver comparison](https://arxiv.org/pdf/1910.12277v4#page=3). Project synthesis: [scientific dependencies](../science/README.md#the-logical-dependencies), [benchmark and resources](../science/interpretation.md#a-benchmark-favorable-to-classical-illumination), [the additional scientific step](../science/interpretation.md#the-additional-scientific-step), and [related-work account](../references/RELATED_WORK.md).
