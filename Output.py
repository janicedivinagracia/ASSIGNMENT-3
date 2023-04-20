from Student import student
from Teacher import teacher
from Grade import grade
from Load import load

#Student Output
print()
Stud = student('21-56545','Divinagracia','Janice','Gonzaga','Student','2','BSCS','A')
print(Stud.Name())
print(Stud.getYrCourseSec())
print()
print('------------------------------')

#STUDENT OUTPUT WITH GRADE
Grade1 = grade(' 90','99','94','92')
Grade1.type = 'Student'
Grade1.id = '21-45354'
Grade1.last_name = 'Divinagracia'
Grade1.first_name = 'Janice'
Grade1.middle_name = 'Gonzaga'
Grade1.year = '2'
Grade1.course = 'BSCS'
Grade1.section = 'A'

print(Grade1.Name())
print(Grade1.getYrCourseSec())
print('------------------------------')
print(Grade1.getGrade())
print('Average: ' + str(Grade1.getAverage()))
print()
print('------------------------------')

#TEACHER OUTPUT
Teach = teacher('Teacher','001-34343','Divinagracia','Nice','Gonzaga','CEIT','Dean')
print(Teach.Name())
print(Teach.getDepartment())
print(Teach.getPosition())

Load = load('English','Math','Science','Filipino')
print('------------------------------')
print('Load: ' + Load.getSubjects())