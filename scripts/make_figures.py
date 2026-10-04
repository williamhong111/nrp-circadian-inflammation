"""Figures.

STUB -- nothing here is implemented yet.

Every number that goes in the write-up needs a plot behind it. A fitted phase with
no picture of the underlying time course is not a result, it is a number that
might be a bug.

Figures this project is likely to need
--------------------------------------
1. One gene's time course with the fitted cosine drawn over it. Start here. Do it
   for Dbp first -- if that does not look like a clean 24-hour wave, stop and fix
   the data loading before doing anything else.

2. The clock-gene panel: several clock genes, one small plot each, as the
   sanity-check figure.

3. Peak times on a 24-hour circle. Time is circular, so a normal axis misleads --
   a polar plot puts CT23 next to CT1 where it belongs.

4. The comparison figure: whatever the chosen question is, the one plot that
   answers it.

Keep the styling plain. Readable beats decorated.
"""

from __future__ import annotations


def plot_gene(t, y, fit=None, title: str = "", ax=None):
    """Plot one gene's expression against time, with the fitted cosine over it."""
    raise NotImplementedError


def plot_clock_panel(expression, times, genes=None):
    """Small-multiples panel of the clock genes. The sanity-check figure."""
    raise NotImplementedError


def plot_phase_circle(peaks, labels=None):
    """Peak times on a 24-hour polar plot."""
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit("Not implemented yet. See docs/project-plan.md phase 4.")
