
##perfectly-balanced 
# Дается массив чисел, найти в массиве такой элемент, где сумма чисел слева равна сумме чисел справа.
# Если такое число есть, то вернуть true, в противном случае false.
# Пример
# Возьмем массив 1, 2, 9, 8, 5, 7
# Число 8 является элементом, где сумма чисел слева равна сумме чисел справа.
# 1   2   9   8   5   7
# (1+2+9)=12  ↑  (5+7)=12
# Ограничения
# 0 <= array.length <= 10_000
# Sample Input:
# [1, 2, 9, 8, 5, 7]
# Sample Output:
# true

def perfectly_balanced(nums:list[int]) -> bool:
    for i in range(1, len(nums)-1):
        left = 0
        right = 0
        
        for l in range(i):
            left += nums[l]
        
        for r in range(i + 1, len(nums)):
            right += nums[r]
        
        if left == right:
            return True
        
    return False

print("result:", perfectly_balanced([1, 2, 9, 8, 5, 7]))