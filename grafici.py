import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 100)
y = 0.5 * 9.81 * t**2            # Terra
y_luna = 0.5 * 1.62 * t**2       # Luna
y_marte = 0.5 * 3.71 * t**2      # Marte

g_terra = 9.81 
g_luna = 1.62
plt.plot(t, y, label="Terra")
plt.plot(t, y_luna, label="Luna")
plt.plot(t, y_marte, label="Marte")
plt.xlabel("Tempo (s)")
plt.ylabel("Spazio (m)")
plt.title("Caduta libera: Terra vs Luna")
plt.legend()
plt.grid()
plt.show()