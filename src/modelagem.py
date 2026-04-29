import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# =========================
# Parâmetros
# =========================
N0 = 100
a = 0.02
Tmin = 5
t = 20

temperaturas = [15, 20, 25, 30]
# Paleta Soft: Azul Sereno, Verde Chá, Salmão Suave, Vermelho Coral
colors = ['#5dade2', '#58d68d', '#f39c12', '#e74c3c']

# Configuração de Estilo
plt.rcParams.update({'figure.facecolor': '#f8f9fa', 'axes.facecolor': '#ffffff'})

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Distribuição de Poisson — Crescimento Bacteriano\n$\lambda = N_0 \cdot e^{[a(T-T_{min})]^2 \cdot t}$", 
             color='#2c3e50', fontsize=18, y=0.96, fontweight='bold')

for ax, T, cor in zip(axes.flat, temperaturas, colors):
    # Cálculo do Lambda
    mu = (a * (T - Tmin))**2
    lam = N0 * np.exp(mu * t)

    # Intervalo de plotagem
    std = np.sqrt(lam)
    x_min = max(0, int(lam - 4 * std))
    x_max = int(lam + 4 * std)
    x = np.arange(x_min, x_max)

    pmf = poisson.pmf(x, lam)

    # Plot das barras
    bar_width = 1 if (x_max - x_min) < 100 else (x_max - x_min) / 100
    ax.bar(x, pmf, color=cor, alpha=0.7, width=bar_width, label='Probabilidade')
    
    # Linha da média (Lambda)
    ax.axvline(lam, color='#34495e', linestyle='--', linewidth=1.5, alpha=0.5, label=f'λ = {lam:.1f}')

    # Títulos e Eixos
    ax.set_title(f"Temperatura: {T}°C", color='#2c3e50', fontsize=14, fontweight='bold')
    ax.set_xlabel("Nº de bactérias (X)", color='#5d6d7e', fontsize=10)
    ax.set_ylabel("P(X = k)", color='#5d6d7e', fontsize=10)
    
    # Grid e Borda
    ax.grid(True, color='#ecf0f1', linestyle='-', alpha=0.7, zorder=0)
    ax.tick_params(colors='#7f8c8d', labelsize=9)
    for spine in ax.spines.values():
        spine.set_edgecolor('#bdc3c7')

    # Legenda
    ax.legend(facecolor='white', edgecolor='#ecf0f1', fontsize=9, loc='upper right')

    # Alerta de risco
    if T >= 28:
        ax.text(0.95, 0.82, '⚠ RISCO ALTO', transform=ax.transAxes,
                color='#c0392b', fontsize=10, fontweight='bold', 
                ha='right', bbox=dict(facecolor='#fdeaea', edgecolor='#e74c3c', boxstyle='round,pad=0.3'))

plt.tight_layout(rect=[0, 0.03, 1, 0.93])
plt.show()