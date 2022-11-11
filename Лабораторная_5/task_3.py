import random
def get_unique_list_numbers(start=-10, finish=10, size=15) -> list[int]:
    password = []
    while len(password) != size:# TODO написать функцию для получения списка уникальных целых чисел
        symbol = random.randint(start, finish)
        if symbol not in password:
            password.append(symbol)
    return password

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
