def sizer(cls):
    class Sizer(cls):
        def __init__(self, *args, **kwargs):
            # Для классов, которые имеют __init__, вызываем его
            if cls is not complex:
                super().__init__(*args, **kwargs)
            self._size_value = None

        @property
        def size(self):
            if self._size_value is not None:
                return self._size_value
            if hasattr(self, '__len__'):
                return len(self)
            elif hasattr(self, '__abs__'):
                return abs(self)
            return 0

        @size.setter
        def size(self, value):
            self._size_value = value

        @size.deleter
        def size(self):
            self._size_value = None

    return Sizer

@sizer
class S(list):
    pass

@sizer
class N(complex):
    pass

@sizer
class E(Exception):
    pass

# Примеры использования
for obj in (S("QWER"), N(3 + 4j), E("Exceptions know no lengths!")):
    print(obj, obj.size)

p = S(range(10, 15))
print(p.size)  # Должно вернуть 5
p.size = p.pop()  # Присваиваем значение size
print(p.size)  # Должно вернуть последнее значение из списка
del p.size  # Удаляем size
print(p.size)  # Должно вернуть текущее значение size (должно быть 4)