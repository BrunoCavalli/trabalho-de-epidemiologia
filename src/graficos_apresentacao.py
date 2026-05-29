import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
from scipy.stats import poisson, nbinom

# ─────────────────────────────────────────────
# PALETA DE CORES (baseada no tema da apresentação)
# ─────────────────────────────────────────────
TEAL       = "#3d7a7a"
TEAL_DARK  = "#2b5c5c"
TEAL_LIGHT = "#6aabab"
ORANGE     = "#e07b39"
PURPLE     = "#7b5ea7"
GRAY_BG    = "#f4f6f6"
GRAY_GRID  = "#dce3e3"
TEXT_DARK  = "#1a2e2e"

FIG_DPI = 180  # resolução adequada para slides

def estilo_base(ax, titulo, xlabel, ylabel):
    """Aplica o tema do Seaborn e consistência visual para os slides."""
    # Configura o Seaborn com um estilo limpo de fundo
    sns.set_theme(style="whitegrid", rc={
        "axes.facecolor": GRAY_BG,
        "figure.facecolor": "white",
        "grid.color": GRAY_GRID,
        "grid.linestyle": "--",
        "grid.linewidth": 0.8,
        "text.color": TEXT_DARK,
        "axes.labelcolor": TEXT_DARK,
        "xtick.color": TEXT_DARK,
        "ytick.color": TEXT_DARK
    })
    
    # Atualiza títulos e eixos usando os parâmetros do Seaborn/Pyplot
    ax.set_title(titulo, fontsize=13, fontweight="bold", color=TEXT_DARK, pad=12)
    ax.set_xlabel(xlabel, fontsize=10, color=TEXT_DARK)
    ax.set_ylabel(ylabel, fontsize=10, color=TEXT_DARK)
    ax.tick_params(labelsize=9)
    
    # Remove as bordas desnecessárias (efeito sns.despine interno)
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color(GRAY_GRID)
    
    # Legenda customizada
    ax.legend(fontsize=9, framealpha=0.85, facecolor="white", edgecolor=GRAY_GRID)


# ─────────────────────────────────────────────
# PARÂMETROS COMPARTILHADOS
# ─────────────────────────────────────────────
N0    = 100        # concentração inicial (UFC/100 mL)
a     = 0.02       # constante de Ratkowsky
T_min = 5.0        # temperatura mínima de crescimento (°C)

def ratkowsky(T):
    """Taxa de crescimento r via modelo de Ratkowsky."""
    return (a * (T - T_min)) ** 2

def logistico(t, N0, r, K):
    return K / (1 + ((K - N0) / N0) * np.exp(-r * t))

def exponencial(t, N0, r):
    return N0 * np.exp(r * t)


# ══════════════════════════════════════════════════════════════
# GRÁFICO 1 — Logístico vs Exponencial (Slide 13)
# ══════════════════════════════════════════════════════════════
def grafico1_logistico_vs_exponencial():
    T = 28.0
    K = 5000
    r = ratkowsky(T)
    t = np.linspace(0, 30, 300)

    N_exp = exponencial(t, N0, r)
    N_log = logistico(t, N0, r, K)

    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=FIG_DPI)

    # Utilizando o sns.lineplot para renderizar as linhas de tendência
    sns.lineplot(x=t, y=N_exp, color=ORANGE, linewidth=2.2, linestyle="--", label="Exponencial (Malthus)", ax=ax)
    sns.lineplot(x=t, y=N_log, color=TEAL_DARK, linewidth=2.5, label=f"Logístico (Verhulst, K = {K:,})", ax=ax)
    
    ax.axhline(K, color=TEAL_LIGHT, linewidth=1.2, linestyle=":", label=f"Capacidade de suporte K = {K:,}")

    # Anotação do ponto de divergência (~t=10h)
    t_div = 10
    ax.annotate(
        "Divergência:\nmalthus superestima\na partir daqui",
        xy=(t_div, exponencial(t_div, N0, r)),
        xytext=(t_div + 4, exponencial(t_div, N0, r) * 1.8),
        fontsize=8, color=ORANGE,
        arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.2)
    )

    estilo_base(ax,
        titulo=f"Crescimento Bacteriano: Exponencial vs Logístico (T = {T}°C)",
        xlabel="Tempo (horas)",
        ylabel="Concentração bacteriana (UFC/100 mL)"
    )
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))

    plt.tight_layout()
    plt.savefig("grafico1_logistico_vs_exponencial.png", dpi=FIG_DPI, bbox_inches="tight")
    plt.close()
    print("✓ grafico1_logistico_vs_exponencial.png")


