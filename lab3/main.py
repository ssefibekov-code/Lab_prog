import itertools


# Task 1

def task1() -> int:
    letters = ['И', 'В', 'А', 'Н']
    code_length = 5
    total_codes_with_i = 0
    
    for combination in itertools.product(letters, repeat=code_length):
        if 'И' in combination:
            total_codes_with_i += 1
    
    return total_codes_with_i



# Task 2

def task2() -> int:
    term1 = 7 * (512 ** 120)
    term2 = 6 * (64 ** 100)
    term3 = 8 ** 210
    result = term1 - term2 + term3 - 255
    
    octal_string = oct(result)[2:]
    zero_count = octal_string.count('0')
    
    return zero_count



# Task 3

def find_divisors_count(n: int) -> int:
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 1
            if i != n // i:
                count += 1
    return count


def task3() -> tuple:
    start_num = 84052
    end_num = 84130
    
    max_divisors = 0
    number_with_max = 0
    
    for num in range(start_num, end_num + 1):
        current_divisors = find_divisors_count(num)
        if current_divisors > max_divisors:
            max_divisors = current_divisors
            number_with_max = num
    
    return (max_divisors, number_with_max)


# Result

if __name__ == "__main__":
    result1 = task1()
    result2 = task2()
    div_count, number = task3()
    
    print(result1)
    print(result2)
    print(div_count, number)