#Creating the list
subjects=["phycis","chemistry","maths","statistics","biology","geology","it","electronics"]
print(subjects)
#Slicing 2 elements into one group
print(subjects[:2])
print(subjects[2:4])
print(subjects[4:6])
print(subjects[6:])
#pairing alternate elements
print(subjects[0:8:2])
# elements from reverse order
print(subjects[-1])
print(subjects[-2])
#starting the list in reverse order
print(subjects[::-1])
#reversing the string permenently 
subjects.reverse()
print(subjects)
