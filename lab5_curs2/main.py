def is_palindrome(s: str) -> bool:
    def is_alnum(c: str) -> bool:
        return ('A' <= c <= 'Z') or ('a' <= c <= 'z') or ('0' <= c <= '9')
    
    left, right = 0, len(s) - 1
    
    while left < right:
        # Перемещаем левый указатель вправо, пропуская не-алфавитно-цифровые символы
        while left < right and not is_alnum(s[left]):
            left += 1
            
        # Перемещаем правый указатель влево, пропуская не-алфавитно-цифровые символы
        while left < right and not is_alnum(s[right]):
            right -= 1
            
        # Сравниваем символы без учета регистра
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
        
    return True

# Чтение входных данных и вывод результата
input_string = input().strip()
print(str(is_palindrome(input_string)).upper())