# ══════════════════════════════════════════════════════════════
# GRÁFICO 2 — Sensibilidade em K (Slide 14)
# ══════════════════════════════════════════════════════════════
def grafico2_sensibilidade_K():
    T  = 28.0
    r  = ratkowsky(T)
    t  = np.linspace(0, 30, 300)
    Ks = [2000, 5000, 10000]
    cores = [TEAL_LIGHT, TEAL, TEAL_DARK]
    estilos = [":", "--", "-"]

    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=FIG_DPI)

    for K, cor, ls in zip(Ks, cores, estilos):
        N_log = logistico(t, N0, r, K)
        sns.lineplot(x=t, y=N_log, color=cor, linewidth=2.2, linestyle=ls,
                     label=f"K = {K:,} UFC/100 mL", ax=ax)
        ax.axhline(K, color=cor, linewidth=0.8, linestyle=":", alpha=0.5)

    estilo_base(ax,
        titulo=f"Sensibilidade do Modelo Logístico ao Parâmetro K (T = {T}°C)",
        xlabel="Tempo (horas)",
        ylabel="Concentração bacteriana (UFC/100 mL)"
    )
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:,.0f}"))

    ax.axhspan(2000, 10000, alpha=0.06, color=TEAL, label="Faixa literatura (praias tropicais urbanas)")

    plt.tight_layout()
    plt.savefig("grafico2_sensibilidade_K.png", dpi=FIG_DPI, bbox_inches="tight")
    plt.close()
    print("✓ grafico2_sensibilidade_K.png")


# ══════════════════════════════════════════════════════════════
# GRÁFICO 3 — Poisson vs Binomial Negativa (Slide 22)
# ══════════════════════════════════════════════════════════════
def grafico3_poisson_vs_nb():
    mu  = 300          
    phi = 5            
    x = np.arange(0, 700, 1)

    p_poisson = poisson.pmf(x, mu)
    p_nb = nbinom.pmf(x, n=phi, p=phi / (phi + mu))

    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=FIG_DPI)

    # Substituído fill_between/plot por sns.kdeplot simulado ou preenchimento nativo via matplotlib integrado
    ax.fill_between(x, p_poisson, alpha=0.35, color=TEAL, label="Poisson (Var = μ)")
    ax.fill_between(x, p_nb,      alpha=0.35, color=ORANGE, label=f"Binomial Negativa (φ = {phi})")
    
    sns.lineplot(x=x, y=p_poisson, color=TEAL, linewidth=1.8, ax=ax)
    sns.lineplot(x=x, y=p_nb, color=ORANGE, linewidth=1.8, ax=ax)

    limite_epa = 104  
    ax.axvline(limite_epa, color="red", linewidth=1.5, linestyle="--",
               label=f"Limite EPA: {limite_epa} UFC/100 mL")

    ax.annotate(
        "Cauda mais pesada:\nNB captura picos\nde contaminação",
        xy=(450, p_nb[450]),
        xytext=(480, p_nb[450] + 0.0012),
        fontsize=8, color=ORANGE,
        arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.2)
    )

    estilo_base(ax,
        titulo=f"Poisson vs. Binomial Negativa (μ = {mu} UFC/100 mL)",
        xlabel="Contagem bacteriana X (UFC/100 mL)",
        ylabel="P(X = k)"
    )

    plt.tight_layout()
    plt.savefig("grafico3_poisson_vs_nb.png", dpi=FIG_DPI, bbox_inches="tight")
    plt.close()
    print("✓ grafico3_poisson_vs_nb.png")


