def get_unique_list_numbers() -> list[int]:
    import random
    password = []
    while len(password) != 15:# TODO написать функцию для получения списка уникальных целых чисел
        symbol = random.randint(-10, 10)
        if symbol not in password:
            password.append(symbol)
    return password

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
