
#Самая сложная задача фукнции
##hanoi-tower 
# "Ханойские башни" - это математическая головоломка. Паззл состоит из трех башен и нескольких дисков (бубликов).
# Задача состоит в том, что нужно переместить диски из первой башни в последнюю. При этом, диски меньшего размера можно положить сверху большего, но не наоборот.

# Напишите функцию hanoiTower, которая принимает число дисков n. Диски расположены на первой башне в порядке возрастания (снизу диски с большим значением, сверху наименьшим). Функция должна напечатать последовательность перекладываний в формате:
# Диск a с башни b переложить в башню c
# где,
# а номер диска
# b номер башни, с которой снимают диск
# c номер башни, на которую ложат диск
# Функция должна вывести минимальное количество команд для перемещения дисков с первой башни на последнюю.
# Пример
# Пример вывода программы для n = 2
# Диск 1 с башни 1 переложить в башню 2
# Диск 2 с башни 1 переложить в башню 3
# Диск 1 с башни 2 переложить в башню 3
# Ограничения
# 0 < n < 100
# Sample Input:
# 5
# Sample Output:
# Диск 1 с башни 1 переложить в башню 3
# Диск 2 с башни 1 переложить в башню 2
# Диск 1 с башни 3 переложить в башню 2
# Диск 3 с башни 1 переложить в башню 3
# Диск 1 с башни 2 переложить в башню 1
# Диск 2 с башни 2 переложить в башню 3
# Диск 1 с башни 1 переложить в башню 3
# Диск 4 с башни 1 переложить в башню 2
# Диск 1 с башни 3 переложить в башню 2
# Диск 2 с башни 3 переложить в башню 1
# Диск 1 с башни 2 переложить в башню 1
# Диск 3 с башни 3 переложить в башню 2
# Диск 1 с башни 1 переложить в башню 3
# Диск 2 с башни 1 переложить в башню 2
# Диск 1 с башни 3 переложить в башню 2
# Диск 5 с башни 1 переложить в башню 3
# Диск 1 с башни 2 переложить в башню 1
# Диск 2 с башни 2 переложить в башню 3
# Диск 1 с башни 1 переложить в башню 3
# Диск 3 с башни 2 переложить в башню 1
# Диск 1 с башни 3 переложить в башню 2
# Диск 2 с башни 3 переложить в башню 1
# Диск 1 с башни 2 переложить в башню 1
# Диск 4 с башни 2 переложить в башню 3
# Диск 1 с башни 1 переложить в башню 3
# Диск 2 с башни 1 переложить в башню 2
# Диск 1 с башни 3 переложить в башню 2
# Диск 3 с башни 1 переложить в башню 3
# Диск 1 с башни 2 переложить в башню 1
# Диск 2 с башни 2 переложить в башню 3
# Диск 1 с башни 1 переложить в башню 3

def hanoiTower(n, source=1, target=3, middle=2):
    if n == 1:
        print(f"Диск 1 с башни {source} переложить в башню {target}")
        return
    
    hanoiTower(n - 1, source, middle, target)

    # перекладывание последнего диска первой башни в третью башню.
    print(f"Диск {n} с башни {source} переложить в башню {target}")

    hanoiTower(n - 1, middle, target, source)

inp = int(input("Enter a number: "))
hanoiTower(inp)
