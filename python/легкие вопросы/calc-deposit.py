
##calc-deposit
# Написать функцию, которая возвращает сколько будет денег на депозите через n месяцев при ставке k и изначальном балансе b тенге.
# Вознаграждения по депозиту начисляются каждый месяц.
# Ограничения
# 0 <= n <= 10000
# 0 <= k <= 100
# 0 <= b <= 10000
# Пример
# Если положить на депозит 1000 тенге на срок в 1 месяц со ставкой в 5%, то через месяц на счете будет 1050 тенге.
# Sample Input:
# 1 5 1000
# Sample Output:
# 1050.0

def calc_deposit(expire:int, percent:float, balance:float) -> float:
    for i in range(expire):
        balance += balance * percent / 100
        
    return balance # round(balance, 1)

print("#1", "[expire=1, percent=5, balance=1000]", "result:", calc_deposit(1, 5, 1000))