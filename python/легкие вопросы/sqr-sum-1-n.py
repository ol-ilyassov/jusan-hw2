
##sqr-sum-1-n
# Вернуть сумму квадратов чисел от 1 до n включительно.
# Ограничения
# 1 <= n <= 10860
# Sample Input:
# 3
# Sample Output:
# 14

def sqr_sum_1_n(n:int) -> int:
    sum = 0
    
    for i in range(1, n+1):
        sum += i**2
        
    return sum

print("#1", "[n=3]", "result:", sqr_sum_1_n(3))
print("#2", "[n=5]", "result:", sqr_sum_1_n(5))
