import json
file = open('Data/Students.json')
students = json.load(file)
print('ИМЕНА ВСЕХ УЧЕНИКОВ')
for student in students:
    print(student['name'])
print('-'*50)

print('ИМЕНА ВСЕХ УЧЕНИКОВ В ДАННОМ КЛАССЕ')
cl = input('Введите класс:')
for student in students:
    if student['class'] == cl:
        print(student['name'],student['surname'])
print('-'*50)

print('УЧИНИКИ ОДНОФАМЕЛЬЦЫ')
list_surnames = [student['surname'] for student in students]
dubles = []
for surname in list_surnames:
    if list_surnames.count(surname) > 1:
        dubles.append(surname)
duble = list(set(dubles))
for surname in duble:
    print(surname)
file.close()
print('-'*50)

print('ИМЕНА ВСЕХ УЧИТЕЛЕЙ')
file2 = open('Data/Teachers.json')
teachers = json.load(file2)
for teacher in teachers:
    print(teacher['name'])
file2.close()
print('-'*50)

print('СПИСОК ВСЕХ ШКОЛ')
file3_1 = open('Data/Students.json')
file3_2 = open('Data/Teachers.json')

schools_1 = json.load(file3_1)
schools_2 = json.load(file3_2)

list_school_1 = [school['school'] for school in schools_1]
list_school_2 = [school['school'] for school in schools_2]

list_school = list(set(list_school_1 + list_school_2))
for el in list_school:
    print(el)
file3_1.close()
file3_2.close()




