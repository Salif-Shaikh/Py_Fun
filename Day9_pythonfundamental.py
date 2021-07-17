#Creating tuple datatype
cars =("suzuki","toyota","hyundai")
print(type(cars))
#Using for loop for tuple
for i in cars:
    print(i.title())
    print(i.upper())
    pass
#Creating Dictionary datatype
human ={"hands":2,"legs":2,"head":1}
print(type(human))
print(human)
print(human["hands"])
#Adding an element to Dictionary
human["eyes"]=2
print(human)
#Using for loop for Dictionary
for x in human:
    print(x.title())
    pass 