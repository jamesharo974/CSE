class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work." % self.name)


person = Person("name", "age")

class Employee(Person):
    def __init__(self, name, job):
        super(Employee,self).__init__(name, age)
        self.name = name
        self.job = job

    def job(self):
        print("%s has a job." % self.name)

employee = Employee("name","job")


class Programmer(Employee):
    def __init__(self, job, laptop, name):
        super(Programmer, self).__init__(job, name)
        self.laptop = laptop

    def python(self):
        print("%s is programming on his %s" % (self.name, self.laptop))


programmer = Programmer("name", "job", "laptop")


