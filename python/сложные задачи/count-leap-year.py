
##count-leap-year 
# В этой задаче вам нужно вернуть кол-во високосных лет до заданного n года.
# Правило для определения високосного года [источник]:
# год, номер которого кратен 400, — високосный;
# остальные годы, номер которых кратен 100, — невисокосные (например, годы 1700, 1800, 1900, 2100, 2200, 2300);
# остальные годы, номер которых кратен 4, — високосные.
# все остальные годы — невисокосные.
# Допускается, что високосные годы можно считать с 0 года.
# Пример
# До года 100 присутстует 24 високосных лет.
# Ограничения
# n > 0
# Запрещенные библиотеки, конструкции
# for
# Sample Input:
# 4
# Sample Output:
# 1

def is_leap_year(year:int) -> bool:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    
    return False

def count_leap_years(n:int) -> int:
    if n < 1:
        return 0

    if is_leap_year(n):
        return 1 + count_leap_years(n - 1)
    
    return count_leap_years(n - 1)

inp = int(input("Enter a year: "))

print("result:", count_leap_years(inp))