
# 5.Напишите программу для нахождения всех 
# совершенных чисел (чисел, равных сумме 
# своих делителей, исключая само число) 
# в заданном диапазоне. Диапазон от 0 до 1000

def is_perfect_number(n:int) -> bool:
    # 0 не является совершенным числом.
    if n < 1:
        return False
    
    total_sum = 0
    
    for i in range(1, n) :
        if n % i == 0:
            total_sum += i
        
    return total_sum == n

perfect_numbers = []

for number in range(1, 1001):
    if is_perfect_number(number):
        perfect_numbers.append(number)

print("Perfect numbers in range (0:1000):")
print(perfect_numbers)
