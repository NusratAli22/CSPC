# CSPC — Computer Science for Physics and Chemistry

My coursework repository. Each practical is under PW<n>/Lab <X>/.

## Setup
Create the environment for a given lab:
```bash
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc

What I built:
Set up the cspc Conda environment, built the CSPC repository structure, tracked simulation files, implemented automated unit tests, and benchmarked loop vs NumPy execution speed.

Speed comparison (loop vs NumPy):

loop: 2.5823 s

numpy: 0.0003 s

speed-up: 9734.41x faster

Tests: all passing? yes

Conclusion:
Successfully established a reproducible development workflow using Conda, Git, and pytest. Vectorizing the decay simulation using NumPy achieved a ~9734x performance improvement over the pure-Python loop. Unit testing verified proper exception handling for negative rates and confirmed agreement with the physical exponential decay law.

## PW1 — Lab B

**Data:** the observed counts start at 5000 at t = 0 and fall steadily to about 1500 at t = 4, a smooth exponential-looking decay with a little noise.

**Comparison with the analytical law:** with λ = 0.3 and N0 = 5000, the observed points match the curve N0·e^(−λt) closely. For example, at t = 4 the observed count is 1512 and the law gives about 1506. The small differences look like random noise, so the data agree with the analytical law.

**Pipeline:** a Snakemake rule rebuilds `figure.png` from `decay_observed.csv` by running `plot.py`, and only reruns when its input is newer than the figure.