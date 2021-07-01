#Removing Whitespaces from a string
word="        python1"
print(word.lstrip())
word="python2             " #altering the value
print(word.rstrip())
word="          python3        "
print(word.strip())
#Using \t tabdelimiter
word="lanugages:\n\tpython\n\tC++\n\tjava"
print(word)