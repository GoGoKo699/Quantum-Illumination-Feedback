# Scientific account

[Repository overview](../README.md)

An unknown return phase can defeat a fixed phase-sensitive quantum-illumination receiver. Learning that phase from early measurements introduces its own rare failure events. This account proves that one classical update can retain a strict quantum advantage after charging all of those measurements to the experiment.

## Read the argument

| Question | Authoritative page |
|---|---|
| Which optical state, noise model and receiver are used? | [Model and detection task](model.md) |
| How does the entire adaptive record determine the exponent? | [Transcript and error-exponent theorem](error_exponent.md) |
| Does the advantage hold at a nonzero specified reflectivity? | [Finite-reflectivity certificate](finite_reflectivity.md) |
| How strong is the classical comparator? | [Classical preparation and detection limit](classical_limit.md) |
| Why can a vanishing pilot fraction fail? | [The cost of freezing a learned phase](pilot_cost.md) |
| What changes physically, and what remains assumed? | [Resource interpretation](interpretation.md) |
| Which ingredients are inherited? | [Related work](../references/RELATED_WORK.md) |
| Which calculations can be reproduced? | [Verification](../verification/README.md) |

## The logical dependencies

The exact thermal output gives geometric photon counts. Their negative-binomial sum probabilities give an exact likelihood for the adaptive transcript. Controlling that likelihood at both typical and rare pilot records yields the large-sample minimax exponent. A uniform weak-reflectivity reduction then solves the pilot-allocation problem analytically.

The classical comparison is a separate converse for classical mixtures of coherent signals at a mean-energy budget. Giving the receiver the preparation label and true phase reduces that problem to displaced thermal-state testing. A direct lower bound on the testing error handles arbitrary randomization of the transmitted energy.

Finally, the all-zero pilot event makes one target phase exactly blind for the frozen one-output receiver. This supplies an architecture-specific obstruction to using a sublinear number of fixed-brightness pilots. A positive pilot fraction and a final test that retains all data overcome that obstruction.

These arguments establish the stated receiver capability. Universal adaptive optimality, phase drift, imperfect storage and a laboratory implementation are outside the theorem.
