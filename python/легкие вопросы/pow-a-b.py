
##pow-a-b
# Вернуть число a в степени b. Используя цикл.
# Ограничения
# b > 0
# a^b входит в ограничения типа int
# Sample Input:
# 2 6
# Sample Output:
# 64

def pow_a_b(a:int, b:int) -> int:
    result = 1
    
    for i in range(b):
        result *= a
        
    return result

print("#1", "[a=2, b=6]", "result:", pow_a_b(2, 6))
print("#2", "[a=2, b=3]", "result:", pow_a_b(2, 3))