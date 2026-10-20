"""
Metode Bolzano (Bagi Dua) - metode tertutup

Tentukan akar persamaan:
    f(x) = 4x^3 - 15x^2 + 17x - 6 = 0

Selang awal [a, b] = [1.5, 3]
    f(1.5) = -0.75  dan  f(3) = 18  ->  f(a) * f(b) < 0
sehingga di dalam selang tersebut terdapat akar.

Titik tengah selang:
    c = (a + b) / 2
Jika f(a) * f(c) < 0 maka selang baru [a, c], selain itu selang baru [c, b].
Lelaran berhenti jika |a - b| < epsilon1 atau |f(c)| < epsilon2.
"""

EPSILON1 = 0.000001
EPSILON2 = 0.00000001
NMAKS = 100


def f(x):
    return 4 * x ** 3 - 15 * x ** 2 + 17 * x - 6


def bolzano(a, b, epsilon1=EPSILON1, epsilon2=EPSILON2, nmaks=NMAKS):
    if f(a) * f(b) > 0:
        print("f(a) * f(b) > 0, selang tidak mengurung akar.")
        return None

    print(f"{'r':>3} {'a':>11} {'c':>11} {'b':>11} {'f(a)':>11} {'f(c)':>11} "
          f"{'f(b)':>11} {'Selang baru':>12} {'Lebarnya':>11}")
    print("-" * 104)
    for r in range(nmaks):
        c = (a + b) / 2
        fa, fc, fb = f(a), f(c), f(b)
        a_lama, b_lama = a, b
        if fa * fc < 0:
            b = c
            selang = "[a, c]"
        else:
            a = c
            selang = "[c, b]"
        lebar = abs(b - a)
        print(f"{r:>3} {a_lama:>11.6f} {c:>11.6f} {b_lama:>11.6f} {fa:>11.6f} "
              f"{fc:>11.6f} {fb:>11.6f} {selang:>12} {lebar:>11.6f}")
        if lebar < epsilon1 or abs(fc) < epsilon2:
            return c, r + 1

    print(f"Jumlah lelaran melebihi Nmaks = {nmaks}")
    return None


def main():
    a, b = 1.5, 3
    print("f(x) = 4x^3 - 15x^2 + 17x - 6")
    print(f"Selang awal [{a}, {b}]")
    print(f"f({a}) = {f(a):.6f} ,  f({b}) = {f(b):.6f}")
    print(f"epsilon1 = {EPSILON1}\n")

    hasil = bolzano(a, b)

    if hasil is not None:
        akar, n = hasil
        print()
        print(f"Hampiran akar x = {akar:.6f}")
        print(f"f({akar:.6f}) = {f(akar):.6e}")
        print(f"Jumlah lelaran = {n}")


if __name__ == "__main__":
    main()
