groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "exams": ["Философия", "ИС", "parfenin", "КТП"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Михаил",
        "surname": "Юхновский",
        "exams": ["Философия", "ИС", "parfenin", "КТП"],
        "marks": [3, 3, 4]
    },
    {
        "name": "Дмитрий",
        "surname": "Масленников",
        "exams": ["Философия", "ИС", "parfenin", "КТП"],
        "marks": [4, 5, 5]
    }
]

def print_students(students):
    avg_marks = float(input("Введите средний балл: "))
    print(avg_marks)
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(40), u"Оценки".ljust(20))
    for student in students:
        if sum(student["marks"])/len(student["marks"]) > avg_marks:
            print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(40), str(student["marks"]).ljust(20))

print_students(groupmates)
# task for labs 1
