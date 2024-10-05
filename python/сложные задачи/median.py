
##median 
# Реализовать функцию median, которое находится в середине массива, если его упорядочить по возрастанию, то есть такое число, что половина из элементов набора не меньше него, а другая половина не больше.
# Если кол-во элементов в массиве четное, то нужно вернуть левое значение медианы.
# Ограничения
# 0 <= array.length <= 10_000
# Sample Input:
# [1, 2, 3]
# Sample Output:
# 2

def median(arr:list[int]) -> int:
    if len(arr) == 0:
        return None
    
    # Сортируем массив
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    
    # Находим медиану
    if n % 2 == 0:
        return sorted_arr[(n // 2) - 1]
    
    return sorted_arr[n // 2]

# Примеры использования:
print("#1", "[1, 2, 3]", "result:", median([1, 2, 3]))
print("#2", "[3, 1, 2]", "result:", median([3, 1, 2]))
print("#3", "[1, 2, 3, 4]", "result:", median([1, 2, 3, 4]))
print("#4", "[]", "result:", median([]))
