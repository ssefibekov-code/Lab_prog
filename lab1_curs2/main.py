k = int(input())
field = [input().strip() for _ in range(4)]

# Считаем количество каждой цифры
count = [0] * 10  # индексы 1..9
for row in field:
    for ch in row:
        if ch != '.':
            count[int(ch)] += 1

# Максимум клавиш, которые могут нажать двое
max_keys = 2 * k

# Считаем баллы
score = 0
for t in range(1, 10):
    if count[t] > 0 and count[t] <= max_keys:
        score += 1

print(score)