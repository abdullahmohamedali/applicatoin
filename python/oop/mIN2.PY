class food:
    
    def __init__(self, name):


        
        self.name = name

        print(f"{self.name} Is created From main base")

    def eat(self):

        print("Eat Method From base class")

class apple(food):

    def __init__(self):
        
        print("apple is created from derived classe") 
food_1 = food("pizza")
food_two = apple()
food_two.eat()