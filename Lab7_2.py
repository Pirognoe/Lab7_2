import math

# Declare first configuration for testing
conf = {
        'exam_max': 30,
        'lab_max': 7,
        'lab_num': 10,
        'k': 0.61,
    }

class Student(object):

    def __init__(self, name, conf):
        self.name = name
        self.conf = conf
        # Create list to store labs results
        self.labs = []
        for i in range(conf['lab_num']):
            self.labs.append(0)
        # Create variable to store exam result
        self.exam = 0


    def make_lab(self,m,n=0):
        if m > self.conf['lab_max']:
            print(m, self.conf['lab_max'], m > self.conf['lab_max'])
            return self
        elif n > self.conf['lab_num']:
            pass
            return self
        else:
            print('zhopa', n, m)
            self.labs[n] = m
            print(self.labs[n])
        return self

    # Define the exam method
    def make_exam(self, m):
        if m > self.conf['exam_max']:
            return self
        else:
            self.exam = m
        return self

    def is_certified(self):
        pass
        return self



conf1 = {'exam_max': 20, 'lab_max': 40, 'lab_num': 12, 'k': 0.75}
o1 = Student('Oleg', conf1)
print('============================Conf_1=====================')
o1.is_certified(), '== (0, False)'
o2 = Student('Oleg', conf1)
o2.make_lab(35.2)
print(o2.labs)
o2.make_lab(60).make_lab(35.2)
print('============================Conf_2=====================')
o2.is_certified(), '== (75.2, True)'
o3 = Student('Oleg', conf1)
o3.make_lab(10).make_lab(10).make_exam(15)
print('============================Conf_3=====================')
o3.is_certified(), '== (35, False)'
o3.make_lab(20, 1).make_lab(20, 0),
print('============================Conf_4=====================')
o3.is_certified(), '== (55, False)'
o3.make_lab(50, 2)
o3.is_certified()
o3.make_lab(40, 1)
print('============================Conf_5=====================')
o3.is_certified(), '== (75, True)'
conf2 = {'exam_max': 52, 'lab_max': 8, 'lab_num': 6, 'k': 0.5}
o4 = Student('Oleg', conf2)
o4.make_exam(100)
print('============================Conf_6=====================')
o4.is_certified(), '== (52, True)'
o5 = Student('Oleg', conf2)
o5.make_lab(40).make_lab(7, 5).make_lab(1).make_lab(7).make_lab(7).make_lab(7).make_lab(7, 1)
print('============================Conf_7=====================')
o5.is_certified(), '== (43, False)'
o5.make_lab(7)
print('============================Conf_8=====================')
o5.is_certified(), '== (43, False)'
o5.make_exam(7)
conf3 = {'exam_max': 10, 'lab_max': 1, 'lab_num': 90, 'k': 0.5, }
o6 = Student('Oleg', conf3)
for i in range(51): o6.make_lab(1)
print('============================Conf_9=====================')
o6.is_certified(), '== (51, True)'
