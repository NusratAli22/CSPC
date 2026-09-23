"""
Tests for the decay simulation.

One complete test is given as a model. Add the two tests described in the
lab handout (a negative-rate test, and a test against the analytical law).
Run with:  pytest -v
"""

import numpy as np
import pytest
from decay import simulate, simulate_loop


def test_starts_at_N0():
    # at time zero, no atoms have decayed yet
    assert simulate(1000, 0.4)[0] == 1000


# TODO 1: test_rejects_negative_rate
def test_rejects_negative_rate():
    """Check that calling simulate(...) with a negative lam raises a ValueError."""
    with pytest.raises(ValueError):
        simulate(N0=1000, lam=-0.4)


# TODO 2: test_matches_law
def test_matches_law():
    """
    Check that the simulation's AVERAGE over many seeds is close to the
    physical law  N0 * exp(-lam * t).
    """
    N0 = 100000
    lam = 0.05
    dt = 0.05
    steps = 200
    t = steps * dt  # total time t = 10.0 seconds

    # Calculate average final count across multiple seeds
    final_counts = [simulate(N0=N0, lam=lam, dt=dt, steps=steps, seed=s)[-1] for s in range(10)]
    avg_final = np.mean(final_counts)

    # Physical analytical law: N0 * exp(-lam * t)
    expected = N0 * np.exp(-lam * t)

    # Compare floating-point values using pytest.approx
    assert avg_final == pytest.approx(expected, rel=0.01)