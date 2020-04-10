import random
import csv

class Course():
	"""Course a student can atttend"""

	def __init__(self, name, classroom, teacher, etcs, grade):
		"""Initialize course"""
		self.name = name
		self.classroom = classroom
		self.teacher = teacher
		self.etcs = etcs
		self.grade = 1

	def __repr__(self):
		return '{self.__class__.__name__}({self.name}, {self.}, {self.}, {self.}, {self.})'.format(self=self)

	def __str__(self):
		return 'this course is named {self.name}'.format(self=self)


class Data_sheet():
	"""Datasheet has multiple courses"""

	def __init__(self, courses):
		"""Initialize data_sheet"""
		self.courses = []
		for course in courses:
			new_course = Course(course.name, course.classroom, course.teacher, course.etcs, course.grade)
			self.courses.append(new_course)

	def __repr__(self):
		return '{self.__class__.__name__}(a list of courses)'.format(self=self)

	def __str__(self):
		return 'this student has courses {self.courses.length} number of courses'.format(self=self)

	def get_grades_as_a_list():
		grades = []
		for c in self.courses:
			grades.append(c.grade)
		return grades


class Student():
	"""Student with datasheet and courses"""

	def __init__(self, name, gender, data_sheet, image_url):
		"""Initialize student"""
		self.name = name
		self.gender = gender
		self.data_sheet = data_sheet
		self.image_url = image_url

	def __repr__(self):
		return '{self.__class__.__name__}({self.name}, {self.gender})'.format(self=self)

	def __str__(self):
		return 'a student named {self.name}'.format(self=self)

	def get_average_grade():
		return sum(self.data_sheet.get_grades_as_a_list()) / len(self.data_sheet.get_grades_as_a_list())


course_names = ["Course1", "Course2", "Course3", "Course4"]
classrooms = [1, 2, 3]
grades = [0, 2, 4, 7, 10, 12]
etcs = [5, 10, 20]
teachers = ["Hanne", "Per", "Bill Gates"]
names = ["Kurt Wonnegut", "Anne Hansen",
		 "Peter Olsen", "Pia Nielsen", "Mette Pedersen"]
gender = ["Male", "Female"]
imgurl = ["https://www.w3schools.com/howto/img_avatar.png", "https://www.w3schools.com/howto/img_avatar2.png", "https://www.w3schools.com/w3images/avatar2.png", "https://www.w3schools.com/w3images/avatar6.png"]


def create_random_students(no):
	csv_file = 'random_student.csv'
	students = []
	for i in range(no):
		rcs = [Course(random.choice(course_names), random.choice(classrooms), random.choice(teachers), random.choice(etcs), random.choice(grades)) for i in range(3)]
		ds = Data_sheet(rcs)
		students.append(Student(random.choice(names), random.choice(gender), ds, random.choice(imgurl)))

	fieldnames = ["Name", "Gender", "Course", "Grade", "ImgUrl"]
	with open(csv_file, 'w') as csv_file:
		students_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
		students_writer.writeheader()
		for s in students:
#			for c in s.data_sheet.courses:
#				students_writer.writerow({'Name' : s.name, 'Gender' : s.gender, 'Course' : c.name, 'Grade': c.grade, 'ImgUrl' : s.image_url})
#				print(s.name, c.name)
				print(s.name)

create_random_students(1)
