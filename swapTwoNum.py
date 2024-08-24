a=int(input("Give a:"))
b=int(input("Give b:"))

b+=a
a=b-a
b=b-a

print(f"value of A:{a}")
print(f"value of A:{b}")

