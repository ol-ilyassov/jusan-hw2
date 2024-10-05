
# 7.Напишите программу, которая определяет, является 
# ли заданное число совершенным числом 
# (число, равное сумме своих делителей, исключая само число). 
# Выведите сообщение с результатом.

def is_perfect_number(n):
    if n < 1:
        return False
    
    total_sum = 0
    
    for i in range(1, n) :
        if n % i == 0:
            total_sum += i
        
    return total_sum == n

inp = int(input("Enter a number: "))

if is_perfect_number(inp):
    print("perfect number")
else:
    print("not a perfect number")
