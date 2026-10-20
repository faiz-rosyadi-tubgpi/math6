"""
Metode Lelaran Titik-Tetap (Fixed Point) - metode terbuka

Tentukan akar persamaan:
    f(x) = 4x^3 - 15x^2 + 17x - 6 = 0 ,  x0 = 3

f(x) = 0 disusun menjadi x = g(x):
    17x = -4x^3 + 15x^2 + 6
      x = (-4x^3 + 15x^2 + 6) / 17

    g(x)  = (-4x^3 + 15x^2 + 6) / 17
    g'(x) = (-12x^2 + 30x) / 17

Prosedur lelaran:
    x_{r+1} = g(x_r)

Syarat konvergen: |g'(x)| < 1 di sekitar akar.
"""

EPSILON = 0.000001
NMAKS = 100


def f(x):
    return 4 * x ** 3 - 15 * x ** 2 + 17 * x - 6


def g(x):
    return (-4 * x ** 3 + 15 * x ** 2 + 6) / 17


def dg(x):
    return (-12 * x ** 2 + 30 * x) / 17


def lelaran_titik_tetap(x0, epsilon=EPSILON, nmaks=NMAKS):
    print(f"{'r':>3} {'x_r':>14} {'|x_r+1 - x_r|':>16}")
    print("-" * 35)
    x = x0
    print(f"{0:>3} {x:>14.6f} {'-':>16}")
    for r in range(1, nmaks + 1):
        x_sebelumnya = x
        x = g(x)
        selisih = abs(x - x_sebelumnya)
        print(f"{r:>3} {x:>14.6f} {selisih:>16.6f}")
        if selisih < epsilon:
            return x, r
        if abs(x) > 1e10:
            print("Nilai x membesar tanpa batas -> Divergen!")
            return None
    print(f"Jumlah lelaran melebihi Nmaks = {nmaks} -> Divergen!")
    return None


def main():
    x0 = 3
    print("f(x)  = 4x^3 - 15x^2 + 17x - 6")
    print("g(x)  = (-4x^3 + 15x^2 + 6) / 17")
    print("g'(x) = (-12x^2 + 30x) / 17")
    print(f"x0    = {x0}")
    print(f"epsilon = {EPSILON}\n")

    hasil = lelaran_titik_tetap(x0)

    if hasil is not None:
        akar, n = hasil
        print()
        print(f"Hampiran akar x = {akar:.6f}")
        print(f"f({akar:.6f}) = {f(akar):.6e}")
        print(f"g'({akar:.6f}) = {dg(akar):.6f}  -> |g'| < 1, konvergen")
        print(f"Jumlah lelaran = {n}")


if __name__ == "__main__":
    main()
