"""
Metode Regula-Falsi (Posisi Palsu) - metode tertutup

Tentukan akar persamaan:
    f(x) = 4x^3 - 15x^2 + 17x - 6 = 0

Selang awal [a, b] = [1.5, 3]  (sama dengan metode Bolzano)

Titik potong garis yang menghubungkan (a, f(a)) dan (b, f(b)) dengan sumbu-x:
    c = b - f(b)(b - a) / (f(b) - f(a))

Pada regula-falsi salah satu ujung selang bisa tidak pernah bergeser,
sehingga lebar selang |a - b| belum tentu mengecil ke nol. Karena itu
lelaran dihentikan jika |c_baru - c_lama| < epsilon atau |f(c)| < epsilon2.
"""

EPSILON = 0.000001
EPSILON2 = 0.00000001
NMAKS = 100


def f(x):
    return 4 * x ** 3 - 15 * x ** 2 + 17 * x - 6


def regula_falsi(a, b, epsilon=EPSILON, epsilon2=EPSILON2, nmaks=NMAKS):
    if f(a) * f(b) > 0:
        print("f(a) * f(b) > 0, selang tidak mengurung akar.")
        return None

    print(f"{'r':>3} {'a':>11} {'c':>11} {'b':>11} {'f(a)':>11} {'f(c)':>11} "
          f"{'f(b)':>11} {'Selang baru':>12} {'|c_r - c_r-1|':>14}")
    print("-" * 107)
    c_lama = None
    for r in range(nmaks):
        fa, fb = f(a), f(b)
        c = b - fb * (b - a) / (fb - fa)
        fc = f(c)
        a_lama, b_lama = a, b
        if fa * fc < 0:
            b = c
            selang = "[a, c]"
        else:
            a = c
            selang = "[c, b]"

        if c_lama is None:
            selisih = None
            teks_selisih = "-"
        else:
            selisih = abs(c - c_lama)
            teks_selisih = f"{selisih:.6f}"
        print(f"{r:>3} {a_lama:>11.6f} {c:>11.6f} {b_lama:>11.6f} {fa:>11.6f} "
              f"{fc:>11.6f} {fb:>11.6f} {selang:>12} {teks_selisih:>14}")

        if abs(fc) < epsilon2 or (selisih is not None and selisih < epsilon):
            return c, r + 1
        c_lama = c

    print(f"Jumlah lelaran melebihi Nmaks = {nmaks}")
    return None


def main():
    a, b = 1.5, 3
    print("f(x) = 4x^3 - 15x^2 + 17x - 6")
    print(f"Selang awal [{a}, {b}]")
    print(f"f({a}) = {f(a):.6f} ,  f({b}) = {f(b):.6f}")
    print(f"epsilon = {EPSILON}\n")

    hasil = regula_falsi(a, b)

    if hasil is not None:
        akar, n = hasil
        print()
        print(f"Hampiran akar x = {akar:.6f}")
        print(f"f({akar:.6f}) = {f(akar):.6e}")
        print(f"Jumlah lelaran = {n}")


if __name__ == "__main__":
    main()
