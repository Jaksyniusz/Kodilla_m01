# Zadanie: gwiazdkowe rysunki

print("Wstęp\n")
for i in range(1,6):
    print("*" * i)


# numer 1
print(f"\n\nZadanie 1\n")
star_row1 = "* " * 20
star_row2 = " *" * 20

def starring():
    print(star_row1)
    print(star_row2)    

for stars in range(1,6):
    starring()


# numer 2
print("\n\nZadanie 2\n")
star = "*"
for i in range(2,8,2):
    print(star * i)
    print(star * i)


# numer 3
print("\n\nZadanie 3\n")
for i in range(6,0,-1):
    print(star * i)