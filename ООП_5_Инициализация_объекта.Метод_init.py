# init = инициализация будущего обьекта

class Cat:

    def __init__(self, name, breed="pers", age=1, color="white" ):
        print('hello new object', self, name, breed, age, color)
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color