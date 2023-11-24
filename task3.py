from numpy import mean

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}\n'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такого студента нет')
            return
        return self.average_grade() < other.average_grade()
    
    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Такого студента нет')
            return
        return self.average_grade() > other.average_grade()
    

    def average_grade(self):
        grades_list = []
        for grades in self.grades.values():
            grades_list += grades
        return round(mean(grades_list),1)
    
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
                
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}\n'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такого лектора нет')
            return
        return self.average_grade() < other.average_grade()
    
    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такого лектора нет')
            return
        return self.average_grade() > other.average_grade()

    def average_grade(self):
        grades_list = []
        for grades in self.grades.values():
            grades_list += grades
        return round(mean(grades_list),1)
    

class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
 
some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.finished_courses += ['Введение в программирование']
second_student = Student('Vasily', 'Pupkin', 'some_gender')
second_student.courses_in_progress += ['Python']
second_student.finished_courses += ['Git']
 
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python']
 
some_reviewer.rate_hw(some_student, 'Python', 8)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)

some_reviewer.rate_hw(second_student, 'Python', 5)
some_reviewer.rate_hw(second_student, 'Python', 3)
some_reviewer.rate_hw(second_student, 'Python', 2)

some_lecturer = Lecturer('Another', 'Buddy')
some_lecturer.courses_attached += ['Python']
second_lecturer = Lecturer('Second', 'Buddy')
second_lecturer.courses_attached += ['Python']

some_student.rate_lecturer(some_lecturer, 'Python', 9)
some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 10)

second_student.rate_lecturer(second_lecturer, 'Python', 10)
second_student.rate_lecturer(second_lecturer, 'Python', 10)
second_student.rate_lecturer(second_lecturer, 'Python', 10)
 
print (some_reviewer)
print (some_lecturer)
print (second_lecturer)
print (some_student)
print (second_student)
print (some_student > second_student)
print (some_lecturer < second_student)