# class Person:
#     def __init__(self, name):
#         self.__name = name
#         self.__age = 1

#     @property 
#     def age(self):
#         return self.__age
    
#     @age.setter
#     def age(self, age):
#         if 1 < age < 110:
#             self.__age =  age 
#         else:
#             print("Недопустимый возраст")
    
#     @property
#     def name(self):
#         return self.__name

#     def display_info(self):
#         print(f'Имя: {self.__name}\tВозраст: {self.__age}')

# tom = Person("Tom")

# tom.display_info()
# tom.age = -3456
# print(tom.age)
# tom.age = 36
# tom.display_info()

class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    def display_info(self):
        print(f"Name: {self.__name}")

class Employee(Person):
    
    def work(self):
        print(f"{self.name} works")

tom = Employee("Tom")
print(tom.name)
tom.display_info()
tom.work()


