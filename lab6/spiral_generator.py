def spiral_from_center(matrix):
    n = len(matrix)
    if n % 2 == 0:
        raise ValueError("Матрица должна быть нечётного размера (3x3, 5x5, ...)")

    center = n // 2
    row, col = center, center

    # Первый элемент (центр)
    yield row, col, matrix[row][col]

    # Длина текущего шага: 1, 1, 2, 2, 3, 3, 4, 4, ...
    step_length = 1
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # право, вверх, лево, низ

    while True:
        for idx, (dr, dc) in enumerate(directions):
            for _ in range(step_length):
                row += dr
                col += dc
                if 0 <= row < n and 0 <= col < n:
                    yield row, col, matrix[row][col]
                else:
                    return  # вышли за границы
            # После двух направлений увеличиваем длину шага
            if idx % 2 == 1:
                step_length += 1