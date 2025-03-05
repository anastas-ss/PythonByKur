class Pairs:
    # Определяем имена полей
    letters = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)]

    def __init__(self, N):
        if not (1 <= N <= 52):
            raise ValueError("N должно быть в диапазоне от 1 до 52")
        
        # Создаем слоты для хранения значений
        self.__slots__ = self.letters[:52]  # Сохраняем только первые 52 буквы
        self._order = self.letters[N-1:] + self.letters[:N-1]  # Определяем порядок отображения
        self._values = {letter: idx + 1 for idx, letter in enumerate(self.letters)}  # Изначальные значения
        
        # Устанавливаем значения полей в соответствии с порядком
        for i, letter in enumerate(self._order):
            setattr(self, letter, i + 1)

    def __str__(self):
        return ' '.join(self._order)

    def __getattr__(self, name):
        if name in self.letters:
            return self._values[name]
        raise AttributeError(f"{name} не является атрибутом {self.__class__.__name__}")

p = Pairs(12)
print(p, p.b, p.y)