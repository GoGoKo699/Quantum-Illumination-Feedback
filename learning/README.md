# Learning the phase-feedback result

[Repository overview](../README.md) · [Scientific account](../science/README.md) · [Verification](../verification/README.md)

The physical question is whether a receiver can learn an unknown target phase from early measurements and still gain an exponential detection advantage after paying for those measurements. The learning route connects the optical correlation, the photon-count record, and the rare phase-learning failures that determine the answer.

## One educational anchor

**Jeffrey H. Shapiro, *The Quantum Illumination Story*, IEEE Aerospace and Electronic Systems Magazine 35(4), 8–20 (2020).** The reading version is [arXiv:1910.12277v4](https://arxiv.org/abs/1910.12277v4), revised **23 December 2019**; [full PDF](https://arxiv.org/pdf/1910.12277v4). The article's publication year is 2020, while the selected author-manuscript revision is from 2019.

The [source-to-project bridge](bridge.md) starts with the review's Gaussian-state discussion and OPA receiver, translates notation, and supplies the additional reasoning needed for paid phase feedback. Its source pointers identify the relevant passages; reading the entire review is unnecessary for this route. Research citations supporting the proofs remain in [related work](../references/RELATED_WORK.md).

## Direct routes

| Aim | Route |
|---|---|
| Understand the physical mechanism | [Bridge: signal, idler, and return](bridge.md#one-signal-one-retained-idler-one-returned-mode) → [OPA counts](bridge.md#the-opa-turns-a-correlation-into-counts) |
| See one complete measurement record | [Worked count example](bridge.md#a-worked-count-record) |
| Understand the calibration cost | [Typical accuracy and rare errors](bridge.md#why-typical-phase-accuracy-does-not-determine-the-exponent) → [exact pilot obstruction](../science/pilot_cost.md) |
| Follow the complete conceptual map | [M01–M12: background](milestones.md#m01) → [M13–M30: project narrative](milestones.md#m13) |
| Inspect the exact detection theorem | [Model](../science/model.md) → [transcript and exponent proof](../science/error_exponent.md) |
| Check the strict classical comparison | [Classical ceiling](../science/classical_limit.md) → [finite-reflectivity bound](../science/finite_reflectivity.md) → [reproduction commands](../verification/README.md) |

## Why the map has 12 background and 18 narrative milestones

The [30-milestone map](milestones.md) describes the project's conceptual dependencies. Its first **12 milestones** build from a photon mode and its state to the complete illumination problem: thermal and coherent light, signal–idler correlations, matched noise, OPA counting, phase sensitivity, fair energy comparison, minimax detection, and rare-event costs. [M12](milestones.md#m12) combines these into one physical and statistical framework.

The following **18 milestones** develop the contribution from local pieces to its overall consequence. [M13](milestones.md#m13) begins with the charged pilot budget. The route then builds the feedback rule and exact conditional likelihood, handles the pilot-origin singularity and count tails, derives the exponent and allocation law, and establishes the classical and finite-reflectivity comparisons. The final steps connect the all-zero-pilot obstruction to the receiver's resource assumptions. [M30](milestones.md#m30) brings the achieved advantage, its assumptions, and its measurement scope together.

The bridge is a connected explanation of that story. The milestone map supplies stable understanding targets and dependencies; the topic pages under `science/` retain the complete statements and proofs.
