# Related work and attribution

This project studies target detection with one unknown return phase that remains fixed across all transmitted pairs. A pairwise optical-parametric-amplifier (OPA) receiver uses some pairs to choose a pump phase and retains the complete pilot and detection record. The question is how that feedback changes the error exponent when every pilot pair is included in the signal-energy budget. The channel, receiver, and resource assumptions are specified in [model.md](../science/model.md).

## OPA receiver

[Tan et al. (2008)](https://doi.org/10.1103/PhysRevLett.101.253601) established Gaussian quantum illumination in a bright thermal background and its comparison with coherent-state illumination. Their coherent-state Chernoff expression is Eq. (11); the discussion around Eq. (19) treats classical signal–idler mixtures and gives the receiver the classical preparation label. These model and comparison ideas are inherited here.

[Guha and Erkmen (2009)](https://doi.org/10.1103/PhysRevA.80.052310) introduced the structured OPA and phase-conjugate receivers and their known-phase advantage. Figure 2 and Eqs. (3)–(6) of the [author manuscript](https://arxiv.org/abs/0911.0950) give the OPA transformation, one-output photon counting, and its performance. The present work uses this established OPA architecture and its thermal photon-count law.

## Learning phase before detection

[Jonsson et al. (2020)](https://doi.org/10.1109/RadarConf2043947.2020.9266597) explicitly propose using `O(√M)` copies to estimate an unknown return phase, followed by detection in the inferred frame using the remaining copies. The relevant passage is Section III.C, immediately after Eq. (13), on p. 4 of the [accepted manuscript](https://acris.aalto.fi/ws/portalfiles/portal/55182705/comparison_between_quantum_and_classical_noise_radar_sources.pdf). This is a direct antecedent of phase learning followed by local **detection**. Its surrounding receiver discussion concerns phase-conjugate reception.

That passage cites [Sanz et al. (2017)](https://doi.org/10.1103/PhysRevLett.118.070803). Their unnumbered type-I/type-II error theorem, on p. 3 of the [author manuscript](https://arxiv.org/abs/1606.06656) near Eq. (4), already establishes small-signal error exponents for a fixed QFI-optimal observable under a stated moment condition. The proof uses a finite moment-generating function and Cramér–Chernoff theory. It is a detection-exponent result, beyond a mean-square-error or central-limit statement. Their parameter `η` is an amplitude; `η²` corresponds to the power reflectivity `κ` used here.

The additional calculation in [error_exponent.md](../science/error_exponent.md) concerns the adaptive record itself: rare pilot outcomes change the setting used for all subsequent counts. The obstruction in [pilot_cost.md](../science/pilot_cost.md) applies to a sublinear pilot stage followed by **one frozen phase and one counted OPA output**. It does not establish the corresponding obstruction for the different phase-conjugate output law considered by Jonsson et al.

[Gong and Bash (2026)](https://doi.org/10.1103/kmnp-11ch) give a closely related two-stage architecture for transmittance **estimation**. Section IV and Fig. 3 of [version 3](https://arxiv.org/html/2402.17922v3) use coherent/heterodyne pilots to estimate phase and transmittance, then apply phase correction, separate two-mode squeezers, and photon counting on both outputs. Theorem 1 establishes consistency and asymptotic normality with the stated quantum-optimal limiting variance. Those estimation asymptotics do not supply the fixed-budget detection exponent of the one-output OPA protocol.

## Fixed measurements, feedback, and collective reception

[Shiraiwa and Kukita (2026)](https://arxiv.org/abs/2608.13997v1) study a common unknown phase with the **same fixed measurement on every copy**. Their Eq. (31) bounds the leading worst-phase exponent by `κ N_S/[4(N_B+1)]`; Appendix A gives an attaining coherent/heterodyne test. A pump setting selected from preceding outcomes lies outside that identical-measurement class. The theorem therefore supplies context for feedback, rather than a bound on every pairwise adaptive receiver.

[Chen and Zhuang (2023)](https://doi.org/10.1103/PhysRevA.107.062405) analyze correlation-to-displacement reception for unknown-phase and fading targets. Sections III–IV of the [author manuscript](https://arxiv.org/abs/2212.08190) retain idlers after return-mode heterodyne measurements and combine them coherently using an outcome-dependent beamsplitter array. That collective concentration is a different receiver resource from the present restriction to quantum operations within individual return–idler pairs.

The broader statistical setting is controlled sensing. [Nitinawarat, Atia, and Veeravalli (2013)](https://doi.org/10.1109/TAC.2013.2261188), especially Sections III and V of the [author manuscript](https://arxiv.org/abs/1205.0858), study fixed-sample error exponents under causal observation control. Their binary result concerns two specified simple hypotheses; their multihypothesis examples show that causal control can help. The continuous unknown-phase alternative here requires its own conditional-likelihood calculation.

## Classical benchmark

[Nair and Gu (2020)](https://doi.org/10.1364/OPTICA.391335), Eq. (6), give the standard classical-illumination exponent. In their notation the reflectivity is a power and `N_S` is total signal energy. With `N` signals of mean energy `n`, the per-pair known-phase coefficient is

$$
\kappa n\bigl(\sqrt{B+1}-\sqrt B\bigr)^2.
$$

[classical_limit.md](../science/classical_limit.md) states the preparation class explicitly as classical mixtures of coherent signals, allowing arbitrary label-conditioned idlers and a total mean signal-energy constraint. It proves a finite-energy error lower bound that is uniform under energy randomization, then gives the receiver both the preparation label and the true phase. Classicality is a condition on the joint preparation, not merely on the signal marginal.

## Testing foundations

The spectral probability distributions used in that converse come from [Nussbaum and Szkoła (2009)](https://doi.org/10.1214/08-AOS593), Section 3 of the [published paper](https://pi.math.cornell.edu/~nussbaum/papers/09-1.pdf). Their main asymptotic theorem is formulated in finite dimension; the proof here explicitly handles the countable thermal spectrum. The matching error **upper** bound uses the trace inequality of [Audenaert et al. (2007)](https://doi.org/10.1103/PhysRevLett.98.160501), Theorem 1 and Eq. (4) of the [author manuscript](https://arxiv.org/abs/quant-ph/0610027). This achievability inequality is distinct from the error lower bound needed for the classical ceiling.

The resulting contribution is a complete-record reliability law for the specified feedback policy, with charged phase pilots and an explicit classical comparison. Finite-reflectivity calculations and their interpretation are recorded in [finite_reflectivity.md](../science/finite_reflectivity.md). Full publication metadata and primary-source links are collected in [references.bib](references.bib).
