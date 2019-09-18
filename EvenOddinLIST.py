l = [1,2,42,4,6,98,453,13]
env = list()
odd = list()

#check even odd from the list of integers
for i in l :
    if i % 2 == 0 :
        env.append(i)
    else:
        odd.append(i)
print('The Even nu,bers are : ',env)
print('The list of odd number are : ',odd)

#element at a particular position
print(l.index(42))

#count the number of time the element occurred
print(l.count(2))

#copy a list into list
v = (l.copy())

#check the addr of same list got by copy() is different
print(l,id(l),'\n',v,id(v))


#elements same , but id different
if l == v :
    print('t')

#pop index
print(l,l.pop(5),l)

#remove
l.remove(453)
print(l)

#reverse the list
l.reverse()
print(l)

#sort
l.sort()
print(l)

#sort desc
l.sort(reverse=True)
print(l)

l1 = []
l1.extend(l)
print(l1)
print(l)
