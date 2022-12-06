def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def multiply(x,y):
    print(x*y)
def divide(x,y):
    print(x/y)


print("OPTIONS \n1.Add\n2.Subtract\n3.Multiply\n4.Divide")









while True:
    p=input("Choose your option:")

    if p in('1','2','3','4'):
        x=int(input("Enter your first number:"))
        y=int(input("Enter your second number:"))
        

        if p=='1':
            add(x,y)
        elif p=='2':
            sub(x,y)
        elif p=='3':
            multiply(x,y)
        elif p=='4':
            divide(x,y)
        break












