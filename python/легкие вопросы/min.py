
##min
# Реализовать функцию min, которая возвращает минимальное число из массива. Если в массиве нет элементов, верните 0.
# Ограничения
# 0 <= array.length <= 10_000
# Sample Input:
# [1, 2, 3]
# Sample Output:
# 1

def min(arr):
    if len(arr) == 0:
        return 0
    
    num = arr[0]
    for i in range(1, len(arr)):
        if num > arr[i]:
            num = arr[i]
            
    return num

print("#1" , "[1, 2, 3]", "result:", min([1, 2, 3]))
print("#2" , "[1, 3, 2]", "result:", min([1, 3, 2]))
print("#3" , "[]", "result:", min([]))