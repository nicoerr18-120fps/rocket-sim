massa = 2.5
peso = massa * 9.81
print(f"Il peso è {peso:.2f} N")

for t in range(6):
    quota = 0.5 * 9.81 * t**2
    print(f"t = {t} s, spazio percorso = {quota:.1f} m")
    