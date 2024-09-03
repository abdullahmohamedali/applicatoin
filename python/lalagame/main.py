import random

options = ("rock","paper","scicors")
player =None
computer = random.choice(options)

player = input("enter a choice (rock,paper,scicors):  ")
print(f"computer: {computer}")
print(f"player: {player}")