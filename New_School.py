import json

file = open('/home/main/Загрузки/Students.json')
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
list_surname = [student['surname'] for student in students] #Доделать

file.close()
print('-'*50)

print('ИМЕНА ВСЕХ УЧИТЕЛЕЙ')
file2 = open('/home/main/Загрузки/Teachers.json')
teachers = json.load(file2)
for teacher in teachers:
    print(teacher['name'])
file2.close()
print('-'*50)

print('СПИСОК ВСЕХ ШКОЛ')
file3_1 = open('/home/main/Загрузки/Students.json')
file3_2 = open('/home/main/Загрузки/Teachers.json')

schools_1 = json.load(file3_1)
schools_2 = json.load(file3_2)

list_school_1 = [school['school'] for school in schools_1]
list_school_2 = [school['school'] for school in schools_2]

list_school = list(set(list_school_1 + list_school_2))
for el in list_school:
    print(el)
file3_1.close()
file3_2.close()




