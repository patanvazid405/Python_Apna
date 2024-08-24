# inp=input("Enter the word:")

# inp=inp.lower()
# a=inp.count("a")
# e=inp.count("e")
# i=inp.count("i")
# o=inp.count("o")
# u=inp.count("u")
# print(f"Vowels are:{a+e+i+o+u}")

math=int(input("Enter Math marks:"))
sci=int(input("Enter Science marks:"))
eng=int(input("Enter English marks:"))

Total_marks=math+sci+eng
Avg_marks=int(Total_marks/3)

if Avg_marks>=90:
    print("You got A")
elif Avg_marks>=80:
    print("You got B")
elif Avg_marks>=70:
    print("You got C") 
else :
    print("You got F") 

print("Total marks are:",Total_marks)
print("Avg marks are:",Avg_marks)


# stri=input("enter the string:")
# reverse=stri[::-1]

# if reverse==stri:
#     print("it is a plaindrome")
# else:
#     print("It is not a palindrome")

#    finding largest number\
          
# num=input("Enter numbers:")

# x,y,z=num.split(",")
# num1=int(x)
# num2=int(y)
# num3=int(z)
# great=""

# if num2>num1:
#     if num2>num3:
#         great=num2
#     else:
#         great=num3
# elif num1>num2:
#     if num1>num3:
#         great=num1
#     else:
#         great=num2 

# print(great)         

# year=input("Enter the year:")

# if year%4==0:
#     if year%100==0:
#         print(f"Print{year} is an leap year")

# print(year)        




