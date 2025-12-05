from libs import part5, part_1_and_2, Part3, Part4

# Part 1 execute
part_1_and_2.describe_pet("alligator", "kanye")
part_1_and_2.describe_pet("Snake", "python")
part_1_and_2.describe_pet("Tucano", "Reagan")

# Separator
print("\n", "#"*80, "\n")

# part 2 execute
part_1_and_2.describe_pet("Cat", "Tac")  
part_1_and_2.describe_pet(pet_name="God", animal_type="Dog")

print("\n", "#"*80, "\n")

# PArt 3 execute
Part3.describe_pet("Brownie")
Part3.describe_pet("Nugget", "chicken")

print("\n", "#"*80, "\n")

# part 4 execute
Part4.Order("water")
Part4.Order("hot chocolate", "large")
Part4.Order("milk tea", "small", iced=True)

print("\n", "#"*80, "\n")

# PArt 5 execute
# Printing it to make it work
x = part5.compute("add", 5, 10)
y = part5.compute("multiply", num1=3, num2=4)
z = part5.compute("subtract", 20)
a = part5.compute("Hello world", 1)

print(x)
print(y)
print(z)
print(a)