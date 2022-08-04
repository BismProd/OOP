# self - затычка обозначающая метод

class Cat:
    breed = "pers"

    def show_breed(self):
        print(f"my breed is {self.breed}")

    def show_name(self):
        if hasattr(self, 'name'):
            print(f"my name is {self.name}")
        else:
            print("nothing")

    def set_value(self, name = "stray", age = 0):
        self.name = name
        self.age = age

