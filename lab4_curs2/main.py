def find_distances(n, street):
    # Создаем массив для результатов
    result = [0] * n
    
    # Первый проход - слева направо
    last_zero = -float('inf')
    for i in range(n):
        if street[i] == 0:
            last_zero = i
        result[i] = i - last_zero
    
    # Второй проход - справа налево
    last_zero = float('inf')
    for i in range(n-1, -1, -1):
        if street[i] == 0:
            last_zero = i
        result[i] = min(result[i], last_zero - i)
    
    return result

# Считываем входные данные
n = int(input())
street = list(map(int, input().split()))

# Получаем и выводим результат
distances = find_distances(n, street)
print(' '.join(map(str, distances)))
