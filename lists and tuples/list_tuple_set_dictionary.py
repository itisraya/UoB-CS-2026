# ction of items stored in a particular order. Lists are mutable, meaning you can add, remove or change items after creating the list.
# Key features: Ordered, changeable, allows duplicate values, and supports indexing.


fruits = ["Apple", "Banana", "Mango", "Apple"]

print(fruits)
print(fruits[0])   # Apple
print(fruits[1])   # Banana

fruits[1] = "Orange"
fruits.append("Grapes")

print(fruits)

print(len(fruits))  # 5


# A tuple is similar to a list, but it is immutable. Once created, its elements cannot be changed, added or removed.
# Key features: Ordered, unchangeable, allows duplicates, and supports indexing.

colours = ("Red", "Green", "Blue", "Red")

print(colours)
print(colours[0])   # Red
print(colours[2])   # Blue

print(len(colours))


# A set is a collection of unique items. It automatically removes duplicate values.
# Unlike lists and tuples, sets are unordered and do not support indexing.
# Key features: No duplicates, no positional indexing, and items can be added or removed.

numbers = {10, 20, 30, 20, 10}

print(numbers)  # {10, 20, 30}
print(len(numbers))  # 3

numbers.add(40)
numbers.remove(20)

print(30 in numbers)  # True


# A dictionary stores information in key–value pairs. Each key identifies a corresponding value.
# Key features: Insertion-ordered, mutable, unique keys, and access by key rather than positional index.

student = {
    "name": "Ali",
    "age": 19,
    "course": "Computer Science",
    "mark": 85,
    "idontknow":"Tom"
}

print(student["name"])
print(student["mark"])

student["mark"] = 90
student["city"] = "Bristol"

print(student)