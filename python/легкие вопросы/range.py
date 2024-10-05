
##range
# Реализовать функцию range, которая создает массив размером n, заполняет ячейки значениями от 1 до n и возвращает созданный массив.
# Пример
# int[] arr = range(5);
# for (int i = 0; i < arr.length; i++) {   
#     System.out.print(arr[i] + " ");
# }
# # Напечатает
# # 1 2 3 4 5
# Ограничения
# 0 < n <= 10_000
# Sample Input:
# 5
# Sample Output:
# [1, 2, 3, 4, 5]

def my_range(n:int) -> list:
    arr = []
    
    for i in range(1, n+1):
        arr.append(i)
        
    return arr

print("#1", "[n=5]", "result:", my_range(5))