#1. Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні операції з 2-ма числами, а саме додавання, віднімання,
# множення, ділення.
#   - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення
#   - Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.
#   - Додати документування в клас (можете почитати цю статтю: https://realpython.com/documenting-python-code/ )

class Calc():
    
    def __init__(self,a,b,last_result = None):
        self.a=a
        self.b=b
        self.last_result = last_result
    def add(self):
        self.last_result = self.a+self.b
        return self.last_result
    def mul(self):
        self.last_result = self.a*self.b
        return self.last_result
    def div(self):
        self.last_result = self.a/self.b
        return self.last_result
    def sub(self):
        self.last_result = self.a-self.b
        return self.last_result
      
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
obj=Calc(a,b)
choice=1

while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Last result")
    choice=int(input("Enter choice: "))
    if choice==1:
        print("Result: ",obj.add())
    elif choice==2:
        print("Result: ",obj.sub())
    elif choice==3:
        print("Result: ",obj.mul())
    elif choice==4:
        print("Result: ",round(obj.div(),2))
    elif choice==5:
        print("Last Result: ",round(obj.last_result))    
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
 