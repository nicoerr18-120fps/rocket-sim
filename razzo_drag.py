import numpy as np
import matplotlib.pyplot as plt

g = 9.81
m = m = 10        # massa (kg)
rho = 1.225      # densità dell'aria (kg/m^3)
Cd = 0.75        # coefficiente di resistenza
A = 0.02        # sezione frontale (m^2)
v0 = 200       # velocità iniziale (m/s)
dt = 0.01        # passo temporale (s)

# Senza aria
t0, y0, v_0 = [0.0], [0.0], v0
while y0[-1] >= 0:
    v_0 = v_0 - g * dt
    y0.append(y0[-1] + v_0 * dt)
    t0.append(t0[-1] + dt)

# Con aria
t1, y1, v1 = [0.0], [0.0], v0
while y1[-1] >= 0:
    drag = 0.5 * rho * Cd * A * v1**2
    a = -g - np.sign(v1) * drag / m
    v1 = v1 + a * dt
    y1.append(y1[-1] + v1 * dt)
    t1.append(t1[-1] + dt)

plt.plot(t0, y0, "--", label="Senza aria")
plt.plot(t1, y1, label="Con aria")
plt.xlabel("Tempo (s)")
plt.ylabel("Quota (m)")
plt.title("Lancio verticale: effetto della resistenza dell'aria")
plt.legend()
plt.grid()
plt.show()

print(f"Quota massima senza aria: {max(y0):.1f} m")
print(f"Quota massima con aria:   {max(y1):.1f} m")
print(f"Tempo di volo senza aria: {t0[-1]:.1f} s")
print(f"Tempo di volo con aria:   {t1[-1]:.1f} s")