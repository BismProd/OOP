#                                 # пример 1
# def main_func(name):
#
#     def inner_func():
#         print("Hello", name)
#
#     return inner_func
#
#
# r = main_func("ivan")
#
# l = main_func("oleh")
# r()
# l()

#                                # пример 2
# def adder(value):
#     def inner(a):
#         return value + a
#
#     return inner
#
#
# a2 = adder(2)
#
# print(a2(5))

#                               # пример 3
#
# def counter():
#     count = 0
#
#     def inner():
#         nonlocal count
#         count +=1
#         return count
#     return inner
#
#
# q = counter()
# print(q)  # python console for help
# print(q)

#                               # пример 4
# def average_nambers():
#     summa = 0
#     count = 0
#
#     def inner(number):
#         nonlocal summa
#         nonlocal count
#         summa += number
#         count += 1
#         return summa / count
#
#     return inner
#
# r1 = average_nambers()
# r1(10)
# r1(5)

#                              # пример 5
# from datetime import datetime
#
#
# def timer():
#     start = datetime.now()
#
#     def inner():
#         return datetime.now() - start
#
#     return inner

#                               # пример 6
# def add(a, b):
#     return a+b
#
#
# def counter(func):
#     count = 0
#
#     def inner(*args, **kwargs):
#         nonlocal count
#         count += 1
#         print(f"функция {func.__name__} вызывалась {count} раз")
#         return func(*args, **kwargs)
#
#     return inner
