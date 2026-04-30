def decor(f):
    def wrapper(*args, **kwargs):
        res = f(*args, **kwargs)
        return res.title()

    return wrapper


@decor
def low_words(*args, separator="; "):
    words = [w for w in args if w.islower()]
    return separator.join(words)


@decor
def short_words(*args, length=1):
    words = [w for w in args if len(w) <= length]
    return ", ".join(words)


if __name__ == "__main__":
    print(low_words("яблоко", "Груша", "слива", separator=" | "))
    print(short_words("кот", "автомобиль", "дом", "окно", length=3))
