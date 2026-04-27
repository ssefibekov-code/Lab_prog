# С рекурсией

def linearize_recursive(nested_list):
    """
    Рекурсивная линеаризация вложенного списка.
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(linearize_recursive(item))
        else:
            result.append(item)
    return result


def linearize_iterative(nested_list):
    """
    Итеративная линеаризация вложенного списка.
    """
    result = []
    stack = [nested_list]
    
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            for item in reversed(current):
                stack.append(item)
        else:
            result.append(current)
    
    return list(reversed(result))


# Без рекурсии
def a_recursive(k):
    """
    Рекурсивное вычисление a_k.
    a_1 = 1, a_k = 2*b_{k-1} + a_{k-1}, b_k = 2*a_{k-1} + b_{k-1}
    """
    def helper(k):
        if k == 1:
            return 1, 1
        a_prev, b_prev = helper(k - 1)
        a_k = 2 * b_prev + a_prev
        b_k = 2 * a_prev + b_prev
        return a_k, b_k
    
    return helper(k)[0]


def a_iterative(k):
    """
    Итеративное вычисление a_k.
    a_1 = 1, a_k = 2*b_{k-1} + a_{k-1}, b_k = 2*a_{k-1} + b_{k-1}
    """
    if k == 1:
        return 1
    
    a_prev, b_prev = 1, 1
    
    for _ in range(2, k + 1):
        a_k = 2 * b_prev + a_prev
        b_k = 2 * a_prev + b_prev
        a_prev, b_prev = a_k, b_k
    
    return a_prev

# Вывод функций

if __name__ == "__main__":
    print("Линеаризация списка:")
    print(linearize_recursive([1, 2, [3, 4, [5, [6, []]]]]))
    print(linearize_iterative([1, 2, [3, 4, [5, [6, []]]]]))
    
    print("\nРекуррентная последовательность a_k:")
    for k in range(1, 8):
        print(f"a_{k} = {a_recursive(k)}")
    
    print("\nРекуррентная последовательность a_k (итеративно):")
    for k in range(1, 8):
        print(f"a_{k} = {a_iterative(k)}")