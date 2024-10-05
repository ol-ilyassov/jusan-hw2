
# 2.Реализуйте программу, которая определяет, 
# является ли введенная пользователем строка 
# палиндромом (читается одинаково слева направо 
# и справа налево). Выведите соответствующее сообщение.

def is_palindrome(s:str) -> bool:
    return s == s[::-1]
    
inp = input("Enter a string: ")

if is_palindrome(inp):
    print("palindrome")
else:
    print("not a palindrome")