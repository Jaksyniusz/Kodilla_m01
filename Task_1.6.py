# Ćwiczenie 1.6

for i in range (1,101):
    division_result = i % 3
    if division_result == 0:
        print("for "+ str(i))
    else:
        pass

my_number = 0
while True:
    pass
    my_number = my_number + 1
    division_result = my_number % 3
    if my_number < 101:
        if division_result == 0:
            print("while " + str(my_number))
        else:
            pass
    else:
        break