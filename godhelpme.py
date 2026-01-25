# Функция для нахождения суммы всех чисел от 1 до N
def sum_to_n(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

N = int(input("Введите число N: "))

print("Сумма чисел от 1 до", N, ":", sum_to_n(N))

# Функция для переворачивания строки
def reverse_string(s):
    return s[::-1]

s = input("Введите строку: ")

print("Перевернутая строка:", reverse_string(s))
# Функция для подсчета количества гласных в строке
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count

input_string = input("Введите строку: ")
print("Количество гласных в строке:", count_vowels(input_string))
# Функция для поиска наименьшего числа в списке
def lowest_digit(s):
    digits = [int(char) for char in s if char.isdigit()]
    if not digits:
        return "Нет цифр в строке"
    return f"Наименьшая цифра: {min(digits)}"

s = input("Введите строку чисел: ")
print(lowest_digit(s))
# Функция для проверки, является ли строка палиндромом
def palindrome_check(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    if cleaned == cleaned[::-1] :
        return 'Строка является палиндромом'
    else:
        return 'Строка не является палиндромом'

s = input("Введите строку: ")
print(palindrome_check(s))

