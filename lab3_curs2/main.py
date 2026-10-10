def find_pair(numbers, target):
    # Создаем словарь для хранения просмотренных чисел
    seen = {}
    
    # Проходим по всем числам
    for number in numbers:
        # Вычисляем необходимое дополнение
        complement = target - number
        
        # Проверяем, есть ли дополнение в словаре
        if complement in seen:
            return f"{complement} {number}"
        
        # Добавляем текущее число в словарь
        seen[number] = True
    
    return "None"

# Считываем входные данные
n = int(input())
numbers = list(map(int, input().split()))
k = int(input())

# Выводим результат
print(find_pair(numbers, k))
