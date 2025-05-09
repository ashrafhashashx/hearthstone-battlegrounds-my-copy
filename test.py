from random import randint

number_of_tries = 0

while True:
    x = randint(1,30)
    print(x)
    if x == 7:
        break
    else:
        number_of_tries = number_of_tries + 1
print(f'Number of tries = {number_of_tries}')