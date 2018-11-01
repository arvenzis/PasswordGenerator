import string
import random


def password_generator(size=8, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for i in range(size))


print(password_generator())
