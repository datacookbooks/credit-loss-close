"""Initial configuration checks; these do not approve the credit models."""

from pathlib import Path

import pytest
import yaml


@pytest.fixture
def assumptions():
    root = Path(__file__).resolve().parents[1]
    with (root / "config" / "assumptions.yaml").open() as file:
        config = yaml.safe_load(file)

    assert isinstance(config, dict)
    return config


def test_documented_scenario_weights_are_valid(assumptions):
    expected = {"upside", "baseline", "downside", "severe"}
    for weights in assumptions["scenario_weights"].values():
        assert set(weights) == expected
        assert all(0 <= weight <= 1 for weight in weights.values())
        assert sum(weights.values()) == pytest.approx(1.0)


def test_card_runoff_and_tail_conventions(assumptions):
    cards = assumptions["cards"]
    rates = cards["quarterly_principal_payment_rates"]

    assert set(rates) == {"slow", "intermediate", "fast"}
    assert 0 < rates["slow"] < rates["intermediate"] < rates["fast"] < 1
    assert cards["imposed_maturity"] is False
    assert cards["future_purchases_or_redraws"] is False

    tail = cards["numerical_tail"]
    assert tail["relative_loss_tolerance"] > 0
    assert tail["absolute_loss_tolerance_usd"] > 0
    assert tail["transfer_residual_mass_to_paid_off"] is False
    assert tail["fail_if_runtime_limit_reached_without_tail_pass"] is True


def test_reserve_routing_and_qualitative_scope(assumptions):
    methodology = assumptions["methodology"]

    assert methodology["existing_cases_receive_new_pd_charge"] is False
    assert methodology["allow_negative_existing_case_acl"] is True
    assert methodology["qualitative_base"] == (
        "pre_default_modeled_reserve_only"
    )
    assert set(methodology["qualitative_components"]) == {
        "funded", "unfunded"
    }
    assert assumptions["workouts"][
        "future_realized_generator_schedules_allowed"
    ] is False


def test_principal_loss_assumptions_are_bounded(assumptions):
    lgds = assumptions["lgd"]["segment_constants"]
    assert all(0 <= value <= 1 for value in lgds.values())
    assert 0 <= assumptions["ccf"]["commercial_revolver"] <= 1
