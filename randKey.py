import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letter = uppercase_letters.lower()

nums = "0123456789"

symbols = "!@#$%^&*()_-=+.,?/:|"

upper, lower, num, symbol = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letter
if num:
    all += nums
if symbol:
    all += symbols
print('Enter length: ')

length = int(input())

print('Enter amount: ')

amount = int(input())

for x in range(amount):
    password = ''.join(random.sample(all, length))
    print(password)
