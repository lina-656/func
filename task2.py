# task2.py
def task2():
    """
    Выполняет задание 2: Проверка сумм трех массивов.
    
    Запрашивает у пользователя ввод трех массивов и проверяет,
    могут ли два числа под одним и тем же номером в сумме давать третье число.
    Если могут, то сумма трех чисел возводится в степень наименьшего числа.
    """
    
    print("Задание 2: Проверка сумм трех массивов")

    arr1 = list(map(int, input("Введите элементы первого массива через пробел: ").split()))
    arr2 = list(map(int, input("Введите элементы второго массива через пробел: ").split()))
    arr3 = list(map(int, input("Введите элементы третьего массива через пробел: ").split()))

    if len(arr1) != len(arr2) or len(arr2) != len(arr3):
        print("Все массивы должны быть одинакового размера.")
        return

    results = []  
    
    # Используем zip для объединения массивов и filter для проверки условий
    results = [
        (a + b + c) ** min(a, b, c) 
        for a, b, c in zip(arr1, arr2, arr3) 
        if a + b == c
    ]
    
    print("Результаты:", results)