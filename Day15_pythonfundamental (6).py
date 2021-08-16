#creating Class 
class Multiplecls(): 
    #note: writting Class in title case to remember
    var=" "
    # Here var is an attribute.
    #variable written inside the class is called as an attributes

    #Enhanced code
    def display(self): #self is temp placeholder for object
        print("started...")

    def addfn(self,value1,value2=2):# default arguments are defined at the end
        self.value1=value1
        self.value2=value2
        value3=value1+value2
        print(f"Multiple= {value3}")

           
#Creating object of Class Multiplecls
obj=Multiplecls()

#calling Method through object.
#oblect is an access to class methods
obj.display()
obj.addfn(10) #Values passed in an method are arguments.

