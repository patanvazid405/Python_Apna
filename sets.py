#sets

set={1,2,3,4}
fruit={'apple','banna','grape'}
print(type(fruit))
fruit.add('orange')
fruit.remove('apple')
print(fruit)

fruit.pop()

#set operations
set1={1,2,3,4}
set2={6,5,4,2,1}
#union
all=set1.union(set2) #prints all
print(all)
#intersection
inter=set1.intersection(set2)
print(inter)
#diffrence
dif=set2.difference(set1)
print(dif)
#symmetric differnce
symm=set2.symmetric_difference(set1)
print(symm)

#membership and length
print(2 in set1)
print(len(set1))


idx={12,3,6,42}
print(idx.pop())
print(idx.update("12","1"))
print(idx.pop())
print(idx)

