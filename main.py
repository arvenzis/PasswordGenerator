import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

secure_random = random.SystemRandom()
password = ''

for i in range(8):
    password += secure_random.choice(letters)

print(password)