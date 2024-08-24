# list=[10,20,30,40,50]
# sum=0
# for i in list:
#     sum+=i
# print(sum)    

# um=0
# length=len(list)
# for i in range(0,length):
#     um+=list[i]
# print(um)  

# while i>len(list):
#     sum+=i
#     i+=1
# print(sum)    

#to find th sum of numbrs

li=[10,20,30,40,50,60]
sum=0
for i in li:
    sum=sum+i
print(sum)

um=0
for i in range(0,len(li)):
    um=um+li[i]
print(um)

while i>len(li):
    sum+=i
    i+=1
print(sum)    

max=li[0]
min=li[0]

for i in li:
    if i>max:
        max=i
    if i<min:
        min=i   
print(max,min)     


list1=[10,20,30,20,40,10,50]

# for i in list1:
#     print(i)
#     if 

#to find factorail

n=5
s=1

for i in range(1,n+1):
    s=s*i
print(s)   


