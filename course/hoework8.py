x = int(input("what is the number? "))
f =0
for i in range(x):
    if i % 5 == 0 and x % 3 ==0:
        f = "fizzbuzz"
        print(f)
        continue
    if i % 5 == 0:
        f = "fizz"
        print(f)
        continue
    if i % 3 ==0:
        f = "buzz"
        print(f)
        continue
    else:
        print(i)
        



    