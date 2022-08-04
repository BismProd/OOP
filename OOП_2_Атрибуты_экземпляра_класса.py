# lesson with attributes of class instance/ урок с атрибутами экземпляра класса

class Car:
    model = "BMW"
    engine = 1.6


a1 = Car()  # create class instance
a2 = Car()

a1.seat = 4  # add attribute to instance a1 of class Car
a1.model = "FIAT"

Car.r = 100  # add attribute directly to class

del a1.model  # delete value of model in a1, but not in Car
if __name__ == "__main__":
    print(Car.__dict__)  # show all attribute
    print(a1.__dict__)  # show attributes a1
    print(a2.__dict__)  # show attributes a1
    print("request for class Car, atr engine in a1 =", a1.engine)
    print("request value from class, because we are delete value in instance/ model a1 = ", a1.model)
