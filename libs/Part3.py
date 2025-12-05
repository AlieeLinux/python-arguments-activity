"""
Part 3 — Default Arguments
    1. Modify the function to include a default value:
def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} and its name is {pet_name}.")
Tasks:
    • Call describe_pet("Brownie")
    • Call describe_pet("Nugget", "chicken")
"""

def describe_pet(animal_type, pet_name="dog"):
    print(f"I have a {animal_type} and its name is {pet_name}.")

describe_pet("Brownie")
describe_pet("Nugget", "chicken")