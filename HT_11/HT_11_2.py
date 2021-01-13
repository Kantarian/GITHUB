#2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів, які зберігатиме в відповідні змінні. Методи, які повинні бути в класі 
#Person - show_age, print_name, show_all_information.
#   - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.


class Person:

    def __init__(self, name, surname, age, address, telephone, email, profession = None):
        self.name = name
        self.surname = surname

        self.age = age

        self.address = address
        self.telephone = telephone
        self.email = email
        self.profession = profession

    def show_age(self):
        print(f'Age: {self.age}')      

    def print_name(self):
        print(f'Name: {self.name}, Surname: {self.surname}')
    
    def show_all(self):
        if self.profession:
            print(f'''
        Name: {self.name}, 
        Surname: {self.surname},
        Age: {self.age},
        address: {self.address}, 
        telephone: {self.telephone}, 
        email: {self.email},
        profession: {self.profession}
            ''')
        else:
            print(f'''
        Name: {self.name}, 
        Surname: {self.surname},
        Age: {self.age},
        address: {self.address}, 
        telephone: {self.telephone}, 
        email: {self.email},
        ''')

           

    



person_1 = Person(
    "Yehor",
    "Horbatko",
    '26',
    "No. 12 Usinskogo, Kyev",
    "+380505202994",
    "dog380973292312@gmail.com",
    "Chemist"
)


print(person_1.show_age())
print(person_1.print_name())
print(person_1.show_all())


person_2 = Person(
    "asd",
    "Horbdsaatko",
    '226',
    "No. 12 Usinsksadsaogo, Kyewev",
    "+38050522342302994",
    "do2@gmail.com",
    "Aba"
)


print(person_2.show_age())
print(person_2.print_name())
print(person_2.show_all())