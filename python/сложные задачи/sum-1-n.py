
##sum-1-n 
# Дается число n. Вернуть сумму от 1 до n без использования циклов.
# Ограничения
# 1 <= n <= 65535
# Sample Input:
# 5
# Sample Output:
# 15

def sum_1_n(n:int) -> int:
    if n == 0:
        return 0
    
    return n + sum_1_n(n-1)

inp = int(input("Enter a number: "))

print("result:", sum_1_n(inp))