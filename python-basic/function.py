def say_hello():
    print("Hello!")

say_hello()
say_hello()
say_hello()

print("#########################################################\n")

def say_hello_2(name, country):
    print(f"Hello {name} from {country}!")

say_hello_2(name="Aziza", country="Indonesia")
say_hello_2(name="Ivan", country="Australia")
say_hello_2(name="Nove", country="Canada")
say_hello_2(country="Indonesia", name="Reza")

print("#########################################################\n")

students = [
    {"name": "Reza", "age": 16},
    {"name": "Jessy", "age": 25},
    {"name": "Nove", "age": 13},
]

def can_have_license(age):
    if age >= 18:
        print("You can have Driving License")
    else:
        print("You can't have Driving License")

for student in students:
    can_have_license(age=student.get("age", None))

print("#########################################################\n")

def say_hello_3(name):
    return f"Hello {name}"

hello = say_hello_3(name="Reza")
print(hello)

print("#########################################################\n")

def sum(x, y):
    return x + y

def sub(x, y):
    return x - y

result_sum = sum(x=5, y=3)
print(result_sum)
result_sub = sub(x=result_sum, y=2)
print(result_sub)