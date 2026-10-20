"""
Pencarian selang kecil yang mengandung akar

Tentukan selang yang mengandung akar persamaan:
    f(x) = 4x^3 - 15x^2 + 17x - 6 = 0

Nilai f(x) dicetak pada titik-titik absis yang berjarak tetap h
di dalam selang [a, b]. Jika tanda f(x) berubah pada sebuah upaselang,
maka di dalam upaselang tersebut terdapat minimal satu akar.
"""


def f(x):
    return 4 * x ** 3 - 15 * x ** 2 + 17 * x - 6


def cari_selang(a, b, h):
    n = round((b - a) / h)
    xs = [round(a + i * h, 10) for i in range(n + 1)]

    print(f"{'x':>6} {'f(x)':>12}")
    print("-" * 19)
    for x in xs:
        print(f"{x:>6.2f} {f(x):>12.6f}")
    print("-" * 19)

    hasil = []
    for i in range(n + 1):
        if f(xs[i]) == 0:
            hasil.append(f"x = {xs[i]:.2f} adalah akar (f(x) = 0)")
        elif i < n and f(xs[i]) * f(xs[i + 1]) < 0:
            hasil.append(f"[{xs[i]:.2f}, {xs[i + 1]:.2f}] mengandung akar")
    return hasil


def main():
    a, b, h = 0, 3, 0.1
    print("f(x) = 4x^3 - 15x^2 + 17x - 6")
    print(f"a = {a} ,  b = {b} ,  h = {h}\n")

    hasil = cari_selang(a, b, h)

    print()
    print("Berdasarkan tabel di atas:")
    for teks in hasil:
        print(f"  {teks}")


if __name__ == "__main__":
    main()
