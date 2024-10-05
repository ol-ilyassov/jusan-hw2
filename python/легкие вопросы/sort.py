
##sort
# Реализовать функцию sort, которая принимает массив array(int[]). Функция должна отсортировать массив по возрастанию.
# Подсказка: https://habr.com/ru/post/204600/
# Запрещено использовать Arrays.sort.
# Пример
# int array[] = {7, 5, 9, 1, 4};
# sort(array);
# for (int i = 0; i < array.length; i++) {   
#     System.out.print(array[i] + " ");
# }
# # Напечатает
# # 1 4 5 7 9
# Ограничения
# 0 <= array.length <= 10_000
# Sample Input:
# [3, 2, 1]
# Sample Output:
# [1, 2, 3]

def my_sort(arr:list[int]) -> list[int]:
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr
    
    
print("#1", "[7, 5, 9, 1, 4]", "result:", my_sort([7, 5, 9, 1, 4]))
print("#2", "[3, 2 ,1]", "result:", my_sort([3, 2, 1]))
