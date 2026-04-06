import numpy as np
import matplotlib.pyplot as plt

# =========================
# Parâmetros do modelo
# =========================

N0 = 100        # bactérias iniciais
a = 0.02        # constante de Ratkowsky
Tmin = 5        # temperatura mínima
t = 5           # tempo

k = 0.0001      # taxa de infecção (ajustável)
Npessoas = 1000 # número de pessoas na praia

# intervalo de temperatura
T = np.linspace(15, 30, 100)

# =========================
# Modelo bacteriano
# =========================

mu = (a * (T - Tmin))**2
N = N0 * np.exp(mu * t)

# =========================
# Modelo de infecção
# =========================

P = 1 - np.exp(-k * N)        # probabilidade de infecção / modelo dose-response
Casos = P * Npessoas         # número esperado de casos

# =========================
# Gráfico 1: Bactérias
# =========================

plt.figure()
plt.plot(T, N)
plt.xlabel("Temperatura da água (°C)")
plt.ylabel("Quantidade de bactérias")
plt.title("Crescimento bacteriano vs temperatura")
plt.grid()
plt.show()

# =========================
# Gráfico 2: Probabilidade
# =========================

plt.figure()
plt.plot(T, P)
plt.xlabel("Temperatura da água (°C)")
plt.ylabel("Probabilidade de infecção")
plt.title("Probabilidade de infecção vs temperatura")
plt.grid()
plt.show()

# =========================
# Gráfico 3: Casos esperados
# =========================

plt.figure()
plt.plot(T, Casos)
plt.xlabel("Temperatura da água (°C)")
plt.ylabel("Número esperado de casos")
plt.title("Casos esperados vs temperatura")
plt.grid()
plt.show()