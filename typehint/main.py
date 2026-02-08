# def main():
#     print("Hello from typehint!")


# if __name__ == "__main__":
#     main()

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

user = User(name="Reza", age=25)
print(user.model_dump())