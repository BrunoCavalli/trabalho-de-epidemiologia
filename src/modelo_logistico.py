import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# ETAPA 1: Modelo de Ratkowsky (Temperatura)
# ==========================================
# Parâmetros biológicos hipotéticos para uma bactéria costeira típica
T_min = 5.0   # Temperatura mínima teórica onde o crescimento cessa (°C)
b = 0.04      # Coeficiente de inclinação biológica

T_mar = 23.0  # Temperatura da água do mar simulada nesta corrida (°C)

# Fórmula: sqrt(r) = b * (T - T_min) -> r = (b * (T - T_min))^2
r_calculado = (b * (T_mar - T_min)) ** 2
print(f"--- CONFIGURAÇÃO BIOLÓGICA ---")
print(f"Temperatura do Mar: {T_mar}°C")
print(f"Taxa intrínseca de crescimento (r) calculada: {r_calculado:.4f} por hora\n")


# ==========================================
# ETAPA 2: Modelo de Crescimento Logístico
# ==========================================
K = 1_000_000  # Capacidade de carga teórica (10^6 células/mL)
N0 = 1_000     # Concentração inicial (10^3 células/mL)
horas = np.arange(0, 48, 1) # Simulação de 48 horas, medindo de hora em hora

def curva_logistica(t, N0, K, r):
    return K / (1 + ((K - N0) / N0) * np.exp(-r * t))

# Gerar a média teórica perfeita para cada hora
N_teorico = curva_logistica(horas, N0, K, r_calculado)


# ==========================================
# ETAPA 3: Variabilidade com Binomial Negativa
# ==========================================
# Parâmetro de dispersão (phi). 
# Valores baixos (ex: 0.5 a 2) criam muitos "clusters" (alta variabilidade).
# Valores altos (ex: >20) deixam os dados muito perto da média teórica.
phi = 1.5 

def amostrar_binomial_negativa(mu, phi):
    """
    O NumPy usa a parametrização (n, p) para a Binomial Negativa.
    Esta função converte a nossa média (mu) e dispersão (phi) para o padrão do NumPy.
    """
    if mu <= 0:
        return 0
    n = phi
    p = phi / (mu + phi)
    return np.random.negative_binomial(n, p)

# Vamos simular que em cada hora nós fomos lá e coletamos 3 amostras independentes (réplicas)
num_replicas = 3
dados_coleta_real = np.zeros((len(horas), num_replicas))

for i, mu_atual in enumerate(N_teorico):
    for rep in range(num_replicas):
        dados_coleta_real[i, rep] = amostrar_binomial_negativa(mu_atual, phi)


# ==========================================
# ETAPA 4: Visualização dos Resultados
# ==========================================
plt.figure(figsize=(12, 6))

# 1. Linha da capacidade de carga (K)
plt.axhline(y=K, color='red', linestyle='--', alpha=0.7, label=f"Capacidade de Carga (K = {K:,})")

# 2. Linha do crescimento esperado (Determinístico)
plt.plot(horas, N_teorico, color='black', linewidth=2.5, label="Modelo Teórico Perfeito (Média)")

# 3. Pontos das coletas simuladas (Estocástico)
for rep in range(num_replicas):
    plt.scatter(horas, dados_coleta_real[:, rep], alpha=0.5, edgecolors='none',
                label="Amostras de Campo Simuladas" if rep == 0 else "")

# Ajustes do gráfico
plt.title(f"Crescimento Bacteriano Marinho Simulada a {T_mar}°C\n(Ratkowsky + Logístico + Binomial Negativa)", fontsize=12)
plt.xlabel("Tempo (Horas)", fontsize=10)
plt.ylabel("Contagem de Bactérias (células / mL)", fontsize=10)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc="upper left")

plt.tight_layout()
plt.show()