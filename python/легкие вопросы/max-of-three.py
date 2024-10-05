
##max-of-three
# Дается три числа a, b и c. Вернуть максимальное число из них.
# Sample Input:
# 42 1 0
# Sample Output:
# 42

def max_of_three(a:int, b:int, c:int) -> int:
    num = a
    
    if b > num:
        num = b
    if c > num:
        num = c
        
    return num

print("#1", "[a=1, b=2, c=3]", "result:", max_of_three(1, 2, 3))
print("#1", "[a=15, b=10, c=5]", "result:", max_of_three(15, 10, 5))
print("#1", "[a=20, b=40, c=30]", "result:", max_of_three(20, 40, 30))