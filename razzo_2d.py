import numpy as np
import matplotlib.pyplot as plt

g = 9.81
Cd = 0.5
A = 0.008

m_secca = 2.0
m_prop = 0.5
spinta = 120.0
t_burn = 2.0
dm_dt = m_prop / t_burn

angolo = 45.0                 # angolo di lancio rispetto al suolo (gradi)
theta = np.radians(angolo)
dt = 0.001

t = 0.0
x, y = 0.0, 0.0
vx, vy = 0.0, 0.0
m = m_secca + m_prop
xs, ys = [x], [y]

while True:
    if t < t_burn:
        Fx = spinta * np.cos(theta)
        Fy = spinta * np.sin(theta)
        m = m - dm_dt * dt
    else:
        Fx, Fy = 0.0, 0.0

    rho = 1.225 * np.exp(-y / 8500)
    v = np.hypot(vx, vy)                    # modulo della velocità
    drag_x = -0.5 * rho * Cd * A * v * vx   # drag opposto alla velocità
    drag_y = -0.5 * rho * Cd * A * v * vy

    ax = (Fx + drag_x) / m
    ay = (Fy + drag_y) / m - g

    vx = vx + ax * dt
    vy = vy + ay * dt
    x = x + vx * dt
    y = y + vy * dt
    t = t + dt

    xs.append(x)
    ys.append(y)
    if y < 0:
        break

plt.plot(xs, ys)
plt.xlabel("Distanza (m)")
plt.ylabel("Quota (m)")
plt.title(f"Traiettoria 2D, angolo {angolo}°")
plt.axis("equal")
plt.grid()
plt.savefig("traiettoria_2d.png", dpi=150)
plt.show()

print(f"Quota massima: {max(ys):.1f} m")
print(f"Gittata: {xs[-1]:.1f} m")
print(f"Tempo di volo: {t:.1f} s")

