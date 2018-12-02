import random
n = random.randint(0,50)
on = ""
while True:
    number = input("Try to guess the number I chose between 0 and 50 ")
    number = int(number)
    if number == n:
        on = "Right"
        print(on)
        break
    elif number < n :
        on = "More"
        print(on)

    else :
        on = "Less"
        print(on)

