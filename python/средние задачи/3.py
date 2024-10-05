
# 3.Реализуйте программу, которая определяет, 
# является ли заданное число простым (имеет 
# только два делителя: 1 и само число). 
# Выведите соответствующее сообщение.

def is_prime(num:int) -> bool:
    # 0 и 1 не являются простыми числами.
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True

number = input("Enter a number: ")

if is_prime(int(number)):
    print("prime number")
else:
    print("not a prime number")