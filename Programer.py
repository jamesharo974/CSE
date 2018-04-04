class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work." % self.name)


class Employee(Person):
    def __init__(self, name, age, pay, job):
        super(Employee,self).__init__(name, age)
        self.pay = pay
        self.job = job

    def Program(self):
        print("You know how to program in python.")

