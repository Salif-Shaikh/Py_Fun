#Creating a dictionary
human={"head":1, "hands":2, "legs":2, "fingers":10}
#Adding an element to a dictionary
human["eyes"]=2
human["nose"]=1
human["mouth"]=1  
human["ears"]=2
#printing the sorted dictionary
print(sorted(human))
#validating the datatype
print(type(human))
#for loop for dictionary
for i,j in human.items():
    #enhancing code
    print(f"key  : {i.title()}")   
    print(f"value: {j}\n")
