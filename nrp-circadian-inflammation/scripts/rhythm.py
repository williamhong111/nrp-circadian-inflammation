"""Fit a 24-hour rhythm to one gene's expression over time.

STUB -- nothing here is implemented yet.

The model
---------
    y(t) = level + amplitude * cos(2*pi*(t - peak) / 24)

    level      the 24-hour average               -> how much
    amplitude  half the peak-to-trough swing     -> how strong the rhythm is
    peak       the time of day of the maximum    -> WHEN

The hint that makes this easy
-----------------------------
"peak" sits inside a cosine, so the model looks non-linear. It is not. Expand

    cos(w*(t - peak)) = cos(w*t)*cos(w*peak) + sin(w*t)*sin(w*peak)

and the model becomes

    y = level + b1*cos(w*t) + b2*sin(w*t)

which is ORDINARY LEAST SQUARES in b1 and b2. Fit those, then convert back to
amplitude and peak. Working out that conversion is part of the exercise -- the two
formulas are a Pythagorean one and an arctangent one. Check the sign carefully,
and check it against data whose answer you already know.

Test it before you trust it
---------------------------
Write `demo()` first. Generate fake genes with a known level, amplitude and peak,
fit them, and confirm the fit recovers the values you put in. If it cannot recover
an answer you already know, nothing it says about real data means anything.
"""

from __future__ import annotations

PERIOD = 24.0


def fit_rhythm(t, y, period: float = PERIOD) -> dict:
    """Fit one gene's daily rhythm.

    Returns a dict with level, amplitude, peak, and some measure of how well it
    fits and whether the rhythm is better than a flat line.
    """
    raise NotImplementedError


def hours_apart(peak_a: float, peak_b: float, period: float = PERIOD) -> float:
    """Shortest distance between two times on a 24-hour clock.

    CT23 and CT1 are 2 hours apart, not 22. Plain subtraction gets this wrong, and
    it is the most common bug in this kind of analysis. Write this one carefully
    and test it on the wrap-around cases.
    """
    raise NotImplementedError


def compare(t_a, y_a, t_b, y_b, period: float = PERIOD) -> dict:
    """Compare one gene's rhythm between two groups.

    Report the difference in level, amplitude and peak, and some test of whether
    the RHYTHM differs rather than just the level.

    A warning worth understanding before writing this: fitting each group
    separately and noting that one is significant and the other is not does NOT
    show that the rhythm changed. The difference between significant and not
    significant is not itself significant. The comparison has to be one test.
    """
    raise NotImplementedError


def demo() -> None:
    """Fit made-up genes with known answers and check they come back.

    Write this BEFORE the real analysis. Suggested cases: a gene whose peak moved,
    one whose rhythm flattened, one whose level rose with the rhythm intact, and
    one that did not change at all. Each should be identified correctly.
    """
    raise NotImplementedError


if __name__ == "__main__":
    raise SystemExit("Not implemented yet. See docs/project-plan.md phase 3.")
