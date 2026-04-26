import numpy as np
import matplotlib.pyplot as plt

# =========================
# Parametros do modelo
# =========================
N0 = 100
a = 0.02
Tmin = 5
T = np.linspace(15, 30, 300)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.patch.set_facecolor('#0f1117')

# =========================
# Grafico 1: N(t) vs Temperatura para diferentes tempos
# =========================
tempos = [2, 5, 10, 20]
colors = ['#4fc3f7', '#29b6f6', '#0288d1', '#01579b']

ax1 = axes[0]
ax1.set_facecolor('#1a1d27')

for t, cor in zip(tempos, colors):
    mu = (a * (T - Tmin))**2
    N = N0 * np.exp(mu * t)
    ax1.plot(T, N, color=cor, linewidth=2.5, label=f't = {t}h')

ax1.set_xlabel("Temperatura da água (°C)", color='white', fontsize=12)
ax1.set_ylabel("N(t) — Quantidade de bactérias", color='white', fontsize=12)
ax1.set_title("Crescimento bacteriano\nN(t) = N₀·e^{[a(T−Tₘᵢₙ)]²·t}", color='white', fontsize=13, pad=12)
ax1.legend(facecolor='#2a2d3a', edgecolor='gray', labelcolor='white', fontsize=11)
ax1.tick_params(colors='white')
ax1.spines[:].set_color('#444')
ax1.grid(True, color='#333', linestyle='--', alpha=0.5)

ax1.axvline(x=28, color='#ff6b6b', linestyle='--', alpha=0.7, linewidth=1.5)
ax1.text(28.2, ax1.get_ylim()[1] * 0.5, 'T = 28°C\n(risco alto)', color='#ff6b6b', fontsize=9)

# =========================
# Grafico 2: mu vs Temperatura (curva de Ratkowsky)
# =========================
ax2 = axes[1]
ax2.set_facecolor('#1a1d27')

mu = (a * (T - Tmin))**2
ax2.plot(T, mu, color='#a78bfa', linewidth=2.5)
ax2.fill_between(T, mu, alpha=0.15, color='#a78bfa')

ax2.set_xlabel("Temperatura da água (°C)", color='white', fontsize=12)
ax2.set_ylabel("μ — Taxa de crescimento", color='white', fontsize=12)
ax2.set_title("Modelo de Ratkowsky\n√μ = a·(T − Tₘᵢₙ)", color='white', fontsize=13, pad=12)
ax2.tick_params(colors='white')
ax2.spines[:].set_color('#444')
ax2.grid(True, color='#333', linestyle='--', alpha=0.5)

plt.tight_layout(pad=3)
plt.savefig('crescimento_bacteriano.png', dpi=150, bbox_inches='tight', facecolor='#0f1117')
plt.show()