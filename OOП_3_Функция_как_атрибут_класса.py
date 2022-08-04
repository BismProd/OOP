class Car:
    model = "BMW"
    engine = 1.6

    @staticmethod  # idk whatisit
    def drive():  # function as attribute of class
        print("Go man")


a = Car()

Car.drive()  # call f drive inside class
a.drive()  # call drive inside instance of class
