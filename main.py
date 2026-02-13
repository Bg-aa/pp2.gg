class User:
    def __init__(self, name, country="Kazakhstan"):
        self.name = name
        self.country = country

u1 = User("Bagdat")
print(u1.country)
