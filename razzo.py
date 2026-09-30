import numpy as np
import matplotlib.pyplot as plt

g = 9.81        # accelerazione di gravità (m/s^2)
v0 = 100.0      # velocità iniziale (m/s)
dt = 0.001    # passo temporale (s)

t = [0.0]       # lista dei tempi
y = [0.0]       # lista delle quote
vel = v0

while y[-1] >= 0:
    vel = vel - g * dt                 # aggiorna la velocità
    y.append(y[-1] + vel * dt)         # aggiorna la posizione
    t.append(t[-1] + dt)               # avanza il tempo

t = np.array(t)
y = np.array(y)
y_analitica = v0 * t - 0.5 * g * t**2  # soluzione esatta

plt.plot(t, y, label="Numerica (Eulero)")
plt.plot(t, y_analitica, "--", label="Analitica")
plt.xlabel("Tempo (s)")
plt.ylabel("Quota (m)")
plt.title("Lancio verticale")
plt.legend()
plt.grid()
plt.show()
