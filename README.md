# Simulated Quarter-End Credit Loss Close

This project is being built as a simulated quarter-end credit loss
close using a synthetic portfolio, with a mortgage PD model to be
estimated on public Freddie Mac loan-level data.

The exercise compares June 30, 2026 with September 30, 2026.
Planned outputs include lifetime expected-loss estimates, separate
funded and eligible unfunded reserves, a sequential reserve walk,
an allowance rollforward, backtesting, and a reporting package.

## Current status

The Phase 0 setup checks pass, including the local PostgreSQL
connection test. Analyst assumptions and generator configuration
remain provisional. Detailed generator parameters and base workout
profiles are pending development. Model development and the reserve
engine are not implemented.

Passing setup tests does not constitute model validation or
approval of the credit loss assumptions.

## Data and interpretation

- Loan portfolios, close events, scenario paths, and close results
  are synthetic, except explicitly identified public calibration
  references.
- Mortgage model development will use Freddie Mac loan-level data
  and public macroeconomic history.
- Other segments will use synthetic development histories driven
  by real national unemployment history.
- Synthetic segments are correctly specified by construction.
  Their validation mainly demonstrates estimation and workflow
  mechanics; it does not establish real-bank model adequacy.
- This project does not reproduce PNC's or the Federal Reserve's
  models and does not estimate PNC's allowance.
- Selected PNC disclosures inform calibration anchors only.
  Undisclosed scenario paths and weights are project constructions.
- The synthetic Q3 unemployment realization of 4.9% is not an
  actual BLS observation.
- Official stress-scenario values must come from the Federal Reserve.
  Any substituted project scenario must be clearly labeled.
- The builder must understand and be able to explain every modeling
  choice and implementation component independently.

## Data handling

The entire data/ directory is excluded from Git. Freddie Mac files
and derived loan-level records must never be committed.

Review the applicable data terms before downloading or distributing
any external data. Code, documented assumptions, coefficient files,
and permitted aggregate summaries are the intended repository contents.

## Architecture

Model development in src/dev/ is separate from the close workflow.

The generator uses config/generator.yaml. The close must never
read that file or any private future realized generator schedules.

The future reserve engine will be a pure function. Its caller will
supply portfolios, as-of workout cases, scenarios, weights, approved
assumptions, and approved PD models.

PostgreSQL runs locally in Docker. SQL will support loading,
validation, reconciliation, and aggregation. No cloud database
is required.

## Local setup

Run commands from the repository root.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Create .env from .env.example and replace the placeholder password.
Never commit .env. Start Docker Desktop, then run:

```bash
docker compose up -d --wait --wait-timeout 60
docker compose ps
```

The example host port is 5433. Settings in .env control the actual port.

## Tests

Tests that do not require PostgreSQL:

```bash
python -m pytest -q
```

Database tests, after PostgreSQL is healthy:

```bash
python -m pytest -q -m database
```

All tests, including database tests:

```bash
python -m pytest -q -m ""
```

## Methodology and reporting

To be completed as the implementation is developed.

The planned sequential walk uses A, X, E, M, N, S, W, Q:
eight contributions from nine reserve runs. Attribution depends
on ordering and is not causal. Shapley attribution is deferred.

## Assumptions and limitations

All configurations currently remain provisional. Null settings
identify unresolved decisions; they must not silently become zero.

Initial numerical tolerances and payment-rate sensitivities are
documented in docs/assumption_review.md.

Pending work includes mortgage severity benchmarking, historical
reversion assessment, base workout profiles, generator parameters,
card group-mix sensitivities, and model estimation.

## Data access and sources

Download instructions are documented in docs/data_access.md.
The acquisition manifest will be populated during Phase 1A.

Official starting points:

- Freddie Mac loan-level data:
  https://www.freddiemac.com/research/datasets/sf-loanlevel-dataset
- National unemployment:
  https://fred.stlouisfed.org/series/UNRATE
- FHFA house price indexes:
  https://www.fhfa.gov/data/hpi
- Freddie Mac mortgage rates through FRED:
  https://fred.stlouisfed.org/series/MORTGAGE30US
