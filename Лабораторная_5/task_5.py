def get_random_password() -> str:
    import string
    import random # TODO написать функцию генерации случайных паролей
    return random.sample(string.digits + string.ascii_lowercase + string.ascii_uppercase, 8)

print(get_random_password())
