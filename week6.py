#first_problem
numbers = [3,7,2,9,4,1,8]
numbers.append(5)
numbers.remove(9)
numbers.sort()
numbers.reverse()
numbers.insert(2,6)
numbers.index(4)
print(numbers)

#second_problem
my_tuple = (15, "Python", 3.14, True, 42, False)
print(my_tuple.index("Python"))
print(my_tuple)
print(my_tuple.count(True))
print(my_tuple[1:5])

#third_problem
students = {
    "Alex": 85,
    "Olivia": 92,
    "Daniel": 76,
    "Sophia": 88,
    "James": 67,
    "Emma": 95,
    "Liam": 81,
    "Mia": 73,
    "Noah": 90,
    "Ava": 84,
    "Ethan": 59,
    "Isabella": 97,
    "Lucas": 71,
    "Amelia": 86,
    "Oliver": 64,
    "Grace": 78
}


students["Frank"]="60"
print(students)