# # # set is an collection of unordered elements which is iterable and mutable...set elements cannot be accessed
# # # by using index becuase they are unordered...set use curly braces{}...
# # # ex: s={}
# # # s={1,2,3,4,5}

# # s={}
# # print(type(s))

# # s1={1,2,3,4,5}
# # print(type(s1))

# # # set elements can be accessed by using for loop:
# # s={1,2,3,4,5}
# # for i in s:
# #     print(i)

# # s=set()
# # print(s)
# # print(type(s)) 

# # # creation of set with mutliple elements:
# # s={1,2,3,4,(5,6),7,8}
# # print(s)
# # print(type(s))


# # s={1,2,3,(4,5),6,7,8}
# # for i in s:
# #     print(i,end="")
# #     print(type(s))

# # # creation of set with hetrogeneous elements:
# # s1={20,"poojitha",85.6,True}
# # print(s1)
# # print(type(s1))

# # creation of list elemts in to set elements:
# # l=[1,2,3,4,5]
# # s=set(l)
# # print(l)
# # print(type(l))
# # print(s)
# # print(type(s))

# # print(type(l))
#  # creation of set from range:
# # s=set(range(1,11))
# # print(s)

# # creation of set from string:
# # name="Rama Lakshmi"
# # s=set(name)
# # print(name)
# # print(type(name))
# # print(s)
# # print(type(s))

# # creation of set from tuple:
# # t=(1,2,3,4,5)
# # s=set(t)
# # print(t)
# # print(type(t))
# # print(s)
# # print(type(s))
# # membership operator in set:
# # s={1,2,3,4,5,6}
# # print(5 in s)
# # print(6 not in s)
# # print(9 not in s)

# # Accessin elements by using iteration for loop:
# # s={1,2,3,4,5,6,7,8,9}
# # for i in s:
# #     print(i,end="")


# # methods in set:
# # 1. Add method()
# # s={1,2,3,4,5,6}
# # print(s.add(7))
# # print(s)
# # print(s.add(-2))
# # print(s)
# # print(s.add("snehi"))
# # print(s)

# # s={10,20,30,40}
# # t=(1,2.3)
# # print(s.add(t))
# # print(s)
# # print(type(s))

# # s={1,2,3,}# we cannot add list to set because it is immutable
# # l=[6,7,8]
# # print(s.add(l))
# # print(s)

# # 2.pop method(): # first element can be removed from set
# # s={1,2,3,4,5,6}
# # print(s.pop())
# # print(s)

# # # 3. remove method():
# # s={10,20,30,40,50,60}
# # print(s.remove(20))
# # print(s)

# # 4. Discard method():
# # discard method removes the element from set and it does not gives any error if we given
# # an element not there in list
# # s={1,2,3,4,5}
# # print(s.discard(1))
# # print(s)
# # print(s.discard(7))
# # print(s)

# # 5. clear method():It removes all elements in set
# # s={1,2,3,4,5}
# # print(s.clear())
# # print(s)


# # 6.copy method(): it copies elements from one set to another set
# # s={10,20,30,40}
# # a=s.copy()
# # print(a)

# # 7.union method: It combines the two sets 
# # s1={"red", "pink","skyblue"}
# # s2={"black","orange"}
# # print(s1.union(s2))

# # # 8.update method(): it will update .before set
# # s1={1,2,3,4,5}
# # s2={6,7,8}
# # print(s1.union(s2))
# # print(s1)
# # print(s1.update(s2))
# # print(s1)

# # 9.difference method(): It returns only s1 elements not s2 elements and common elements
# # s1={1,2,3,4,5}
# # s2={4,5,6,7,8}
# # print(s1.difference(s2))

# # # 10. symmetric difference method(): It returns s1 and s2 elements not common elements
# # s1={10,20,30,40,50}
# # s2={40,50,60,70,80}
# # print(s1.symmetric_difference(s2))

# # 11. superset and subset:
# s1={1,2,3,4,5,6,7,8}
# s2={3,4,5}
# print(s1.issuperset(s2))
# print(s2.issubset(s1))
# print(s2.issuperset(s1))
# print(s1.issubset(s2))

# # 12. Isdisjiont:
# s1={1,2,3,4,5}
# s2={3,4}
# print(s1.isdisjoint(s2))

# s1={1,2,3,4,5}
# s2={6,7,8}
# print(s1.isdisjoint(s2))

# s={"pooji"}
# s={ i[0] for i in s}
# print(s)

#frozenset: frozenset is same as set but it is immutable, thats why we cannot perform modifying operations
s1={1,2,3,4,5}
fs=frozenset(s1)
print(fs)
print(type(fs))

# In frozenset we cannot add or remove:
s1={1,2,3,4,5}
fs=frozenset(s1)
print(fs)
print(fs.add(20))
print(fs)
print(fs.remove(1))
print(fs)