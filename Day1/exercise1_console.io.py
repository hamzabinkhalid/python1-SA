your_name = input("Enter your name: ")

your_age = input("Enter your age: ")

your_age = int(your_age)  # coerce age to int

print(your_name + " is " + str(your_age + 1)
      + " years old next year.")  # Python2 old school

# Placeholders, Python 3
print("{} is {} years old next year.".format(your_name, your_age + 1))

# Placeholders, Python 3.5 >
print(f"{your_name} is {your_age + 1} years old next year.")

# Placeholders, Python 3.67 >, """ preserves newlines
print(f"""{your_name} is
{your_age + 1}
years old next year.""")
