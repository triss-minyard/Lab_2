
info = input("Информация о студенте(Имя, возраст, група, оценки: ")
parts = info.split()
name = parts[0]
age = parts[1]
groupa = parts[2]
grades = list(parts[3:])
res = [name, age, groupa, grades]
print(res)
