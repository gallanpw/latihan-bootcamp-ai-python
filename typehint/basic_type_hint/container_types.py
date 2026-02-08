# Cara lama
from typing import List, Dict, Tuple, Set, Optional

names: List[str] = ["Reza", "Jessy", "Joe"]
scores: Dict[str, int] = {"Reza": 95, "Jessy": 87}
coordinates: Tuple[float, float] = (10.5, 20.3)
unique_ids: Set[int] = {1, 2, 3, 4}

def example_function(value: Optional[str]) -> Optional[str]:
    if value is not None:
        print(f"Received: {value}")
    else:
        print("Received None")
    return value

# Cara baru Python 3.10+
# tanpa menginisiasi typing dan import List, Dict, Tuple, Set, Optional
# gunakan dengan huruf kecil seperti list, dict, tuple, set

names: list[str] = ["Reza", "Jessy", "Joe"]
scores: dict[str, int] = {"Reza": 95, "Jessy": 87}
coordinates: tuple[float, float] = (10.5, 20.3)
unique_ids: set[int] = {1, 2, 3, 4}

def example_function_310(value: str | None) -> str | None:
    if value is not None:
        print(f"Received: {value}")
    else:
        print("Received None")
    return value

# Using str | None is equivalent to Optional[str]