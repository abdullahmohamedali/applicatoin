class member:

    not_allowed_names = ["blalala"]

    def __init__(self, first_name, password, email, gender):
        
        self.name = first_name
        self.password = password
        self.email = email
        self.gender = gender
    def full(self):
        if self.name == member.not_allowed_names:
            raise ValueError("name no alowed")

        else:

            return f"{self.name} {self.password} {self.email}"
    
    def name_with_title(self):
        if self.gender == "boy":
            return f"hello mr {self.name}"
        elif self.gender == "girl":
            return f"hello miss {self.name}"
        else:
            return f"hello {self.name}"
    
    
admin_one = member("abdullah", "12345678", "blala@gmail.com", "boy")
m1 = member("seif","12345678", "blala@gmail.com", "boy")
m2 = member("mona","12345678", "blala@gmail.com", "girl")


print(admin_one.full())
print(admin_one.name_with_title())




