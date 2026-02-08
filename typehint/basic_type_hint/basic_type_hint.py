name_1 = "Reza"
name_2: str = "Aziza"
age: int = 14
phi: float = 3.14
is_student: bool = True

def sum(x: int, y: int) -> int:
    return x + y

def say_hello(name: str) -> str:
    return f"Hello {name}!"

data_1 = say_hello(name="Aziza")
data_2 = sum(5, 7)