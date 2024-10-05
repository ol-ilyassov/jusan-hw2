
# 8.Создайте программу, которая определяет, 
# в какой сезон года попадает заданная дата 
# (месяц и день). 

def season(month, day):
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    else:
        return "autumn"
    

month = int(input("Enter a month: "))
day = int(input("Enter a day: "))

# В случае если даты правильные, то значение сезона будет зависить лишь от месяца:
print("Season:", season(month, day))