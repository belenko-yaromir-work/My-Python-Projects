def is_palindrome(s):
    res_t = "".join(_.lower() for _ in s if _.isalpha())

    def check(z):
        if len(z) <= 1:
            return True
        if z[0] != z[-1]:
            return False

        return check(z[1:-1])

    return check(res_t)


if __name__ == "__main__":
    test_string = "А роза упала на лапу Азора"
    if is_palindrome(test_string):
        print(f"Строка '{test_string}' — палиндром!")
    else:
        print("Это не палиндром.")
