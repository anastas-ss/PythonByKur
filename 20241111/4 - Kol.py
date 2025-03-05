import sys
from collections import deque

class ClassChecker:
    def __init__(self, code):
        self.code = code
        self.classes = {}
        self.mros = {}
        self.parse_classes()

    def parse_classes(self):
        # Разбираем код и собираем информацию о классах и их родителях
        lines = self.code.splitlines()
        for line in lines:
            if line.strip().startswith("class "):
                self.process_class_declaration(line.strip())

    def process_class_declaration(self, line):
        # Находим имя класса и его родительские классы
        parts = line.split('(')
        class_name = parts[0].split()[1].strip()  # Имя класса
        parent_classes = []

        if '(' in line:
            parents = parts[1].rstrip('):').split(',')
            parent_classes = [p.strip() for p in parents]

        self.classes[class_name] = parent_classes

    def check_mro(self):
        # Проверяем, что для каждого класса его MRO не нарушает правил C3
        for class_name in self.classes:
            mro = self.compute_mro(class_name)
            self.mros[class_name] = mro

        # Проверяем, что каждый класс наследуется в правильном порядке
        for class_name, mro in self.mros.items():
            for i, base_class in enumerate(mro[:-1]):
                if base_class not in self.mros:
                    return "No"
                # Проверяем, что этот base_class находится в MRO всех его наследников
                if mro[i + 1] not in self.classes.get(base_class, []):
                    return "No"

        return "Yes"

    def compute_mro(self, class_name):
        # Рассчитываем MRO с учетом C3
        # Начинаем с самого класса
        mro = [class_name]
        parent_classes = self.classes.get(class_name, [])

        # Если у класса нет родителей, его MRO это он сам
        if not parent_classes:
            return mro

        # Рекурсивно вычисляем MRO для всех родителей
        parent_mros = [self.compute_mro(parent) for parent in parent_classes]

        # Реализуем слияние MRO по алгоритму C3
        return self.merge_mros(parent_mros)

    def merge_mros(self, parent_mros):
        # Алгоритм слияния C3 для нескольких MRO
        result = []
        while any(parent_mros):
            # Выбираем кандидатов, которые не были еще добавлены в результат
            candidates = []
            for m in parent_mros:
                if m and m[0] not in result:
                    candidates.append(m[0])

            # Если нет кандидатов, это ошибка (циклическое наследование)
            if not candidates:
                return result
                        # Проверяем, что кандидаты не нарушают C3
            for candidate in candidates:
                # Проверяем, что кандидаты не находятся в конфликте с другими родителями
                valid = True
                for m in parent_mros:
                    if candidate in m:
                        parent_mros.remove(m)
                        break
                if valid:
                    result.append(candidate)
                    break
            else:
                return result

        return result


def main():
    # Чтение кода с stdin
    code = """class Nabal: pass
class Sienese: pass
class ganey: pass
class erasures: pass
class Faeroe(ganey, Sienese): pass
class OOUI(erasures, Faeroe): pass
class partakes(OOUI, erasures, Faeroe): pass"""
    #sys.stdin.read().strip()

    checker = ClassChecker(code)
    result = checker.check_mro()
    print(result)


if __name__ == "__main__":
    main()