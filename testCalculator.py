from mymodule import Calculator
import string
option=0
try:
    print("Enter 1.Add 2.Subtract 3.Multiply 4.Divide")
    option = int(input("Enter your option: "))
    if(option==1):
        input1=int(input("Enter a number: "))
        input2 =int(input("Enter a number: "))
        c1 = Calculator(input1,input2)
        print(c1.add())
    if(option==2):
        input1=float(input("Enter a number: "))
        input2 = float(input("Enter a number: "))
        c1 = Calculator(input1,input2)
        print(c1.sub())
    if(option==3):
        input1=float(input("Enter a number: "))
        input2 = float(input("Enter a number: "))
        c1 = Calculator(input1,input2)
        print(c1.mul())
    if(option==4):
        input1=float(input("Enter a number: "))
        input2 = float(input("Enter a number: "))
        c1 = Calculator(input1,input2)
        print(c1.div())
except ValueError as e:
    print("Enter valid option")

