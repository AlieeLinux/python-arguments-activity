"""Part 1 — Basic Function Arguments
    1. Create a function named describe_pet that accepts two arguments:
        ◦ animal_type
        ◦ pet_name
    2. The function should print:
    3. I have a <animal_type> and its name is <pet_name>.
Task:
Call the function three times with different animals and names.

Part 2 — Positional vs Keyword Arguments
    1. Using the same function describe_pet, call it:
        ◦ Using positional arguments
        ◦ Using keyword arguments (reverse the order)
Example:
describe_pet("dog", "Buddy")             # positional  
describe_pet(pet_name="Milo", animal_type="cat")   # keyword  
"""

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} and its name is {pet_name}.")


# Part 1 execute
describe_pet("alligator", "kanye")
describe_pet("Snake", "python")
describe_pet("Tucano", "Reagan")

print()

# part 2 execute
describe_pet("Cat", "Tac")  
describe_pet(pet_name="God", animal_type="Dog")