# Circadian Timing of Neuroinflammation — NRP

When inflammation happens, not just how much of it there is.

Neuroinflammation is almost always measured as an amount: more microglial activation,
more cytokine, worse disease. But inflammatory signalling in a healthy brain is
rhythmic — it rises and falls on a daily cycle driven by the circadian clock, and the
same immune challenge produces a different response depending on the time of day it
arrives. If that is true, a brain can be abnormal in two separate ways: the amount can
be wrong, or the timing can be wrong. A study that samples tissue once cannot tell
those apart.

This project asks whether the timing is a real, measurable thing in public gene
expression data. It is a computational study: the team picks a public dataset, fits a
daily rhythm to each gene, and compares the timing of inflammatory genes between
conditions or tissues. No laboratory, no new data collection. See
[`docs/project-plan.md`](docs/project-plan.md) for the full plan.

## Status

Early. This is a placeholder scaffold. Nothing here is finished — the scripts are
stubs, and the structure below will change once the team decides which dataset to use.

## First decision: which dataset

Three candidates are described in [`docs/datasets.md`](docs/datasets.md). They lead to
three different versions of the question, and the team picks one before writing any
analysis code:

- **GSE54650** — healthy mice, 12 organs, 24 timepoints each. Asks whether
  inflammatory genes peak at the same time of day in every organ.
- **GSE261698** — mouse glia, wild type versus an Alzheimer's model, around the clock.
  Asks whether disease shifts the timing of glial inflammatory genes.
- **GSE140345** — mouse cortex, sleep deprivation and recovery. Asks whether losing
  sleep moves inflammatory timing.

Only the first has been confirmed on its GEO page. **Checking the other two is the
first task** — open each accession, confirm it exists, and record in
`docs/datasets.md` how many samples it has and whether sampling times are recorded.
A dataset with no time variable cannot answer any version of this question, however
large it is.

## Three numbers

Whichever dataset wins, the method is the same. For each gene, fit

```
y(t) = level + amplitude * cos(2*pi*(t - peak) / 24)
```

| | meaning | question |
| --- | --- | --- |
| level | 24-hour average | how much |
| amplitude | size of the daily swing | how strong the rhythm is |
| peak | time of day of the maximum | **when** |

Comparing those three between groups separates a change in amount from a change in
timing, which is the entire point of the project.

## Repository structure

```
docs/         Project plan, dataset notes, meeting notes
data/         Downloaded data (gitignored, not redistributed)
scripts/      Analysis code (currently stubs)
notebooks/    Exploratory work
results/      Fitted parameters, tables
figures/      Plots
```

## Getting started

```bash
pip install -r requirements.txt
```

Then read [`docs/project-plan.md`](docs/project-plan.md) and
[`docs/datasets.md`](docs/datasets.md), and start with the dataset decision.

## Data and licensing

Datasets are downloaded into `data/` (gitignored). This repository points to them, it
does not redistribute them. All three candidates are public and free, with no
application or account required — check each one's terms before any reuse beyond this
project.
