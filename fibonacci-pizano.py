# Даны целые числа 1 <= n <= 10^18 и 2 <= m <= 10^5,
# необходимо найти остаток от деления n-го числа Фибоначчи на m.

# Решение через период Пизано

# https://ru.wikipedia.org/wiki/Период_Пизано
# https://oeis.org/A001175


def fib(n, m):
    if n == 0:
        return 0
    if n == 1:
        return 1
    x = 1
    f0 = 0
    f1 = 1
    pizano = [0]
    pizano_found = True
    for i in range(n - 1):
        pizano.append(x % m)
        x = f0 + f1
        f0, f1 = f1 % m, x % m
        if f0 == 0 and f1 == 1:
            break
    else:
        pizano_found = False

    pizano.pop()
    return pizano[n % len(pizano)] if pizano_found else x % m


def main():
    n, m = map(int, input().split())
    print(fib(n, m))


if __name__ == "__main__":
    main()
