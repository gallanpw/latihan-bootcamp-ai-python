age = 16
has_license = True

if age >= 18:
    print("You are eligible for Driving License")
else:
    print("DON'T DRIVE!")

############################################################

grade = 87

if grade >= 90:
    print("Kamu lulus dengan nilai bagus")
elif grade >= 80:
    print("Kamu lulus dengan nilai cukup")
else:
    print("Kamu tidak lulus")

# 2 Buah Condition Statement
gaji = 5000000

if gaji < 1000000:
    print("Anda boleh gak bayar pajak")
elif gaji >= 1000000 and gaji <= 5000000:
    print("Anda harus bayar pajak 5%")
else:
    print("Anda harus bayar pajak 10%")