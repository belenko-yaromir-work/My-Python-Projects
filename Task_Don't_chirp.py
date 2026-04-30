class NoSubstringError(Exception):
    pass


def chirp(*args, **kwargs):
    if "taboo" not in kwargs:
        raise NoSubstringError("No named argument.")
    
    for arg in args:
        if not isinstance(arg, str):
            raise TypeError("The argument is not a string.")
    
    taboo = kwargs["taboo"].lower()
    res = []
    
    for sound in args:
        if taboo not in sound.lower():
            res.append(sound)
    
    return sorted(res)


if __name__ == "__main__":
    try:
        sounds = ["Чирик", "Кар", "Чик-чирик", "Мяу", "Чирикует"]
        result = chirp(*sounds, taboo="чирик")
        print(f"Разрешенные звуки: {result}")
    except NoSubstringError as e:
        print(f"Ошибка: {e}")
