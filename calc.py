class Calculator:
    def __init__(self):
        self.num1 = eval(input("enter first value"))
        self.num2 = eval(input("enter second value"))
    def sum(self):
        print(self.num1 + self.num2)
    def sub(self):
        print(self.num1 - self.num2)
    def mul(self):
        print(self.num1 * self.num2)
    def div(self):
        print(self.num1 / self.num2)

try:
    op = input('enter the operator:')
    obj = Calculator()

    if op == '+':
        obj.sum()
    elif op =='-':
        obj.sub()
    elif op =='*':
        obj.mul()
    elif op =='/':
        obj.div()
    else:
        print ("please dia enter valid operators")

except valueError as o:
    print("please Enter valid value")
    


