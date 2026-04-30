def square(f):
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        return [x**2 for x in res]

    return wrapper


def minus(f):
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        return [x - 1 for x in res]

    return wrapper


@square
@minus
def multiples(*args, key=1):
    return [x for x in args if x % key == 0]


if __name__ == "__main__":
    print(multiples(3, 6, 9, 12, key=3))
