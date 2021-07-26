#input method
msg=input("Enter something: ")
print(msg)

#Enhanced code for input method
var="We want to greet you"
var +="\nEnter your name: "
name=input(var)
print(f"\n Hi, {name}")

#while loop
num=1
while num<=10:
    print(num)
    num+= 1

#while loop with input method
var="If you want to quit the enter quit: "
msg=" "

while msg != 'QUIT':
    print("\nTo quit type QUIT.")
    msg=input(msg)
    print(msg)