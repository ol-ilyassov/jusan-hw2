
# 6.Реализуйте программу для проверки, является ли 
# заданное число числом Фибоначчи (число, которое 
# является членом последовательности Фибоначчи). 
# Заданное число 25

def is_fibonacci(n:int) -> bool:
    # начало последовательности Фибоначчи.
    if n == 0 or n == 1:
        return True
    
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    
    return b == n

number = 25

if is_fibonacci(number):
    print("Fibonacci number")
else:
    print("not a Fibonacci number")

# Последовательность Фибоначчи: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...