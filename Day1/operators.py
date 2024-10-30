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
