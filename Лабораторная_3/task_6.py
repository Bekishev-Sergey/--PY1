list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
num = max(list_numbers)
index = list_numbers.index(num)
o_o = list_numbers[-1]
list_numbers[-1] = num
list_numbers[index] = o_o

print(list_numbers)
