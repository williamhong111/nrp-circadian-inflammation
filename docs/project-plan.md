# Project plan

**Circadian timing of neuroinflammation.** A computational study using public gene
expression data.

> This is a scaffold. Sections marked **[TO FILL]** are for the team to write once the
> dataset decision is made.

## The one-line thesis

Inflammation in the brain is treated as a quantity — how much microglial activation,
how much cytokine — but inflammatory signalling is rhythmic, so a brain can be
abnormal in its inflammatory *timing* as well as its inflammatory *amount*. This
project measures the timing directly and asks whether it moves.

## Why this is answerable without a laboratory

Circadian experiments collect tissue at many times of day, and many of those datasets
are public. The timing information is already in them. The work is reading the data
correctly and fitting a rhythm to it, both of which are computational.

## The method, in three numbers

For each gene, fit a 24-hour cosine to its expression across time:

```
y(t) = level + amplitude * cos(2*pi*(t - peak) / 24)
```

| | meaning | question it answers |
| --- | --- | --- |
| level | the 24-hour average | how much |
| amplitude | half the peak-to-trough swing | how strong the rhythm is |
| peak | the time of day of the maximum | **when** |

Comparing these three between groups separates a change in amount from a change in
timing. That separation is the project.

This is not machine learning. The phase sits inside a cosine, which looks non-linear,
but the model can be rewritten as a linear combination of `cos(wt)` and `sin(wt)`, so
it is ordinary least squares. Working that out is the first real task.

## Research question

**[TO FILL — depends on the dataset.]** Write it as a question that ends in a question
mark, naming what is being compared and what is being measured. See
[`datasets.md`](datasets.md) for what each candidate dataset supports.

A topic is a subject. A question is something that could come out either way.

## What we already know going in

Two 2025 papers addressed versions of the biological question and should be read
before starting, whichever dataset is chosen:

- **Nature Neuroscience 2025** — mouse glia sampled every 2 hours across 24 hours, wild
  type versus an amyloid model. Glial circadian transcriptomes are substantially
  reprogrammed under amyloid pathology.
  <https://www.nature.com/articles/s41593-025-02067-1>
- **Neuron 2025** — human Alzheimer's cortex, with circadian phase inferred
  computationally because post-mortem time of death is unreliable.

Knowing this literature and positioning against it is what makes the work credible.
Writing as though the area were untouched is the fastest way to lose a reader.

**[TO FILL]** — after reading both, write two or three sentences here on what they did
and what they left open.

## Plan

### Phase 1 — Choose the dataset

Open all three accessions in [`datasets.md`](datasets.md). For each, record the sample
count and whether sampling times are present. Pick one. Write down why.

**The disqualifying check:** no recorded time of day means the dataset cannot answer
this question, whatever else it has.

### Phase 2 — Load the data and prove you loaded it right

Download, parse, and get to a table where you know which column is which timepoint and
which condition. **[TO FILL: which files, which format, any surprises.]**

This is the slowest phase and the one most likely to be done wrong silently. Budget
for it.

### Phase 3 — The sanity check

Fit the clock genes before fitting anything else. `Dbp`, `Arntl` (Bmal1) and `Per2`
should cycle strongly in any tissue with a working clock.

**If the clock genes come out flat, the problem is in phase 2, not in the biology.**
Do not go on until they behave. This is the single most useful checkpoint in the
project, because it tests the data handling and the fitting code at once against an
answer that is already known.

### Phase 4 — The analysis

Fit the inflammation gene set. Record level, amplitude and peak for every gene in
every group. Compare.

**[TO FILL: exactly what is being compared.]**

### Phase 5 — Write up

Manuscript, figures, and a repository someone else could run.

## Known traps

Write more here as you hit them.

- **Gene symbol case.** Mouse symbols are Title case (`Il1b`), human are upper case
  (`IL1B`). The wrong case returns nothing and raises no error.
- **Probe IDs are not gene names.** Microarray rows are probes. You must join through
  the platform annotation, and one gene usually has several probes.
- **Time is circular.** CT23 and CT1 are two hours apart, not twenty-two. Never
  subtract two peak times directly.
- **A peak time from a flat gene is meaningless.** Check amplitude before trusting a
  phase — the maximum of a flat line is noise.
- **Multiple testing.** Fitting 20,000 genes at p < 0.05 gives roughly 1,000 false
  positives by chance. Report FDR-corrected q values for any genome-wide scan.
- **[TO FILL]**

## Deliverables

**[TO FILL]**

## Out of scope

No laboratory work, no new data collection, no human subjects. No new analytical
methods — the cosinor model is standard and that is the point.
