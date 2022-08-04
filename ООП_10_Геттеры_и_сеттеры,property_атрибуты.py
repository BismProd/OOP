class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance  # private atr

    def get_balance(self):
        print("get balance")
        return self.__balance

    def set_balance(self, value):
        print("set balance")
        if not isinstance(value, (int, float)):
            raise ValueError("Баланс должен быть числом")
        else:
            self.__balance = value

    def delete_balance(self):
        print("delete balance")
        del self.__balance

    balance = property(fget=get_balance,
                       fset=set_balance,
                       fdel=delete_balance)

    # a = BankAccount("Ivan", 300) /ввод значений
    #
    # a.balance /проверка значение
    #
    # a.balance = 400 /повторный ввод значения
    #
    # del a.balance /удаление значения