# ══════════════════════════════════════════════════════════════
# GRÁFICO 4 — P(risco) vs Temperatura: Poisson vs NB (Slide 23)
# ══════════════════════════════════════════════════════════════
def grafico4_risco_temperatura():
    temperaturas = np.linspace(15, 32, 200)
    t_sim        = 3        
    K            = 5000
    limite_epa   = 104      
    phi          = 5

    p_risco_poisson = []
    p_risco_nb      = []

    for T in temperaturas:
        r  = ratkowsky(T)
        mu = logistico(t_sim, N0, r, K)
        p_risco_poisson.append(1 - poisson.cdf(limite_epa, mu))
        p_risco_nb.append(1 - nbinom.cdf(limite_epa, n=phi, p=phi / (phi + mu)))

    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=FIG_DPI)

    sns.lineplot(x=temperaturas, y=p_risco_poisson, color=TEAL, linewidth=2.2, linestyle="--", label="Poisson", ax=ax)
    sns.lineplot(x=temperaturas, y=p_risco_nb, color=ORANGE, linewidth=2.5, label=f"Binomial Negativa (φ = {phi})", ax=ax)

    ax.axvspan(25, 30, alpha=0.08, color=ORANGE, label="Verão RJ (25–30°C)")
    ax.axhline(0.5, color="gray", linewidth=1, linestyle=":", label="P = 0,5 (referência)")

    T_ref = 28.0
    r_ref = ratkowsky(T_ref)
    mu_ref = logistico(t_sim, N0, r_ref, K)
    p_po = 1 - poisson.cdf(limite_epa, mu_ref)
    p_nb = 1 - nbinom.cdf(limite_epa, n=phi, p=phi / (phi + mu_ref))
    
    ax.annotate(
        f"T = 28°C:\nPoisson: {p_po:.2f}\nNB: {p_nb:.2f}",
        xy=(T_ref, (p_po + p_nb) / 2),
        xytext=(T_ref - 8, 0.7),
        fontsize=8.5, color=TEXT_DARK,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=GRAY_GRID),
        arrowprops=dict(arrowstyle="->", color=TEXT_DARK, lw=1.1)
    )

    estilo_base(ax,
        titulo=f"P(X > limite EPA) vs. Temperatura  (t = {t_sim}h, K = {K:,})",
        xlabel="Temperatura da água (°C)",
        ylabel=f"P(X > {limite_epa} UFC/100 mL)"
    )
    ax.set_ylim(0, 1.05)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:.1f}"))

    plt.tight_layout()
    plt.savefig("grafico4_risco_temperatura.png", dpi=FIG_DPI, bbox_inches="tight")
    plt.close()
    print("✓ grafico4_risco_temperatura.png")


# ══════════════════════════════════════════════════════════════
# GRÁFICO 5 — P(risco) vs Temperatura para diferentes K (Slide 24)
# ══════════════════════════════════════════════════════════════
def grafico5_risco_vs_K():
    temperaturas = np.linspace(15, 32, 200)
    t_sim        = 20
    limite_epa   = 104
    phi          = 5
    Ks           = [2000, 5000, 10000]
    cores        = [TEAL_LIGHT, TEAL, TEAL_DARK]
    estilos      = [":", "--", "-"]

    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=FIG_DPI)

    for K, cor, ls in zip(Ks, cores, estilos):
        p_risco = []
        for T in temperaturas:
            r  = ratkowsky(T)
            mu = logistico(t_sim, N0, r, K)
            p_risco.append(1 - nbinom.cdf(limite_epa, n=phi, p=phi / (phi + mu)))
        sns.lineplot(x=temperaturas, y=p_risco, color=cor, linewidth=2.3, linestyle=ls,
                     label=f"K = {K:,} UFC/100 mL", ax=ax)

    ax.axvspan(25, 30, alpha=0.07, color=ORANGE, label="Verão RJ (25–30°C)")
    ax.axhline(0.5, color="gray", linewidth=1.0, linestyle=":", alpha=0.7)

    ax.annotate(
        "K alto → risco cresce\nquase linearmente com T\nnesta faixa",
        xy=(27, 0.6), xytext=(18, 0.75),
        fontsize=8.5, color=TEAL_DARK,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor=GRAY_GRID),
        arrowprops=dict(arrowstyle="->", color=TEAL_DARK, lw=1.1)
    )

    estilo_base(ax,
        titulo=f"P(X > limite EPA) vs. Temperatura por K  (NB, φ = {phi}, t = {t_sim}h)",
        xlabel="Temperatura da água (°C)",
        ylabel=f"P(X > {limite_epa} UFC/100 mL)"
    )
    ax.set_ylim(0, 1.05)
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f"{x:.1f}"))

    plt.tight_layout()
    plt.savefig("grafico5_risco_vs_K.png", dpi=FIG_DPI, bbox_inches="tight")
    plt.close()
    print("grafico5_risco_vs_K.png")


# ──────────────────────────────────────────────
# EXECUÇÃO
# ──────────────────────────────────────────────
if __name__ == "__main__":
    # Garante que as dependências necessárias estejam prontas
    # Requisitos: pip install seaborn matplotlib scipy numpy
    grafico1_logistico_vs_exponencial()
    grafico2_sensibilidade_K()
    grafico3_poisson_vs_nb()
    grafico4_risco_temperatura()
    grafico5_risco_vs_K()
