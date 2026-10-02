# External Data Access and Reproducibility

## Storage and redistribution

Store downloaded data and derived loan-level files under data/.
The entire directory is excluded from Git.

Do not commit Freddie Mac files, sampled mortgage records, or
derived loan-level panels. Review the applicable terms before use
or redistribution. Commit download instructions, code, model
coefficients, and permitted aggregate summaries only.

## Freddie Mac mortgage data

Official entry point:
https://www.freddiemac.com/research/datasets/sf-loanlevel-dataset

1. Follow the official access link to Clarity Data Intelligence.
2. Register or sign in and review the applicable terms.
3. Obtain sample files or a documented selection of vintages.
   The selection must support pre-2008 estimation, crisis testing,
   final calibration, and the post-pandemic holdout.
4. Download corresponding origination and monthly performance files.
5. Obtain the user guide, layouts, release notes, and headers that
   match the downloaded release.
6. Save source files and documentation under
   data/development/freddie_mac/.
7. Record actual release coverage separately from the analytical
   performance cutoff of September 30, 2025.

Filtering a newer release to older performance dates does not
convert it into an older file format or historical release vintage.
Older observations may also contain subsequent revisions; record
that limitation rather than claiming a historical real-time dataset.

Field mappings will be documented before parsing. Preserve missing
values and unresolved outcomes. Do not divide Actual Loss directly
by first-default exposure as a substitute for the required
principal-loss mapping and matched-event LGD benchmark.

## National unemployment

Source: BLS, distributed through FRED.
https://fred.stlouisfed.org/series/UNRATE

Save monthly, seasonally adjusted observations under
data/development/macro/.

Calculate quarterly rates as the arithmetic mean of all three
monthly observations. Retain percent units, retrieval date, source
vintage where available, and the original downloaded file.

Synthetic development runs through Q2 2026. The Q3 2026 unemployment
realization of 4.9% is a synthetic project input.

Check downloaded April-June 2026 values against the specification's
frozen reference before generation. Resolve revisions explicitly;
do not silently overwrite approved references or scenario files.

## House price indexes

Official entry point:
https://www.fhfa.gov/data/hpi

Obtain quarterly national and state-level HPI data. Record the exact
index family, seasonal-adjustment convention, series identifiers,
and release before building the panel.

Use a consistent series definition across historical calculations
and benchmark comparisons. State HPI refreshes historical property
values; the base champion uses national HPI growth as its macro
predictor and national scenario paths in projection.

For consecutive quarterly index levels, annualized growth in
percent is:
100 * ((HPI_t / HPI_previous_quarter) ** 4 - 1)

Retain sufficient earlier history to refresh property values from
each selected mortgage's origination date.

## Mortgage market rates

Freddie Mac PMMS series distributed through FRED:
https://fred.stlouisfed.org/series/MORTGAGE30US

Download historical observations and record their original frequency
and units. Define the start-of-quarter alignment rule before joining
the development panel. Convert percent rates to annual decimal rates
for the project's delivered loan and market-rate fields.

Future realized rates must not replace the frozen launch market
mortgage rate in a lifetime forecast.

## Optional regional and stress data

State unemployment is optional for a regional challenger; the base
champion uses national unemployment. Any regional challenger needs
explicit estimation-to-projection mapping.

The optional stress extension requires official Federal Reserve
scenario files, source URLs, retrieval dates, and calendar labels.
It is not a prerequisite for Phase 0 or the core close.

## Acquisition manifest

For every downloaded source, record:

- Source organization and full URL.
- Retrieval date.
- Release identifier and vintage, when available.
- Original filenames and SHA-256 hashes.
- Actual coverage and selected analytical cutoff.
- Units, frequency, seasonal adjustment, and transformations.
- Matching guide/layout version.
- Applicable terms and any unresolved limitations.

Acquisition status: pending.
No external data download has yet been recorded in this document.
