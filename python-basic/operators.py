# Arithmetic
first_number = 2
second_number = 3
sum_result = first_number + second_number
print(sum_result)

# Comparison -> Return dari Comp. selalu Boolean (True/False)
is_equal = first_number == second_number
is_not_equal = first_number != second_number
print(is_equal)

# Logical -> Membanding multiple Boolean Value
age = 18
has_license = True

# AND -> True ketika semua nilai True
can_drive = age >= 18 and has_license
print(can_drive)

# OR -> True ketika salah satu nilainya -> True
username = "reza"
is_admin = username == "reza" or username == "admin"
print(is_admin)

# Membership -> Mengecek apakah nilai ada di dalam list / words
my_string = "Hello World"
is_hello_in_string = "Hello" in my_string
print(is_hello_in_string)

# Identity -> Mengecek apakah dua buah variable merujuk kepada object yang sama
data = None
is_data_exist = data is None
# user is None / user is not None
print(is_data_exist)