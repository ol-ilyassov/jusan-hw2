
##int-cmp
# Дается два числа a и b. Вернуть:
# 1, если a > b
# 0, если a = b
# -1, если a < b
# Sample Input:
# 1 0
# Sample Output:
# 1

def int_cmp(a:int, b:int) -> int:
    if a > b:
        return 1
    elif a < b:
        return -1
    
    return 0

print("#1", "[10 > 5]", "result:", int_cmp(10, 5))
print("#2", "[5 < 10]"," result:", int_cmp(5, 10))
print("#3", "[10 == 10]", "result:", int_cmp(10, 10))
