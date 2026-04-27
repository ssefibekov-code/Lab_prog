# Замыкание для получения простых чисел.

def log_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Called {func.__name__} with args {args}, result: {result}")
        return result
    return wrapper

def make_calc(operation, initial=0):
    result = initial
    
    @log_decorator
    def calc(value):
        nonlocal result
        if operation == '+':
            result += value
        elif operation == '-':
            result -= value
        elif operation == '*':
            result *= value
        elif operation == '/':
            result /= value
        return result
    
    return calc

# Пример использования
calc = make_calc("+", initial=10)
print(calc(5))  # 15
print(calc(3))  # 18


# Декоратор, не позволяющий функции выполняться больше определённого времени.

def call_limiter(max_calls=None):
    def decorator(func):
        calls = 0
        
        def wrapper(*args, **kwargs):
            nonlocal calls
            if max_calls is not None and calls >= max_calls:
                raise Exception("Превышено максимальное количество вызовов")
            calls += 1
            try:
                return func(*args, **kwargs)
            finally:
                # Уменьшаем счетчик при выходе из функции
                calls -= 1
        return wrapper
    return decorator

@call_limiter(max_calls=3)
def test_function():
    print("Функция вызвана")

# Пример с рекурсией
@call_limiter(max_calls=5)
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

# Тестирование
try:
    print(factorial(3))  # Должно работать
    print(factorial(5))  # Вызовет ошибку из-за превышения лимита
except Exception as e:
    print(e)
