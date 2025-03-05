import random
from collections.abc import Sequence, Iterable

def rnd(a, b=None):
    match (a, b):
        case (int(), None):
            # Если передан только один целый параметр, возвращаем случайное число в диапазоне [0...a]
            print('(int(), None)')
            return random.randint(0, a)
        
        case (int(), int()):
            print('(int(), int())')
            # Если переданы два целых числа, возвращаем случайное число в диапазоне [a...b]
            return random.randint(a, b)
        
        case (float(), float()):
            print('(float(), float())')
            # Если переданы два вещественных числа, возвращаем случайное вещественное число в диапазоне [a...b)
            return random.uniform(a, b)
        
        case (float(), int()) | (int(), float()):
            print('(float(), int()) | (int(), float())')
            # Если один параметр вещественный, а другой целый или вещественный, возвращаем случайное вещественное число
            return random.uniform(a, b)
        
        case (Sequence(), None):
            print('(Sequence(), None)')
            # Если передан индексируемый объект (например, список или строка), возвращаем случайный элемент
            return random.choice(a)
        
        case (Sequence(), int()):
            print('(Sequence(), int()')
            # Если передан индексируемый объект и целое число, возвращаем список из b случайных элементов
            return random.sample(a, b)
        
        case (str(), int()):
            print('(str(), int())')
            # Если передана строка и целое число, возвращаем случайную подстроку длиной b
            start = random.randint(0, len(a) - b)
            return a[start:start + b]
        
        case (str(), None):
            print('(str(), None)')
            # Если передана только строка, возвращаем случайное слово
            return random.choice(a.split())
        
        case (str(), str()):
            print('(str(), str())')
            # Если переданы две строки, возвращаем случайную строку из split(a, b)
            return random.choice(a.split(b))
        
        case (Iterable(), None):
            print('(Iterable(), None)')
            # Если передан итерируемый объект (не индексируемый), возвращаем случайный элемент
            return random.choice(list(a))
        
        case (Iterable(), int()):
            print('(Iterable(), int())')
            # Если передан итерируемый объект и целое число, возвращаем список из b случайных элементов
            return random.sample(list(a), b)
        
        case _:
            print('huy')
            raise TypeError(f"Unsupported types for a={type(a)} and b={type(b)}")



import random
random.seed(1234)
print(rnd(range(20)))
print(*rnd(range(30), 5))
print(rnd("range(20)"))
print(rnd("range(30), 5", 5))

