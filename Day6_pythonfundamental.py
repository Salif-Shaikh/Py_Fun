car =["Bmw","Audi","Mercedes","Lamborghini","Ferrari","Porche","Buggati","Mclaren"]
print(car)
#Arranging the list in order temp
print(sorted(car))
#Arranging the list in order perm
car.sort()
print(car)
#Deleting an element from the list 
del car[5]
print(car)
#Temp deleting an element 
x=car.pop(2)
print(car)
print(x)
print(len(car))