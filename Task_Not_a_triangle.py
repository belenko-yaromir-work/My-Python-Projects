class NotEnoughError(Exception):
    pass


class DoNotMatchError(Exception):
    pass


def istriangle(*args):
    if len(args) < 3:
        raise NotEnoughError("Not enough arguments.")

    for x in args:
        if len(x) != 2:
            raise DoNotMatchError("The number of coordinates does not match.")

    (x1, y1), (x2, y2), (x3, y3) = args[0], args[1], args[2]
    area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
    return area != 0


if __name__ == "__main__":
    try:
        print(istriangle((0, 0), (3, 0), (0, 4)))
        print(istriangle((0, 0), (1, 1), (2, 2)))
    except (NotEnoughError, DoNotMatchError) as e:
        print(f"Ошибка: {e}")
