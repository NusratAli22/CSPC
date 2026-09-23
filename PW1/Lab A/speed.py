import time
from decay import simulate, simulate_loop

N0 = 200000
lam = 0.4
dt = 0.05
steps = 200

# Time the pure-Python loop version
t0 = time.perf_counter()
simulate_loop(N0=N0, lam=lam, dt=dt, steps=steps)
t_loop = time.perf_counter() - t0

# Time the NumPy vectorized version
t0 = time.perf_counter()
simulate(N0=N0, lam=lam, dt=dt, steps=steps)
t_numpy = time.perf_counter() - t0

# Calculate and print speed-up factor
speedup = t_loop / t_numpy

print(f"Pure-Python loop time: {t_loop:.4f} s")
print(f"NumPy vectorized time: {t_numpy:.4f} s")
print(f"Speed-up factor: {speedup:.2f}x faster")