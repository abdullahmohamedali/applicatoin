b = int(input("how old are you? "))

x = 0 

if b <= 15:
    print("you can enter the site")

elif b >= 15 and b <= 18:
    x = input("do you have a id(y,n) ")

    if x == "n":
        print("you cant enter the site")
    elif x == "y":
        print("you can enter the site")
elif b > 18:

    v = input("do you have a licens?(y,n) ")

    if v == "n":
        print("you cant enter the site")

    if v == "y":
        print("you can enter the site")
    


