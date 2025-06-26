# creation of dictionary
d={}
print(type(d))

d={"name":"snehi","rollno":24,"grade":"A"}
print(d)
print(type(d))

# Accessing elements in dict:
d={"name":"pooji","rollno":64,"place":"kakinada"}
print(d)
print(d["name"])
print(d["rollno"])
print(d["place"])

# Accessing values by using get method:
d={"name":"vasavi","rollno":45,"place":"rjy"}
print(d.get("name"))
print(d.get("rollno"))
print(d.get("place"))

# modification of elements using assignment operator:
d={"name":"pooji","rollno":24,"place":"rjy"}
d["name"]="snehi"
print(d)
d["rollno"]=48
d["place"]="vizag"
print(d)

#using integer keys:
d=dict({1:"Apple",2:"raju"})
print(d)
print(d[1])
print(d[2])

