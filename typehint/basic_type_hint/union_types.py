# Cara lama
from typing import Union

def process_id(user_id: Union[int, str]) -> str:
    return str(user_id)

# Cara baru Python 3.10+
# tanpa menginisiasi typing dan import Union

def process_id_310(user_id: int | str) -> str:
    return str(user_id)