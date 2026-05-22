"""
Лабораторная работа №6
Генератор спирального обхода от центра
"""

def spiral_from_center(matrix):
    """Генератор для обхода матрицы по спирали от центра"""
    if not matrix or not matrix[0]:
        return
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Находим центр
    center_r = rows // 2
    center_c = cols // 2
    
    # Матрица посещённых клеток
    visited = [[False] * cols for _ in range(rows)]
    
    # Направления: вверх, вправо, вниз, влево
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    r, c = center_r, center_c
    yield r, c, matrix[r][c]
    visited[r][c] = True
    
    step_size = 1
    direction_index = 0
    
    while True:
        for _ in range(2):  # Каждый размер шага повторяется дважды
            dr, dc = directions[direction_index]
            for _ in range(step_size):
                r += dr
                c += dc
                if 0 <= r < rows and 0 <= c < cols and not visited[r][c]:
                    visited[r][c] = True
                    yield r, c, matrix[r][c]
                else:
                    return
            direction_index = (direction_index + 1) % 4
        step_size += 1


def get_spiral_order(matrix):
    """Возвращает список всех элементов в спиральном порядке"""
    return list(spiral_from_center(matrix))