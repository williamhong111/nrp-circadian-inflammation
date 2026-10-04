"""Gene sets, and mapping probe IDs to gene symbols.

STUB -- the gene lists are filled in, the mapping functions are not.

Why mapping is needed
---------------------
Microarray data has probe IDs as rows:

    probe       GSM1320990   GSM1320991
    10344614    7.23         7.41

Nobody knows what probe 10344614 is. The platform annotation file maps probes to
genes, and for Affymetrix arrays the symbol is buried in a messy string:

    NM_011580 // Il1b // interleukin 1 beta // 2 F // 16176 /// ...

Groups are separated by ///, fields within a group by //, and the symbol is the
second field. One probe can map to several genes and one gene to several probes,
so decide what to do about both before you start.

The platform annotation for GSE54650 is at
https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL6246 (scroll to the bottom).

RNA-seq datasets may already use gene symbols, in which case none of this is needed.
Check the data first.
"""

from __future__ import annotations

import pandas as pd

# Mouse gene symbols are Title case: Il1b, not IL1B. The wrong case matches
# nothing and raises no error. This is the most common early mistake here.

CLOCK_GENES = [
    "Arntl",   # also written Bmal1 -- the annotation may use either name
    "Clock",
    "Per1",
    "Per2",
    "Per3",
    "Cry1",
    "Cry2",
    "Nr1d1",   # Rev-erb alpha
    "Nr1d2",
    "Dbp",     # the strongest rhythm of the lot, and the best sanity check
]

INFLAMMATION_GENES = [
    # Cytokines
    "Il1b",
    "Tnf",
    "Il6",
    "Il10",
    # Complement
    "C1qa",
    "C1qb",
    "C3",
    # Microglia and macrophage identity and activation
    "Aif1",     # Iba1
    "Cd68",
    "Tmem119",
    "P2ry12",
    "Trem2",
    "Cx3cr1",
    # General immune signalling
    "Nfkb1",
    "Tlr4",
    "Ccl2",
]

GENE_SETS = {
    "clock": CLOCK_GENES,
    "inflammation": INFLAMMATION_GENES,
}

# Add or remove genes as the project narrows, but decide the list BEFORE looking
# at which ones turn out to be rhythmic. Picking the gene set after seeing the
# results is how a real finding turns into a false one.


def parse_gene_assignment(value) -> list[str]:
    """Pull gene symbols out of one messy annotation string.

    >>> parse_gene_assignment("NM_011580 // Il1b // interleukin 1 beta // 2 F // 16176")
    ['Il1b']

    Many probes map to nothing ("---" or blank). That is expected, not an error.
    """
    raise NotImplementedError


def read_annotation(path) -> pd.DataFrame:
    """Read a platform annotation file into a probe -> symbol table.

    GEO annotation files start with comment lines beginning '#'.
    """
    raise NotImplementedError


def collapse_to_genes(expression: pd.DataFrame, mapping: pd.DataFrame, symbols=None):
    """Turn a probe-level matrix into a gene-level one.

    Several probes often measure the same gene. Decide how to combine them --
    averaging is the usual choice, taking the probe with the highest mean is the
    other -- and say which you chose in the write-up, because it can change which
    genes come out rhythmic.
    """
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit("Not implemented yet. See docs/project-plan.md phase 2.")
