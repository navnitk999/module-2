
import random
again = True
while again:
    print(random.randit(1,6))
    another_roll=input("wnat to roll the dice again (y/n):")
    if another_roll.lower() == "y":
        continue
    else:
        break
