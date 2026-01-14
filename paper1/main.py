import numpy as np
import matplotlib.pyplot as plt

N = 100
l = 4000
M = 100
d_toBS = 92
E_elec = 50e-9
epsilon_fs = 10e-12
epsilon_mp = 0.0013e-12
E_DA = 5e-9

k_values = np.arange(1, 12, 2)
E_total_values = []

# 根據公式18計算總能耗
for k in k_values:
    E_total = l * (2 * N * E_elec + N * E_DA + k * epsilon_mp * (d_toBS**4) + N * epsilon_fs * (M**2) / (2 * np.pi * k))
    E_total_values.append(E_total * 1e2)

plt.figure(figsize=(10, 7))
plt.plot(k_values, E_total_values, 'k-', marker='*', markersize=8, linewidth=0.8)
plt.xlabel('Number of clusters', fontsize=12)
plt.ylabel('Average energy dissipation per round', fontsize=12)
plt.xlim(1, 11)
plt.xticks(np.arange(1, 12, 1))
plt.tight_layout()
plt.show()