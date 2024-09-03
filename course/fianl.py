v = int(input("what is the number? "))
flag = False
if v > 1:
    for i in range(2, v):
        if (v % i) == 0:
            flag = True
    if flag:
        print(v,"is not a prime number")
    else:
        print(v,"is a prime number")
else:
    print(f"{v} is not a prime number")

