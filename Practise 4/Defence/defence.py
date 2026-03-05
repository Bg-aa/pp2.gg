import json 
teacher1= {
    "name": "Nikita",
    "Course": '1',
}
teacher2 = {
    "name" : "Akbota",
    "Course" : '2',
}

teacher3 = {
    "name" : "Ayan",
    "Course" : '3',
}
teacher4 = {
    "name" : "Aksha",
    "Course" : '4',
}
with open('instractors.json', 'w') as file:
    json.dump([teacher1, teacher2, teacher3, teacher4], file)
with open('instractors.json', 'r') as file:
    data = json.load(file)
    for teacher in data:
        print(f"Name: {teacher['name']}, Course: {teacher['Course']}")


Student1 = {
    "name": "Aibyn",
    "Course": '1',
}
Student2 = {
    "name" : "Kanat",
    "Course" : '1',
}
Student3 = {
    "name" : "Dastan",
    "Course" : '2',
}
Student4 = {
    "name" : "Daryn",
    "Course" : '2',
}
Student5 = {
    "name" : "Dro",
    "Course" : '3',
} 
Student6 = {
    "name" : "Messi",
    "Course" : '3',
}
Student7 = {
    "name" : "Ronaldo",
    "Course" : '4',
}
Student8 = {
    "name" : "Neymar",
    "Course" : '4',
}
with open('students.json', 'w') as file:
    json.dump([Student1, Student2, Student3, Student4, Student5, Student6, Student7, Student8], file)
with open('students.json', 'r') as file:
    data = json.load(file)
    for student in data:
        print(f"Name: {student['name']}, Course: {student['Course']}")