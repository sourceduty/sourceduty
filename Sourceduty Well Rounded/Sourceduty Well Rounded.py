import matplotlib.pyplot as plt
import numpy as np

domains = ["Mathematics", "Physics", "Chemistry", "Biology", "Environmental Science",
           "Astronomy", "Computer Science", "Engineering", "Theoretical (New_Science)"]
coverage = [0.15, 0.12, 0.10, 0.10, 0.10, 0.10, 0.18, 0.10, 0.15]

N = len(domains)
theta = np.linspace(0.0, 2*np.pi, N, endpoint=False)
width = (2*np.pi)/N * np.ones(N)
colors = plt.cm.Set3(np.linspace(0, 1, N))

fig, ax = plt.subplots(figsize=(14,7), subplot_kw=dict(polar=True))
bars = ax.bar(theta, coverage, width=width, bottom=0.0, color=colors, edgecolor='black')

ax.set_title("Sourceduty Science Knowledge Coverage", va='bottom', fontsize=16, pad=30)
ax.set_xticklabels([])
ax.set_yticklabels([])

legend_labels = [f"{d} ({int(c*100)}%)" for d,c in zip(domains, coverage)]
ax.legend(bars, legend_labels, loc='upper center',
          bbox_to_anchor=(0.5,-0.1), ncol=3, fontsize=9, frameon=False)

plt.tight_layout()
plt.show()
