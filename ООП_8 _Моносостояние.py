# существует для изменения всех значений экземпляров при изменении одного

class Cat:
    __shared_attr = {  # created dictionary
        'breed': 'pers',
        'color': 'black'
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr  # присвоили стандартному словарю созданный выше словарь
