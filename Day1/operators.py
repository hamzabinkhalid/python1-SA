# an expression involves operators and operands
# an operand is a value or a variable
# an operator is a symbol that performs an action
# an expression is a combination of operators and operands
# an expression evaluates to a single value

# arithmatic operators
# +, -, *,
# / (division),
# % (modulus),
# // (floor division) e.g. 5//2 = 2,
# ** (exponent)

print(10 / 3)  # 5.0
print(10 // 3)  # 3
print(10 % 3)  # 1
print(10 ** 3)  # 1000
# IEEE 754, something has to do with converting to binary and converting back
# to integer
# we should not use float values where accuracy is of primary concern

# promotion
# the act of storing smaller data type in a larger data type

print(1 + 1.0)  # 2.0

# non-numeric arithmatic
print("ho" * 3)  # hohoho

# assignment operators
# =, +=, -=, *=, /=, %=, **=, //=
my_num = 1
my_num += 1
my_num += 1
print(my_num)  # 3

my_string = ""
my_string += "I"
my_string += " am"
my_string += " learning"
print(my_string)  # I am learning
# note, this way of building string is expensive, when long strings
# are involved
# other methods see https://www.tracedynamics.com/python-string-builder/

# walrus operator := assigns and returns at the same time
# before walrus
x = 1
print(x)  # 1
# print(x = 2)  # TypeError: 'x' is an invalid keyword argument for print()

# with walrus
print(y := 1)  # 2, assigns and returns in the same line

# Increment and decrement operators do not exist in Python e.g. ++, --

# Multiple assignment
x, y, z = 1, 2, 3
# better than x = 1, y = 2, z = 3
print(x, y, z)  # 1 2 3

# dict
my_dict = {"name": "alan", "age": 2}
name, age = my_dict["name"], my_dict["age"]
# NOTE: square brackets notation for dict props
print(name, age)  # alan 2

# list
my_nums = [1, 2, 3]
first, second, third = my_nums[0], my_nums[1], my_nums[2]

# assignment operator chaining (more specialised, avoid writing if possible)
x = 1
y = 1
# may be rewritten as
x = y = 1
print(x, y)  # 1 1

# comparison operators
# ==, !=, >, <, >=, <=
# is, tests for IDENTITY: reference the same object as the other
# examples of comparison operators:
print(1 == 1)  # True
print(1 == 2)  # False
print(1 != 1)  # False
print(1 != 2)  # True
print(1 > 1)  # False
print(1 < 1)  # False
print(1 >= 1)  # True
print(1 <= 1)  # True
print(1 >= 2)  # False
print(1 <= 2)  # True
# note: not is a keyword, not a function
print(1 is 1)  # True
print(1 is not 1)  # False

# misc.
x = y = 1
print(x, y)
y = 2
print(x, y)

my_list = [1, 2, 3]
my_other_list = [1, 2, 3]
my_copied_list = my_list
print(my_list is my_other_list)  # False
print(my_list is my_copied_list)  # True

# the system python uses to determine if two variables reference the same object is built-in function id()
print(id(my_list))  # 140732135058432
print(id(my_copied_list))  # 140732135058432
print(id(my_other_list))  # 140732135058432

# because the copy copies the reference it is calle3d a SHALLOW copy
# the original may be mutated through the new reference
my_copied_list.append(4)
print(my_list)  # [1, 2, 3, 4]
print(my_copied_list)  # [1, 2, 3, 4]

# way to go around it
import copy
my_deep_copied_list = copy.deepcopy(my_list)
my_deep_copied_list.append(5)
print(my_list)  # [1, 2, 3, 4] the original is unaffected
print(my_deep_copied_list)  # [1, 2, 3, 4, 5]
