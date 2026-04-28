from spiral_generator import spiral_from_center

# Пример матрицы 5x5
matrix = [
    [ 1,  2,  3,  4,  5],
    [ 6,  7,  8,  9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

for r, c, value in spiral_from_center(matrix):
    print(f"({r}, {c}) -> {value:2d}")