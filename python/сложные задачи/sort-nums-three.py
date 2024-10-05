
##sort-nums-three 
# Напишите функцию, которая отсортировывает по возрастанию три числа a, b, c, без использования циклов.
# Отсортированные числа вывести в консоль.
# Пример
# 3 2 1 -> 1 2 3
# Sample Input:
# 3 2 1
# Sample Output:
# 1 2 3

def sort_nums_three(n1:int, n2:int, n3:int) -> list:
    if n1 > n2:
        n1, n2 = n2, n1
    if n1 > n3:
        n1, n3 = n3, n1
    if n2 > n3:
        n2, n3 = n3, n2
        
    return n1, n2, n3


a = int(input("Enter a number(A): "))
b = int(input("Enter a number(B): "))
c = int(input("Enter a number(C): "))

print("result:", sort_nums_three(a, b, c))