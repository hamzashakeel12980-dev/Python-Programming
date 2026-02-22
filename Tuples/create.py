a = (10,20,30)
b = ()
print(type(a))
print(b)

# len
print(len(a))
#indexing
print(a[0])
print(a[1])
print(a[2])
# slicing
print(a[0:2])
print(a[1:3])
#max and min
print(max(a))
print(min(a))  
# concatenation
c = a + (40,50,60)
print(c)
# repetition
d = a * 2
print(d)
# membership
print(20 in a)
print(40 in a)
# unpacking
x,y,z = a
print(x)
print(y)
print(z)
