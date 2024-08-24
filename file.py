
f=open("demo.txt","r")
data=f.read()
print(data)
f.close()




F=open("file.txt","w")
mat=F.write("hello chinna")
print(mat)


prac=open("practise.txt","w+")
list=prac.write("Hi everyone /n We are learning filei/o /n")
print(list)

with open ("hello.txt","w+") as k:
    k.write("hello vazid\n hello developer")
    
print(k)