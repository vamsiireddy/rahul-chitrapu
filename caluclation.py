num1=int(input("enter the number1 : "))
num2=int(input("enter the number2 : "))
op=input("enter the operator : ")
if op =="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op == "*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else :
    print("unknown operation")