
##print-even-a-b
# Вывести в консоль четные числа в диапазоне от a включительно до b включительно.
# Sample Input:
# 0 4
# Sample Output:
# 0 2 4

def print_even_a_b(a:int, b:int):
    for n in range (a, b+1):
        if n % 2 == 0:
            print(n)

print("#1", "[a=0, b=4]", "result:") 
print_even_a_b(0, 4)

print("#2", "[a=3, b=7]", "result:")
print_even_a_b(2, 7)