# a=[1,23,21,45,7,45,78,2,3,4,4.001,3]
# print(a[-1][2])

# a.append("last element")
# a.insert(1,123)
# a.remove(3)
# a.pop(0)
# a.sort()
# a.reverse()
# a.index(7)

# a.sort()
# a.reverse()
# a[0]=100
# print(a)


# Tuple

# a=(1,2,3,"apple","orange")
# a[0]=10
# print(a[0])

# Set 

# s1=[1,2,3,4,3,5,6,7,3]
# s2={32,21,45,324,561,2,3}
# print(s1.difference(s2))
# print(set(s1))

# Dict 

# d1={
#     'a':"Apple",
#     'b':"Ball",
#     'c':"Cat",
#     'd':"Duck",
#     'e':"Elephant",
#     1:"One"
# }

# print(d1.keys())
# print(d1.values())
# print(d1.items())
# d1['c']="Car"
# print(d1)


list1=[2,3,23,45,34,54,67,45,6,6,7,8,1,1,2,3,2,3,5]
print(list(set(list1)))