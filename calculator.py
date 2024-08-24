num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))

op=(input("enter operation:"))

if op=="+":
    print("Addtion of two nums are:",num1+num2)
elif op=="-":
    print("subtarction of two nums are:",num1-num2) 
elif op=="*":
    print("Multiplication of two nums are:",num1*num2) 
elif op=="/":
    print("Divison of two numbers are:",num1/num2)
elif op=="%":
    print("Module of two numbers are:",num1%num2)
else:
    print("Invalid operator")
print("-------ended------")        



