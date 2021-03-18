class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_attached = []
        self.grades = {}
    def rate_lectuer(self, lectuer, course, grade):
        if grade > 10 or grade < 0:
            return 'Оценку можно выставлять только по 10-балльной шкале'
        if isinstance(lectuer, Lectuer):
            if (course in self.courses_attached) or (course in self.finished_courses):
                if course in lectuer.courses_attached:
                    if course in lectuer.grades:
                        lectuer.grades[course] += [grade]
                    else:
                        lectuer.grades[course] = [grade]
                    return 'ok'
                return 'Лектор ' + lectuer.surname + ' ' + lectuer.name + ' не преподает курс "' + course + '"'
            return 'Вы не проходили курс "' + course + '"'
        return 'Объект ' + lectuer + ' не является объектом класса Lectuer'
    def __str__(self):
        print('Имя:', self.name)
        print('Фамилия:', self.surname)
        total_grade = 0
        for course, grade in self.grades.items():
            total_grade += sum(grade) / len(self.grades)
        print('Средняя оценка за домашние задания:', total_grade)
        print('Курсы в процессе изучения:', self.courses_attached)
        print('Завершенные курсы:', self.courses_attached)
        return chr(10) + chr(13)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lectuer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def __str__(self):
        print('Имя:', self.name)
        print('Фамилия:', self.surname)
        print('Средняя оценка за лекции:', sum(self.grades)/len(self.grades))
        return chr(10) + chr(13)

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student):
            if course in self.courses_attached:
                if course in student.courses_attached:
                    if course in student.grades:
                        student.grades[course] += [grade]
                    else:
                        student.grades[course] = [grade]
                    return 'ok'
                return 'Студент' + student.surname + ' ' + student.name + ' не проходит курс "' + course + '"'
            return 'Эксперт ' + self.surname + ' ' + self.name + ' не закреплен за курсом "' + course + '"'
        return 'Объект ' + student + ' не является объектом класса Student'
    def __str__(self):
        print('Имя:', self.name)
        print('Фамилия:', self.surname)
        return chr(10) + chr(13)

def middle_grade(list, course):
    i = 0
    total_grade = 0
    for unit in list:
        if isinstance(unit, Student) or isinstance(unit, Lectuer):
            if course in unit.courses_attached:
                for courses, grade in unit.grades.items():
                    if course == courses:
                        total_grade += sum(grade)
                        i += len(grade)
    if i > 0 and total_grade > 0:
        return total_grade/i
    return 0

student_1 = Student('Иван', 'Иванов', 'М')
student_1.courses_attached.append('Python')
student_1.courses_attached.append('Java')
student_1.finished_courses.append('JavaScript')
student_2 = Student('Петр', 'Петров', 'М')
student_2.courses_attached.append('Python')
student_2.courses_attached.append('Java')
student_1.finished_courses.append('C++')
lectuer_1 = Lectuer('Василий', 'Васильев')
lectuer_1.courses_attached.append('Python')
lectuer_2 = Lectuer('Алексей', 'Алексеев')
lectuer_2.courses_attached.append('Java')
Reviewer_1 = Reviewer('Сергей', 'Сергеев')
Reviewer_1.courses_attached.append('JavaScript')
Reviewer_1.courses_attached.append('Java')
Reviewer_2 = Reviewer('Дмитрий', 'Дмитриев')
Reviewer_2.courses_attached.append('C++')
Reviewer_2.courses_attached.append('Python')

student_1.rate_lectuer(lectuer_1, 'Python', 1)
student_1.rate_lectuer(lectuer_2, 'Java', 1)

student_2.rate_lectuer(lectuer_1, 'Python', 8)
student_2.rate_lectuer(lectuer_2, 'Java', 9)

Reviewer_1.rate_hw(student_1, 'Java', 5)
Reviewer_1.rate_hw(student_2, 'Java', 3)

Reviewer_2.rate_hw(student_1, 'Python', 4)
Reviewer_2.rate_hw(student_2, 'Python', 6)
Reviewer_2.rate_hw(student_2, 'Python', 10)

# str(student_1)
# str(student_2)
#
# str(Reviewer_1)
# str(Reviewer_2)
#
# str(lectuer_1)
# str(lectuer_2)

print(middle_grade([student_1, student_2], 'Python'))
print(middle_grade([student_1, student_2], 'Java'))
print(middle_grade([lectuer_1, lectuer_2], 'Python'))
print(middle_grade([lectuer_1, lectuer_2], 'Java'))