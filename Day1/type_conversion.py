# Python is dynamically-typed
# this means that datatypes can change during an application
# this type coercion or conversion happens implicitly in Python
# but may be called explicitly as well, on purpose
# each datatype, has its wrapper function with the same name

# conversion to boolean (bool)
# every datatype has its truthy and falsy values (convert to True or False)
# easier to remember the Falsy values, as most values as Truthy
# falsy values: None, False, 0, 0.0, 0j, "", (), [], {}
# truthy values: everything else
# note: empty collections in JS are truthy!

print("using bool() wrapper")
# numbers
print(bool(1))
print(bool(99))
print(bool(-99))
print(bool(0))

# strings
print(bool("hello"))
print(bool(""))

# containers
print(bool([1, 2, 3]))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(dict()))

# int()
print(int(True))
print(int(False))
print(int(1.0))
print(int(1.5))  # rounds to the nearest whole number

print("Using str wrapper:")
print(str(True))
print(str(False))
print(str(1.0))
print(str(1.5))

# can we convert list to set or tuple?
print(set([1, 2, 3]))
print(tuple([1, 2, 3]))
print(tuple([1, 2, 3, 4]))

# can we convert set to list or tuple?
print(list({1, 2, 3}))
print(tuple({1, 2, 3}))
print(tuple({1, 2, 3, 4}))
