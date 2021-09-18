#This is to show the Exception handling
try:
    with open('file1.txt') as file_obj:
        content = file_obj.read()
    print(content)

except FileNotFoundError:
    print("An ERROR occurred")