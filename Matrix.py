# когда 2 условия
# pill = "red"
#
# if pill == "red":
#     print("Neo is fighting...")
# else:
#     print("Neo is still working in office...")


# Когда 1 условие
# password = 1234
#
# if password == 1234:
#     print("Welcome to system!")

# password = 1234
#
# if not (password == 1234):   или поставить не равно !=
#     print("Access denied!")

# если синтаксически требуется конструкция, а логически ничего нет, то используется pass - пустой операнд
# НО ИСПОЛЬЗОВАТЬ В РАБОТЕ НЕЛЬЗЯ!

#когда условий >2
# Оценки в школе
# 0 - 3 - "Very bad"
# 4 - "So-so"
# 5 - 6 - "Good"
# 7 - 8 - "Very good"
# 9 - 10 - "Super"

mark = 6

if mark <=3:
    print("Very bad")
elif mark == 4:
    print ("So-so")
elif mark == 5 or mark == 6:
    print("Good")
elif mark == 7 or mark == 8:
    print("Very good")
else: print("Super")

