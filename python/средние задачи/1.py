
# 1.Создайте программу, которая проверяет, 
# является ли введенное пользователем число четным 
# или нечетным, и выводит соответствующее сообщение.

def is_even(num:int) -> bool:
    if num % 2 == 0:
        return True
    
    return False

number = int(input("Enter a number: "))

if is_even(number):
    print("even number")
else:
    print("odd number")