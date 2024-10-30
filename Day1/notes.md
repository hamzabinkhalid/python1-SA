9:30 Start

11:00 break am 20 mins

12:30 - 13:30 LUNCH

15:00 break pm

16:30 formal finish, QA

17:00 finish

alanl@stayahead.com

mobiles:

+353 85 105 2818
+44 7442 173078

In case of power outage

Code along
Intro, don't need to write

It came from Monty python not snakes, was a huge fan.

Object oriented language

OO languages:
Favour data encpsulation in object structures (in Python dictionary structure is akin to a literal object in other languages)

JS: object literal:
{ name: "Hamza"
age: 29
}

PY; dictionary:
{ name: "Hamza",
age: 29}

objects: key: value pairs, comma separated, enclosed in curly braces.


Functional programming:

Immutable data structures preferred, that cannot change in the same way the mutable objects can.

Think of OOP as "Save" = saves in place

Think of FP as "Save as" = save a new copy with changes

Neither of them are exclusive they play along together.

Python versioning:

Python was re-written between 2 and 3.
Strangely for a language that was a breaking change.
Code written on 2 will not run on 3.

Most of what we do hasn't changed since 3.5, but better to use latest version of python.

Once installed, runs two ways:
- 1. as REPL (Read, Evaluate, Print, Loop) - one line at a time, always useful as you code larger scripts to check syntax.
- 2. script more: write in an editor, save with the .py file extension, run in editor or from command line.

Implementation:
- We should not concern ourselves with it.
- CPython is interprated, i.e not compile time check for syntax error.

Editors:
- Pycharm, Spyder, Idle (after Eric Idle), used to ship with Python, Visual Studio (paid MS.net). VSCode (Opensource). IntelliJ IDEA, Webstorm, Eclipse, Sublime, Atom.

We use VSCode as it is fully featured and open source.

Documentation:
- Is recommended for people having experience in development.

W3schools.com, geeksforgeeks.org

Naming conventions:
- Variables and functions shouls be named snake_case.
- Classes should be named PascalCase (CamelCase)
- So, if you ever see a capital letter in Python, there should be a class definition
- It doesn't support constants, that may not be reassigned, they need to be written in SCREAMING_SNAKE_CASE
- Comments should be whole sentences, sentence case and should be terminated with full stop.

These are non mandatory but are BEST PRACTICES for readability, ignoring them would be non-pythoneque.

Indenting and line splitting:
- Denote code blocks
- Each line is terminated at new line
- Multiple statements can be written in one line, semi colon seperated, but should not, cause not typical

e.g. num1 = num2; num3 = num4

splits should happen if line exceeds 89 characters or before:

3 ways:
- technology_without_an_interesting_name = "TWAIN
- technology_without_an_interesting_name /
= "TWAIN
- {technology_without_an_interesting_name
 = "TWAIN}
- (technology_without_an_interesting_name
 = "TWAIN) // See walrus operator, probably most readable

