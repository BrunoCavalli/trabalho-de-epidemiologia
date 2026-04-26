import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# =========================
# Parametros
# =========================
N0 = 100
a = 0.02
Tmin = 5
t = 5

temperaturas = [15, 20, 25, 30]
colors = ['#4fc3f7', '#a78bfa', '#f9a825', '#ff6b6b']

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.patch.set_facecolor("#afb7cf")
fig.suptitle("Distribuição de Poisson — X ~ Poisson(λ)\nλ = N₀·e^{[a(T−Tₘᵢₙ)]²·t}",
             color='white', fontsize=15, y=0.93)

for ax, T, cor in zip(axes.flat, temperaturas, colors):
    ax.set_facecolor("#e8eaf1")

    mu = (a * (T - Tmin))**2
    lam = N0 * np.exp(mu * t)

    x_min = max(0, int(lam - 4 * np.sqrt(lam)))
    x_max = int(lam + 4 * np.sqrt(lam))
    x = np.arange(x_min, x_max)

    pmf = poisson.pmf(x, lam)

    ax.bar(x, pmf, color=cor, alpha=0.75, width=max(1, (x_max - x_min) / 80))
    ax.axvline(lam, color='white', linestyle='--', linewidth=1.5, alpha=0.8, label=f'λ = {lam:.0f}')

    ax.set_title(f"T = {T}°C", color='white', fontsize=13)
    ax.set_xlabel("Número de bactérias (X)", color='white', fontsize=10)
    ax.set_ylabel("P(X = k)", color='white', fontsize=10)
    ax.tick_params(colors='white')
    ax.spines[:].set_color('#444')
    ax.grid(True, color='#333', linestyle='--', alpha=0.4)
    ax.legend(facecolor='#2a2d3a', edgecolor='gray', labelcolor='white', fontsize=10)

    if T >= 28:
        ax.text(0.05, 0.85, '⚠ Risco alto', transform=ax.transAxes,
                color='#ff6b6b', fontsize=11, fontweight='bold')

plt.tight_layout(pad=3)
plt.savefig('poisson_bacterias.png', dpi=150, bbox_inches='tight', facecolor='#0f1117')
plt.show()