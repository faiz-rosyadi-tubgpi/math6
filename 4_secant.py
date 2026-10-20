"""
Metode Secant - metode terbuka

Tentukan akar persamaan:
    f(x) = 4x^3 - 15x^2 + 17x - 6 = 0 ,  x0 = 3 ,  x1 = 2.5

Turunan f'(x) pada Newton-Raphson dihampiri dengan
    f'(x_r) ~ (f(x_r) - f(x_r-1)) / (x_r - x_r-1)

sehingga rumus secant menjadi
    x_{r+1} = x_r - f(x_r)(x_r - x_r-1) / (f(x_r) - f(x_r-1))
"""

EPSILON = 0.000001
NMAKS = 30


def f(x):
    return 4 * x ** 3 - 15 * x ** 2 + 17 * x - 6


def secant(x0, x1, epsilon=EPSILON, nmaks=NMAKS):
    print(f"{'r':>3} {'x_r':>14} {'f(x_r)':>14} {'|x_r+1 - x_r|':>16}")
    print("-" * 50)
    print(f"{0:>3} {x0:>14.6f} {f(x0):>14.6f} {abs(x1 - x0):>16.6f}")
    x_lama, x = x0, x1
    for r in range(1, nmaks + 1):
        fx_lama, fx = f(x_lama), f(x)
        if fx - fx_lama == 0:
            print(f"{r:>3} {x:>14.6f} {fx:>14.6f} {'-':>16}")
            print("f(x_r) - f(x_r-1) = 0, lelaran tidak dapat dilanjutkan.")
            return None

        x_baru = x - fx * (x - x_lama) / (fx - fx_lama)
        selisih = abs(x_baru - x)
        print(f"{r:>3} {x:>14.6f} {fx:>14.6f} {selisih:>16.6f}")

        x_lama, x = x, x_baru
        if selisih < epsilon:
            print(f"{r + 1:>3} {x:>14.6f} {f(x):>14.6f} {'-':>16}")
            return x, r

    print(f"Jumlah lelaran melebihi Nmaks = {nmaks} -> Divergen!")
    return None


def main():
    x0, x1 = 3, 2.5
    print("f(x) = 4x^3 - 15x^2 + 17x - 6")
    print(f"x0 = {x0} ,  x1 = {x1}")
    print(f"epsilon = {EPSILON}\n")

    hasil = secant(x0, x1)

    if hasil is not None:
        akar, n = hasil
        print()
        print(f"Hampiran akar x = {akar:.6f}")
        print(f"f({akar:.6f}) = {f(akar):.6e}")
        print(f"Jumlah lelaran = {n}")


if __name__ == "__main__":
    main()
