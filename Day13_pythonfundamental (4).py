# program to add 2 intgers 
#creating the function
def add():
    #taking input from user
    a= int(input("Enter the first value: ")) 
    b= int(input("Enter the second value: "))
    #starting the variable with '_' to suppress the warning
    # warning=" unused variable" 
    _c=a+b 
    print(f"Addition: {_c}")


#calling the function
add()
