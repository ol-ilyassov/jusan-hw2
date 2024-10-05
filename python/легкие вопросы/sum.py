
##sum
# Реализовать функцию sum, которая возвращает сумму чисел массива.
# Пример
# int array[] = {7, 5, 9, 1, 4};
# int sum_number = sum(array);
# print(sum_number); // <-- выведет 26
# Ограничения
# 0 <= array.length <= 10_000
# Sample Input:
# [1, 2, 3]
# Sample Output:
# 6

def sum(arr: list[int]) -> int:
    result = 0
    
    for i in range(len(arr)):
        result += arr[i]
    
    return result

print("#1", "[7, 5, 9, 1, 4]", "result:", sum([7, 5, 9, 1, 4]))
print("#2", "[1, 2, 3]", "result:", sum([1, 2, 3]))
