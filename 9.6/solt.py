#-*-coding:utf-8-*-

class Student(object):
    __slots__ = ('name','age')
    # pass

s=Student()
s.name='haha'
s.age='12'
# s.score=99

# print(s.name)



class GraduateStudent(Student):
    pass
g = GraduateStudent()
g.score=999
# print(g.score)