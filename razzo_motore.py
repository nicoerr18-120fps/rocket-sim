import numpy as np
import matplotlib.pyplot as plt

g = 9.81
rho = 1.225
Cd = 0.5
A = 0.008            # sezione frontale (m^2)

m_secca = 2.0        # massa senza propellente (kg)
m_prop = 0.5         # massa propellente (kg)
spinta = 120.0       # spinta del motore (N)
t_burn = 2.0         # durata della combustione (s)
dm_dt = m_prop / t_burn   # portata di propellente (kg/s)

dt = 0.001
t, y, v, m = [0.0], [0.0], 0.0, m_secca + m_prop
v_list = [0.0]

while True:
    if t[-1] < t_burn:
        F_spinta = spinta
        m = m - dm_dt * dt
    else:
        F_spinta = 0.0

    drag = 0.5 * rho * Cd * A * v**2
    F_tot = F_spinta - m * g - np.sign(v) * drag
    a = F_tot / m

    v = v + a * dt
    y.append(y[-1] + v * dt)
    v_list.append(v)
    t.append(t[-1] + dt)

    if y[-1] < 0:
        break

plt.plot(t, y)
plt.xlabel("Tempo (s)")
plt.ylabel("Quota (m)")
plt.title("Razzo con motore, drag e perdita di massa")
plt.grid()
plt.show()

print(f"Quota massima: {max(y):.1f} m")
print(f"Velocità massima: {max(v_list):.1f} m/s")