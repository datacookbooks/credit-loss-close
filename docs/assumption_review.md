# Assumption Review

Status: Phase 0 configuration; credit models and base workout profiles
are not yet approved.

## Numerical and accounting conventions

The builder selected the revised settings on October 2, 2026.

Generated monetary fields use whole cents. Currency CSV fields are
represented in USD with exactly two decimal places and parsed using
decimal arithmetic before conversion to integer cents.

Generator closing balances are derived from rounded event flows.
Independent rounding of opening balances, flows, and closing
balances must not create unexplained reconciliation differences.

Principal reconciliation requires exactly zero cents at loan,
workout-case, segment, and portfolio levels.

Reserve computations retain unrounded engine values. Currency
exports are rounded after validation. Reserve reconciliation allows
$0.01 per reported component. Presentation rounding is excluded
from validation; rounded table footing must be explained.

These are project choices, not regulatory thresholds.

## Numerical tolerances

- Transition-row and state-vector sums: absolute tolerance 1e-10.
- Scenario weight sum: absolute tolerance 1e-8; individual weights
  remain in [0, 1] and substantive errors are never normalized away.
- Pure recentering: absolute probability tolerance 1e-10.
- Q2 scenario-anchor comparison: 0.1 percentage point.
- Card omitted-loss bound: larger of $1 and 1% of accumulated EL,
  assessed for each scenario and the weighted result.
- Card checkpoints: 20, 40, and 60 quarters, then extend as needed.
- Card runtime guard: 400 quarters; unmet tail tolerance is failure,
  never a payoff or permission to discard remaining exposure.

## Sensitivity cases

Commercial revolver CCF: 25%, 50%, and 75%.

LGD: 80%, 100%, and 120% of base, capped at 100% LGD. Report the
values actually used after capping.

Once a reliable matched-event mortgage benchmark exists, replace
the provisional mortgage high multiplier with severity for first
defaults during 2008-2011. Preserve target-population, principal-loss,
recovery-rights, follow-up, and censoring consistency. Assess how
this applies to any selected conditional LGD model. Do not force
the empirical result above base or use liquidations alone.

Card payments: 75%, 100%, and 125% of each group's base rate.
Group-mix sensitivities remain pending.

Workout timing: shift collection, confirmed-writeoff, and recovery
lags two quarters earlier or later, preserving lifetime totals,
event chronology, and observed as-of facts.

## Reserve-impact review

Reporting threshold: larger of $1,000 and 1% of the absolute
reference reserve.

Investigation threshold: larger of $5,000 and 5% of the absolute
reference reserve, together with a 90% sampling interval for the
difference that excludes zero.

Apply these to documented, matching comparison scopes, including
funded and unfunded components separately. If sampling evidence
is unavailable or unreliable, retain an unresolved review item.
Statistical uncertainty does not override accounting errors,
conceptual defects, data leakage, or missing-case controls.

Below-threshold results remain available in the benchmark tables.
Thresholds govern reporting emphasis and investigation, not data
deletion or automatic model approval.

## Pending development decisions

- Mortgage matched-event LGD benchmark and model selection.
- Historical reversion targets and comparable-outcome benchmark.
- Base workout timing, recovery shares, and fallback coverage.
- Generator severity distribution and transition parameters.
- Card group shares and group-mix sensitivity.
- Mortgage launch market rate and model perturbations.
- Empirical validation and engine-based reserve sensitivities.
