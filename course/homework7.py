number = int(input("what is the number? "))

if number % 5 == 0 and number % 3 ==0:
    print("!")
elif number % 5 == 0:
    print("*")
elif number % 3 ==0:
    print("#")