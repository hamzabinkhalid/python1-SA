# the standard, built-in data types in python
# literal, or single values, OR expressions that evaluate to them
# IMMUTABLE by default

# bool. or boolean
# values: True or False
# IMMUTABLE type

my_bool = True
my_bool = False
# a re-assignment of the same reference, NOT a mutation of value

# tuples, are immutable, but can update the reference of a whole tuple variable as whole, not the individual elements
# when don't want the data to be changed, or returning from a function
my_tuple = (1, 2, 3)

my_tuple = (4, 5, 6)

# sets, elements can be of any type, elements are not ordered, they don't allow duplicates, powerful for examining differences and similarities
my_set = {1,2,2,3,4,5,5}
# print(my_set) //{1, 2, 3, 4, 5}

print(bool(-1))

# dict (dictionary)
# values: key: value pairs
# keys: may be of any type, commonly strings
# keys must be unique
# values: may be of any type and may be duplicated
# mutable
# note: a python dict is not same as an object
# even though they both print out with curly brances and key: value pairs
# objects are made by classes
# the way we drill down into properties is different in objects and dicts
# theoracitcally everything is an object in python

my_dict = {"name": "Hamza", "age": 22, "employed": True}
print(my_dict)

# None type
my_none = None
print(type(my_none))
# means the reference associated with it points nowhere
# if it did reference any of the other types, it doesn't any more
# null, in other languages