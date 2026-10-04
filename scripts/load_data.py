"""Load the chosen dataset into an expression table plus sample information.

STUB -- nothing here is implemented yet.

Whichever dataset is chosen, this module has to end up producing two things:

    expression : rows = genes or probes, columns = samples, values = expression
    samples    : one row per sample, with AT MINIMUM a time-of-day column and a
                 group column (organ, genotype, or condition)

Everything downstream assumes those two objects. Getting them right is most of
the work on this project.

Where the time comes from
-------------------------
In GEO series matrix files the time is usually hidden in the sample title or in a
characteristics field, not in a tidy column. For GSE54650 the titles look like
"Adr_CT18" (organ, then circadian time). Other datasets encode it differently --
look at the actual sample titles before writing the parser.

A GEO series matrix file is plain text: metadata lines starting with "!", then the
expression table between "!series_matrix_table_begin" and "!series_matrix_table_end".
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def read_series_matrix(path: str | Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Read a GEO series matrix file.

    Returns (expression, samples). See the module docstring for their shape.
    """
    raise NotImplementedError


def parse_sample_times(samples: pd.DataFrame) -> pd.DataFrame:
    """Add a numeric time-of-day column by parsing the sample titles.

    Look at the real titles first. Anything that does not parse should come out as
    missing, not as a guess, and you should count how many failed before moving on.
    """
    raise NotImplementedError


def subset(expression: pd.DataFrame, samples: pd.DataFrame, group: str):
    """Pull out one group's samples, sorted by time.

    Returns (sub_expression, times) ready to pass to the rhythm fitting.
    """
    raise NotImplementedError


def summarise(expression: pd.DataFrame, samples: pd.DataFrame) -> None:
    """Print what was loaded: how many genes, how many samples, which groups,
    how many timepoints each, how many values are missing.

    Always look at this before analysing anything. Most mistakes on this project
    are visible here and invisible later.
    """
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit("Not implemented yet. See docs/project-plan.md phase 2.")
