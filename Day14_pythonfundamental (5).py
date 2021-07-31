#creating function for info of the pet
#adding the parameters as keyword here
def describe_pet(petname='lily',animaltype='cat'):#declaring the default argument at the end.
    print(f"I have a {animaltype}")
    print(f"my {animaltype}'s name is {petname}")


#caling the function without arguments
describe_pet()

#positional arguments
#calling the function with altered values
describe_pet('doggo','dog')

#calling the function with 1 argument and 1 default arguments 
describe_pet('rex')