class SchoolMember:
	'''所有成员'''
	def __init__(self,name,age):
		self.name = name
		self.age = age
		print("Initialized SchoolMember:{}".format(self.name))

	def tell(self):
		print('Name:{} Age:"{}"'.format(self.name, self.age), end = " ")


class Teacher(SchoolMember):
	'''老师'''
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print("Initialized Teacher:{}".format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('Salary:{:d}'.format(self.salary))


class Student(SchoolMember):
	'''学生'''
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print("Initialized Student:{}".format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('marks:{:d}'.format(self.marks))


t1 = Teacher('Mrs.Sherry','40',30000)
t2 = Teacher('Mr.Liu','52',50000)
s = Student('aiyi','22',75)

print()

teachers = [t1,t2]
for teacher in teachers:
	teacher.tell()
'''members = [t,s]
for member in members:
	member.tell()'''
		
