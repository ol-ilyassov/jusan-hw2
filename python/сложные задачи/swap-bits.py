
##swap-bits
# Реализуйте метод, который меняет местами первые 4 бита с остальными 4 и возвращает результат.
# Примеры
# 0000 1111 -> 1111 0000
# 0110 0111 -> 0111 0110
# Ограничения
# 0 <= a <= 255
# Sample Input:
# 15
# Sample Output:
# 240

# * Не придумал лучше решение, чем сразу воспользоваться 
# * bitwise операторами.

def swap_bits(a):
    if not (0 <= a <= 255):
        return None

    # получить нужные части
    first_bits = (a & 0b11110000)
    second_bits = (a & 0b00001111)

    # объединить
    result = (second_bits << 4) | (first_bits >> 4)
    
    return result

print("result:", swap_bits(15))
