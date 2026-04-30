class LimitedList(list):
    def __init__(self, max_size, d=None):
        self.max_size = max_size
        super().__init__((d or [])[:max_size])

    def append(self, item):
        if len(self) < self.max_size:
            super().append(item)
            return f"Элемент {item} добавлен."
        return f"Список полон! Максимальный размер: {self.max_size}"

    def is_full(self):
        return len(self) >= self.max_size

    def available_space(self):
        return self.max_size - len(self)


if __name__ == "__main__":
    my_list = LimitedList(3, ["Яблоко", "Банан"])
    
    print(my_list.append("Груша"))
    print(my_list.append("Слива"))
    print(f"Осталось места: {my_list.available_space()}")
    print(f"Весь список: {my_list}")
