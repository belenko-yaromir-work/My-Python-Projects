class CounterString(str):
    def __init__(self, value=""):
        self.count = 0

    def upper(self):
        self.count += 1
        return CounterString(super().upper())

    def lower(self):
        self.count += 1
        return CounterString(super().lower())

    def replace(self, old, new, count=-1):
        self.count += 1
        return CounterString(super().replace(old, new, count))

    def get_stats(self):
        return self.count


if __name__ == "__main__":
    s = CounterString("Привет, Мир!")
    s = s.upper()
    s = s.lower()
    s = s.replace("мир", "Яромир")
    
    print(f"Итоговая строка: {s}")
    print(f"Количество изменений: {s.get_stats()}")
