#Creating list
subjects=['physics','chemistry','maths']  
print(subjects)
#Printing an element from list
print(' \t',subjects[0])
#adding an element into list  
subjects.append('statistics')   
print(subjects)
#Adding an element to custom place
subjects.insert(3,'biology') 
print(subjects)
#Replacing an element
subjects[2]='C language'    
print(subjects)