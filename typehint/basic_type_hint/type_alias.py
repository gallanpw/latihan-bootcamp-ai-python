# Tanpa Alias
def get_user(id: int) -> tuple[str, int]:
    return ("Admin", 1)

# Dengan Alias (Lebih Jelas) Python 3.10+
from typing import TypeAlias

UserRecord_310: TypeAlias = tuple[str, int]

def get_user_310(id: int) -> UserRecord_310:
    return ("Admin", 1)

# Python 3.12+
type UserRecord_312 = tuple[str, int]

def get_user_312(id: int) -> UserRecord_312:
    return ("Admin", 1)


# bisa juga menggunakan Generik (Generic Types) TypeVar('T')
# Python 3.10+
from typing import TypeVar, TypeAlias, List
T = TypeVar('T')

# Alias Daftar[T] untuk daftar data yang tipenya fleksibel
# Cara ke 1
# perlu tambahan # type: ignore karena ada pengecekan dari vscode
Daftar_310: TypeAlias = list[T]
def fungsi_contoh_310(data: Daftar_310) -> T: # type: ignore
    return data[0]

# Cara ke 2
# perlu import List
def fungsi_contoh_310(data: List[T]) -> T:
    return data[0]


# Python 3.12+
# Tanpa from typing import TypeVar, TypeAlias
# Dan tanpa T = TypeVar('T')
# Alias Daftar[T] untuk daftar data yang tipenya fleksibel
type Daftar_312[T] = list[T]

def fungsi_contoh_312[T](data: Daftar_312[T]) -> T:
    return data[0]