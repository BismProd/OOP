class BankAccount:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    # def print_public_data(self):
    #     print(self.name, self.balance, self.passport)  # without any underscore /можно вызывать напрямую мне класса

    def print_public_data(self):
        self.__print_private_data() # вызываем инкапсулиемый метод внутри класса
    #
    # def print_protected_data(self):
    #     print(self._name, self._balance, self._passport)  # with one _ /можно вызывать напрямую вне класса с добавлением одного подчеркивания

    def __print_private_data(self): # инкапсулируем сам метод
        print(self.__name, self.__balance, self.__passport)  # with two __ / нельзя вызывать напрямую вне класса, только при помощи метода(инкапсуляция)


account1 = BankAccount("Bob", 1000, 12345678)
account1.print_public_data()  # call private method inside public method
print(dir(account1))  # look at all directories
account1._BankAccount__print_private_data()  # call data from ↑
account1.__print_private_data()  # tried to call private method
print(account1.name)  # tried to call public
print(account1._balance)  # tried to call protected
print(account1.__passport)  # tried to call private
