print("welcome to the adventure game your goul is to find a treasure chest\n")
qestoin = input("you are on a island you are hungry you need shelter go left or right? ").lower()

if qestoin == "left":
    q2 = input("ther is a cave would you like to enter or not? ")
    if q2 == "yes":
        q3 = input("there is a bear attack it or run away? ")      
        if q3 == "attack":
            print("the bear is storger you dead")
        if q3 == "run":
          q5 = input("you need a shelter build one out od wood or bricks or starw? ")
        if q5 == "wood" or "bricks":
            q7 = input("it is the next day serch for the chest in the beach or in the jungle? ")
            if q7 == "beach":
                print("you found a axe you are strong")
                q8 = input("there is a loin kill it or run away? ")
                if q8 == "kill it":
                    print("congratulation you killed the lion you ate its meat you make a sord ot of its bones you are even stronger and you found a secret door under it")
                    q9 = input("enter thhe secret door or not? ")
                    if q9 == "enter":
                        print("you founde the chest congratolaitions")
                    if q9 == "no":
                        print("there was a sbake it killed you")
                if q8 == "run":
                    print("the loin is faster it killed you")
            if q7 == "jungle":
                print("there was a tigger and killed you")
        else:
            print("a snake enterd and killed you")
    if q2 == "no":
        q5 = input("you need a shelter build one out od wood or bricks or starw? ")
        if q5 == "wood" or "bricks":
            q7 = input("it is the next day serch for the chest in the beach or in the jungle? ")
            if q7 == "beach":
                print("you found a axe you are strong")
                q8 = input("there is a loin kill it or run away? ")
                if q8 == "kill it":
                    print("congratulation you killed the lion you ate its meat you make a sord ot of its bones you are even stronger and you found a secret door under it")
                    q9 = input("enter thhe secret door or not? ")
                    if q9 == "enter":
                        print("you founde the chest congratolaitions")
                    if q9 == "no":
                        print("there was a sbake it killed you")
                if q8 == "run":
                    print("the loin is faster it killed you")
            if q7 == "jungle":
                print("there was a tigger and killed you")
        else:
            print("a snake enterd and killed you")

      

