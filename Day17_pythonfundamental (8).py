#req:- Create a class and its constructor
#creating a class called cat

class cat():
    '''creating the constructor'''
    def __init__(self,name,age):
        #Here __init__ is the constructor
        self.name = name 
        self.age = age
        print("Constructor is called the moment the object of the class is created.")
        #we don't need to call the Fn for the method executionw

    def details(self):
        print(f"{self.name} is a cat.")
        print(f"{self.name} is {self.age} year old.")

    
#Creating the object for class cat
paw=cat('tom',1) 
#we can pass the argument while assigning the objects

#calling the method
paw.details()
#This is also called as call by reference 
#here we are calling the method by reference