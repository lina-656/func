# task1.py
def task1():
    """
    Выполняет задание 1: Сумма двух массивов.
    
    Запрашивает у пользователя ввод двух массивов, сортирует их,
    вычисляет сумму элементов с учетом заданных условий и 
    выводит результат.
    """
    print("Задание 1: Сумма двух массивов")

    arr1 = list(map(int, input("Введите элементы первого массива через пробел: ").split()))
    arr2 = list(map(int, input("Введите элементы второго массива через пробел: ").split()))

    if len(arr1) != len(arr2):
        print("Массивы должны быть одинакового размера.")
        return

    arr1.sort(reverse=True)  
    arr2.sort()               
    
    # Используем map и zip для вычисления результата
    result = list(map(lambda a_b: a_b[0] + a_b[1] if a_b[0] != a_b[1] else 0, zip(arr1, arr2)))

    # Сортировка результата с использованием встроенной функции sorted
    result.sort()
    
    print("Результат:", result)