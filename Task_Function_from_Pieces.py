from functools import lru_cache


@lru_cache(None)
def func(n):
    if n < 1:
        return 1
    if n % 2 == 0:
        return n + func(n // 2)
    else:
        return n * func(n - 1) + func(n - 2)


if __name__ == "__main__":
    number = 20
    print(f"Результат функции для n={number}: {func(number)}")
