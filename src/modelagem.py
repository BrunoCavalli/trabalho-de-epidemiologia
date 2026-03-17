import numpy as np
import matplotlib.pyplot as plt

# =========================
# Parametros do modelo
# =========================

N0 = 100        # quantidade inicial de bacterias
a = 0.02        # constante de Ratkowsky
Tmin = 5        # temperatura minima (°C)
t = 5           # tempo de crescimento

# intervalo de temperatura (°C)
T = np.linspace(15, 30, 100)

# =========================
# Modelo de Ratkowsky
# =========================

mu = (a * (T - Tmin))**2

# modelo exponencial
N = N0 * np.exp(mu * t)

# =========================
# Grafico
# =========================

plt.figure()

plt.plot(T, N)

plt.xlabel("Temperatura da agua (°C)")
plt.ylabel("Quantidade de bacterias")
plt.title("Crescimento bacteriano em funcao da temperatura")

plt.show()