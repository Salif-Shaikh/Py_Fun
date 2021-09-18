#req:- 2 objects for a single class
#Creating a class
class dog():
    '''creating methods related to dog'''

    def detail(self,name,age): #detail of the dog like Name and age.
        '''Here self is an temp placeholder for object'''
        self.name = name #Taking name as argument in Fn call
        self.age = age #Taking age as argument in Fn call
        print(name , age)

    def jump(self):
        #Here we are calling the variable by reference
        print(f"{self.name} is now jumping.")

    def belong(self):
        print(f"{self.name} is {self.age} years old. And {self.name} belong to kim jennie")
        '''we can use the same variable for numbers of time'''



#Creating the object for class dog
tail=dog()

#calling the methods with tail object
print("\n")
tail.detail('luca',2) #pass the value for the variable in string form.
tail.jump()
tail.belong()
print("\n")

#crearting the second object for class dog
obj=dog()

#calling the method with obj object
obj.detail('kai',3)
obj.jump()
obj.belong()

