class Student:
    def __init__(self, name, surname, gender):

        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, cours_name):
        self.finished_courses.append(cours_name)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'error'
    def __str__(self):
       return "Имя:" + self.name +"\nФамилия:" + self.surname +"\nСредняя оценка за домашние задания:"+ rate_asb(self.grades)+ "\nКурсы в процессе изучения:" + str(self.courses_in_progress) + "\nЗавершенные курсы: " + str(self.finished_courses)


class Mentor:
    def __init__(self, name, surname):

        self.name = name
        self.surname = surname


class Reviewer(Mentor):
    def __init__(self, name, surname):

        super().__init__(name, surname)
        self.cours_attached = []
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'error'

    def __str__(self):
        return "Имя:"+ self.name + "\nФамилия:" + self.surname

class Lecturer(Mentor):
    def __init__(self, name, surname):

        super().__init__(name, surname)
        self.grades = []
        self.cours_attached = []
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.cours_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return "Имя:" + self.name + "\nФамилия:" + self.surname + "\nСредняя оценка за лекции:" + rate_asb(self.grades)

def rate_asb(grades):
    if type(grades) is dict:
        amount_grades = []
        for grades in grades.values():
            for grade in grades:
                amount_grades.append(grade)
        return rate_asb(amount_grades)
    elif type(grades) is list and len(grades)!= 0:
        average = round(sum(grades) / len(grades), 2)
        return str(average)
    else:
        return "Данные не в словаре и не в списке."

def cours_grade_mean(students, cours):
    grades = []
    for cur_student in students:
        if cours in cur_student.grades.keys():
            for every_grade in cur_student.grades.get(cours):
                grades.append(every_grade)
        else:
            print("Курс" + cours + "отсутствует у студента" +cur_student.name + cur_student.surname)
    return students(grades)

def lecturers_grade_mean(all_lecturers):
    grades = []
    for current_lecturer in all_lecturers:
        for every_grade in current_lecturer.grades:
            grades.append(every_grade)
    return rate_asb(grades)



some_student = Student("Сергей","Нечаев","35")
some_student.finished_courses += ['Git']
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Внедрение интеграционных решений']
some_student.add_courses('автотестирование')
some_student.grades['Git'] = [7, 7, 7]
some_student.grades['Python'] = [5, 9, 5, 10, 9]
some_student.grades['Внедрение интеграционных решений'] = [6, 3]
print(some_student)

some_student_1 = Student("Сергей","Смирнов","35")
some_student_1.finished_courses += ['Git']
some_student_1.courses_in_progress += ['Python']
some_student_1.courses_in_progress += ['Внедрение интеграционных решений']
some_student_1.add_courses('автотестирование')
some_student_1.grades['Git'] = [4, 5, 3]
some_student_1.grades['Python'] = [1, 9, 5, 5, 9]
some_student_1.grades['Внедрение интеграционных решений'] = [8, 10]
print(some_student)

some_lecturer = Lecturer("Ivan","Ivanov")
some_lecturer.cours_attached += ['Git']
some_lecturer.cours_attached += ['Python']
some_lecturer.cours_attached += ['Внедрение интеграционных решений']
print(some_lecturer)

some_lecturer_1 = Lecturer("Рома","Петров")
some_lecturer_1.cours_attached += ['Git']
some_lecturer_1.cours_attached += ['Python']
some_lecturer_1.cours_attached += ['Внедрение интеграционных решений']
print(some_lecturer_1)

some_reviewer = Reviewer("Иван","Додик")
some_reviewer.cours_attached += ['Python']
print(some_reviewer)

some_reviewer1 = Reviewer("Сергей","Сергаев")
some_reviewer1.cours_attached += ['Python']
print(some_reviewer1)

print(some_student < some_student_1)
print(some_student_1 < some_student)
print(some_student > some_student_1)
print(some_student_1 > some_lecturer)

print(some_lecturer < some_lecturer_1)
print(some_lecturer < some_lecturer_1)
print(some_lecturer > some_lecturer_1)
print(some_lecturer > some_student_1)