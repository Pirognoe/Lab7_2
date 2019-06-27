import math

#Вынес настройку курса вне класса - для пробы пера
conf = {
        'exam_max': 30,
        'lab_max': 7,
        'lab_num': 10,
        'k': 0.61,
    }

class Student(object):
    name = 'Lox'

    def __init__(self, name, conf):
        self.name = name
        self.conf = conf
        # Create list to store labs results
        self.labs = []
        for i in range(conf['lab_num']):
            self.labs.append(0)
        # Create variable to store exam result
        self.exam = 0
    #def error_check(self)

    def make_lab(self,m,n):
        if m > conf['lab_max']:
            pass

    #def make_exam(m)

    #def is_certified()



conf1 = {'exam_max': 20, 'lab_max': 40, 'lab_num': 12, 'k': 0.75}
o1 = Student('Oleg', conf1)
print
o1.is_certified(), '== (0, False)'
o2 = Student('Oleg', conf1)
o2.make_lab(60).make_lab(35.2)
print
o2.is_certified(), '== (75.2, True)'
o3 = Student('Oleg', conf1)
o3.make_lab(10).make_lab(10).make_exam(15)
print
o3.is_certified(), '== (35, False)'
o3.make_lab(20, 1).make_lab(20, 0),
print
o3.is_certified(), '== (55, False)'
o3.make_lab(50, 2)
o3.is_certified()
o3.make_lab(40, 1)
print
o3.is_certified(), '== (75, True)'
conf2 = {'exam_max': 52, 'lab_max': 8, 'lab_num': 6, 'k': 0.5}
o4 = Student('Oleg', conf2)
o4.make_exam(100)
print
o4.is_certified(), '== (52, True)'
o5 = Student('Oleg', conf2)
o5.make_lab(40).make_lab(7, 5).make_lab(1).make_lab(7).make_lab(7).make_lab(7).make_lab(7, 1)
print
o5.is_certified(), '== (43, False)'
o5.make_lab(7)
print
o5.is_certified(), '== (43, False)'
o5.make_exam(7)
conf3 = {'exam_max': 10, 'lab_max': 1, 'lab_num': 90, 'k': 0.5, }
o6 = Student('Oleg', conf3)
for i in range(51): o6.make_lab(1)
print
o6.is_certified(), '== (51, True)'