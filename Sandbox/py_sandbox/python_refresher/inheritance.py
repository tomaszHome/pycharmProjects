class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):  # calculates the average of the marks
        return sum(self.marks) / len(self.marks)

    #@classmethod
    #def add_friend(cls, origin, friend, *args):   # adds friend in the same school
       # return cls(friend, origin.school, *args)

    # Using **kwarg
    @classmethod
    def add_friend(cls, origin, friend, **kwargs):  # adds friend in the same school
        return cls(friend, origin.school, **kwargs)

# anna = Student("Anna", "MIT")
# friend = anna.add_friend("Greg")

# print friend.name
# print friend.school


# Inheritance


# by passing the Student this class
# inherits __init__ method from Student class
class WorkingStudents(Student):
    # cause name and school are already in Student class
    # there is no need to call them again
    def __init__(self, name, school, salary, job_title):
        # Instead we use super().__init__ superclass Student what will set name and school
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title


anna = WorkingStudents("Anna", "MIT", 100, "waiter")
print("""{} studies at {}, 
Works as {},
Salary = £{} a week.\n""".format(anna.name, anna.school, anna.job_title, anna.salary))
# adding new friend from the anna origin
# origin is required so that software knows where the school is coming from
# salary and job_title added for **kwarg
# when using *arg the above not needed
friend = WorkingStudents.add_friend(anna, "Greg", salary=300, job_title="mechanic")
print("""{} studies at {}, 
Works as {},
Salary = £{} a week.""".format(friend.name, friend.school, friend.job_title, friend.salary))


