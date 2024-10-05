
##miss-you 
# Дается два массива чисел, вернуть числа из второго массива, которые не присутствуют в первом в отсортированном порядке.
# Ограничения
# 0 <= array1.length <= 10_000
# 0 <= array2.length <= 10_000
# Sample Input:
# [1, 1, 3, 2, 5]
# [1, 3, 9, 1, 5, 7]
# Sample Output:
# [7, 9]

def miss_you(array1:list[int], array2:list[int]) -> list[int]:
    result=[]
    
    for i in range(len(array2)):
        for j in range(len(array1)):
            if array2[i]==array1[j]:
                break
            if j==len(array1)-1:
                result.append(array2[i])
    
    return sorted(result)
    
print("result:", miss_you([1,2,3,5], [1,2,3,6,4]))