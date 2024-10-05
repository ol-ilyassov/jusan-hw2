
# 4.Реализуйте программу, которая определяет, 
# является ли заданная дата корректной (). 
# Выведите соответствующее сообщение.
# Дата дана в формате "20.01.2002"

def is_leap_year(year:int) -> bool:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    
    return False

def is_valid_date(date_str) -> bool:
    day, month, year = map(int, date_str.split('.'))
    
    if year < 1:
        return False
    
    if month < 1 or month > 12:
        return False
    
    max_days = 0
    if month in (1, 3, 5, 7, 8, 10, 12):
        max_days = 31
    elif month in (4, 6, 9, 11):
        max_days = 30
    else:  # Февраль
        if is_leap_year(year):
            max_days = 29
        else:
            max_days = 28
    
    if day < 1 or day > max_days:
        return False

    return True

inp = input("Enter a date (example: 20.01.2002): ")

if is_valid_date(inp):
    print("valid date")
else:
    print("not a valid date")
