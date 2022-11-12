import string
import random
def get_random_password(password_size = 8) -> str:
    return random.sample(string.digits + string.ascii_lowercase + string.ascii_uppercase, password_size)

print(get_random_password())
