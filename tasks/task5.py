# tasks/task1.py



def solve():




    numbers = map(int, input("Введите числа: ").split())
    squared_numbers = list(map(lambda x: x ** 2, numbers))
    print("Результат:", ' '.join(map(str, squared_numbers)))
# Ниже пишите решение задачии(Обязательно поставьте четыре пробела после функции Solve())


# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()