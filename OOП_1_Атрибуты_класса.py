# lesson with attribute of class / действия над атрибутами класса тут и ниже

class Person:  # add new class
    name = "Ivan"  # add attribute
    age = 30  # add attribute


# Класс.названиеАтрибута - стандартный шаблон обращения к атрибуту класса
Person.name = "Oleh"  # change attribute`s value
Person.x = 10  # add new attribute
setattr(Person, "y", 200)  # add new attribute / set attribute
del Person.x  # delete exist attribute
delattr(Person, "y") # also delete exist attribute

if __name__ == "__main__":
    print(getattr(Person, "name", 100))  # value identity check
    print(Person.__dict__)  # call all attribute

# добавления атрибутов классам влияет на добавленные атрибуты екземпляров

