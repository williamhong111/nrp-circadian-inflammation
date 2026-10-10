# Candidate datasets

Three public datasets. Each supports a different version of the question. **Pick one
before writing analysis code.**

Fill in the blanks below as you check each one. The first task of the project is to
open each accession in a browser and record what is actually there.

---

## The one thing that disqualifies a dataset

**Does it record the time of day each sample was collected?**

The question is about *timing*. A dataset where every sample was collected at one time
of day cannot answer it, no matter how many samples it has. Check this first, before
anything else about the dataset matters.

Look for `ZT` or `CT` values in the sample titles or characteristics (ZT = zeitgeber
time, CT = circadian time; both are hours since lights-on).

---

## Option 1 — GSE54650

<https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE54650>

*A circadian gene expression atlas in mammals assayed by microarray.* Mouse, 12 organs,
sampled every 2 hours for 48 hours. Platform GPL6246.

**Confirmed:** 288 samples. Sample titles look like `Adr_CT18` — organ abbreviation
plus circadian time. CT runs past 24 because sampling continued for two days.

**The question this supports:** do inflammatory genes peak at the same time of day in
every organ, or does each organ run inflammation on its own schedule?

**Note:** all healthy wild-type mice. No disease, no circadian disruption. This
establishes what normal timing looks like — which is a prerequisite for the disease
question, but is not itself the disease question.

| | |
| --- | --- |
| Samples | 288 (confirmed) |
| Timepoints | 24 per organ (confirmed) |
| Time variable | yes, in sample titles (confirmed) |
| Download | Series Matrix File — **not** the 1.2 GB `GSE54650_RAW.tar` |
| Checked by | |
| Date checked | |
| Notes | |

---

## Option 2 — GSE261698

<https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE261698>

*A glial circadian gene expression atlas.* Mouse, wild type versus APP/PS1-21 (an
Alzheimer's amyloid model), reported as sampled every 2 hours over 24 hours, with
astrocytes, microglia and bulk cortex profiled separately. Published 2025 in Nature
Neuroscience.

**NOT VERIFIED.** This accession came from the paper's data-availability statement,
not from the GEO page. Confirm it before planning around it.

**The question this supports:** does amyloid pathology change the timing of glial
inflammatory genes — the version closest to what the team originally proposed.

**Note:** the published paper already analysed this data and reported that glial
circadian transcriptomes are substantially reprogrammed under amyloid pathology. Using
it means either reproducing a known result (useful for learning, honest if stated) or
finding a narrower question the paper did not ask. Read the paper before deciding:
<https://www.nature.com/articles/s41593-025-02067-1>

There is also a browsable version of the data, which is the fastest way to get a feel
for it: <https://musieklab.shinyapps.io/Glial_Circadian_Translatome/>

| | |
| --- | --- |
| Samples | 165, confirmed |
| Timepoints | reported as 12, confirm |
| Time variable | in CT, graph shows 0-24 |
| Download |  |
| Checked by | |
| Date checked | |
| Notes | |

---

## Option 3 — GSE140345

<https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE140345>

*Sleep-wake driven and circadian contributions to daily rhythms in gene expression and
chromatin accessibility in the murine cortex.* Mouse cortex, 24-hour baseline followed
by sleep deprivation and recovery.

**NOT VERIFIED.** Confirm before planning around it.

**The question this supports:** does sleep loss — a circadian disruption that does not
require a disease model — shift the timing of inflammatory genes in the brain?

**Note:** this separates circadian drive from sleep-wake drive by design, which is
exactly the confound that makes the disease version of this question hard. It may be
the most tractable route to a real finding.

| | |
| --- | --- |
| Samples | 123, confirmed |
| Timepoints | measured after 3 and 6 hours, |
| Time variable | ZT |
| Download | ? |
| Checked by | |
| Date checked | |
| Notes | |

---

## Other candidates, unchecked

Only look at these if none of the three above works out.

| Accession | What it is | Why it might help |
| --- | --- | --- |
| GSE23628 | Sleep deprivation across 7 mouse brain regions, including the SCN | Regional comparison within the brain |
| GSE151565 | Circadian expression in mouse striatum, cortex, hypothalamus; 13 timepoints | Another healthy baseline, brain-focused |
| GSE154665 | Astrocyte *Bmal1* deletion, cortex | Clock knocked out in one glial cell type |
| GSE293026 | REV-ERB knockout, astrocyte reactivity, alpha-synuclein model | Clock knockout plus a disease model |

None verified. Same rule: check the time variable first.

---

## Recording the decision

Once the team picks one, write here:

- **Dataset chosen:**
- **Why, in two sentences:**
- **The question, written as a question:**
- **Date decided:**

Then stop reopening it.
