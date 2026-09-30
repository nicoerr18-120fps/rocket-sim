import numpy as np
import matplotlib.pyplot as plt

g = 9.81
m = 1.0          # massa (kg)
rho = 1.225      # densità dell'aria (kg/m^3)
Cd = 0.75        # coefficiente di resistenza
A = 0.005        # sezione frontale (m^2)
v0 = 100.0
dt = 0.01

t = [0.0]
y = [0.0]
vel = v0

while y[-1] >= 0:
    drag = 0.5 * rho * Cd * A * vel**2
    # il drag si oppone sempre al moto: il segno dipende dalla direzione di vel
    a = -g - np.sign(vel) * drag / m
    vel = vel + a * dt
    y.append(y[-1] + vel * dt)
    t.append(t[-1] + dt)

plt.plot(t, y, label="Con resistenza dell'aria")
plt.xlabel("Tempo (s)")
plt.ylabel("Quota (m)")
plt.title("Lancio verticale con drag")
plt.legend()
plt.grid()
plt.show()
