import json

ask = False

students = [{"name": "Василий",
               "middle_name": "Дмитриевич",
               "surname": "Десятый",
               "school": "67 школа",
               "class": "7 В",
               "birth_day": "06.06.1997"},
            {"name": "Вадим",
               "middle_name": "Юрьевич",
               "surname": "Рахимов",
               "school": "17 гимназия",
               "class": "9 А",
               "birth_day": "14.06.2000"},
            {"name": "Данил",
               "middle_name": "Антонович",
               "surname": "Астафьев",
               "school": "111 лицей",
               "class": "10 А",
               "birth_day": "18.12.1999"},
            {"name": "Максим",
               "middle_name": "Антонович",
               "surname": "Астафьев",
               "school": "84 лицей",
               "class": "6 В",
               "birth_day": "20.04.2004"},
            {"name": "Евгений",
               "middle_name": "Васильевич",
               "surname": "Плутонов",
               "school": "184 лицей",
               "class": "13 В",
               "birth_day": "31.12.2225"}]

if ask:

    for student in students:

        students_data = json.load(open('Data/Students.json'))

        students_data.append(student)
        students_data_json = (json.dumps(students_data, ensure_ascii=False))

        file = open('Data/Students.json','w')
        file.write(students_data_json)

        file.close()




Teachers = [
  {
    "name": "Александр",
    "middle_name": "Васильевич",
    "surname": "Белый",
    "school": "76 школа",
    "class": [
      "4 А",
      "8 Б",
      "9 В"
    ],
    "birth_day": "06.03.1975"
  },
  {
    "name": "Владислав",
    "middle_name": "Мехайлович",
    "surname": "Низкин",
    "school": "12 гимназия",
    "class": [
      "7 А",
      "7 Б",
      "7 Г",
      "8 В"
    ],
    "birth_day": "29.10.1978"
  },
  {"name": "Екатирина",
    "middle_name": "Георгевна",
    "surname": "Маркушева",
    "school": "85 гимназия",
    "class": [
      "3 А",
      "5 Б",
      "8 Г",
      "9 В"
    ],
    "birth_day": "01.01.1981"
   }]

if ask:

    for Teacher in Teachers:

        Teachers_data = json.load(open('Data/Teachers.json'))

        Teachers_data.append(Teacher)
        Teachers_data_json = (json.dumps(Teachers_data, ensure_ascii=False))

        file = open('Data/Teachers.json','w')
        file.write(Teachers_data_json)
        file.close()

list_class = ['5 А','1 В','3 Г']

full_name_teacher = 'Екатирина Георгевна Маркушева'
name = full_name_teacher.split(' ')

if ask:

    teachers_data = json.load(open('Data/Teachers.json'))

    for teacher in teachers_data:

        if teacher['name'] == name[0] and teacher['middle_name'] == name[1] and teacher['surname'] == name[2]:
            for _class in list_class:
                teacher['class'].append(_class)

    teachers_data_json = (json.dumps(teachers_data, ensure_ascii=False))

    file = open('Data/Teachers.json','w')
    file.write(teachers_data_json)
    file.close()

full_name_student = 'Вадим Юрьевич Рахимов'
name = full_name_student.split(' ')

i = 0

if ask:
    students_data = json.load(open('Data/Students.json'))

    for student in students_data:

        if student['name'] == name[0] and student['middle_name'] == name[1] and student['surname'] == name[2]:
            del students_data[i]

            students_data_json = (json.dumps(students_data, ensure_ascii=False))
            file = open('Data/Students.json', 'w')
            file.write(students_data_json)
            file.close()
        i += 1

_class = '7 В'
i = 0
ask = True

if ask:
    students_data = json.load(open('Data/Students.json'))

    for student in students_data:

        if student['class'] == _class:
            del students_data[i]

            students_data_json = (json.dumps(students_data, ensure_ascii=False))
            file = open('Data/Students.json', 'w')
            file.write(students_data_json)
            file.close()

        i += 1

full_name_teacher = 'Екатирина Георгевна Маркушева'
name = full_name_teacher.split(' ')

i = 0

if ask:
    teachers_data = json.load(open('Data/Teachers.json'))

    for teacher in teachers_data:

        if teacher['name'] == name[0] and teacher['middle_name'] == name[1] and teacher['surname'] == name[2]:
            del teachers_data[i]

            teachers_data_json = (json.dumps(teachers_data, ensure_ascii=False))
            file = open('Data/Teachers.json','w')
            file.write(teachers_data_json)
            file.close()

        i += 1

school = '12 гимназия'

if ask:
    teachers_data = json.load(open('Data/Teachers.json'))

    for teacher in teachers_data:

        if teacher['school'] == school:
            del teachers_data[i]

            teachers_data_json = (json.dumps(teachers_data, ensure_ascii=False))
            file = open('Data/Teachers.json','w')
            file.write(teachers_data_json)
            file.close()


full_name_teacher = 'Александр Васильевич Белый'
name = full_name_teacher.split(' ')
_class = '4 А'

i = 0
if ask:
    teachers_data = json.load(open('Data/Teachers.json'))

    for teacher in teachers_data:
        if teacher['name'] == name[0] and teacher['middle_name'] == name[1] and teacher['surname'] == name[2]:
            for find_class in teacher['class']:
                if find_class == _class:
                    del teacher['class'][i]

                    teachers_data_json = (json.dumps(teachers_data, ensure_ascii=False))
                    file = open('Data/Teachers.json','w')
                    file.write(teachers_data_json)
                    file.close()
                i += 1
