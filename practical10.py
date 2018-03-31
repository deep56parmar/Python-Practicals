class College():
    """College class contains information about College."""
    def __init__(self):
        self.collegeName = ""
        self.collegeCode = 0
        self.collegeBranches = 0
    def setData(self,name,code,number):
        self.collegeName += name
        self.collegeCode = code
        self.collegeBranches = number
    def getData(self):
        print("college Name is ",self.collegeName)
        print("college Code is ",self.collegeCode)
        print("Number of branches ",self.collegeBranches)

class Student(College):
    """Student Class inherits the data of college class"""
    def __init__(self):
        super().__init__()
        self.studentName = ""
        self.enrollment = 0
        self.studentBranch = ""
        self.semester =0
    def setData(self,name,code,number,Sname,enroll,branch,sem):
        self.studentName += Sname
        self.enrollment = enroll
        self.studentBranch += branch
        self.semester = sem
        self.collegeName += name
        self.collegeCode = code
        self.collegeBranches = number
    def getData(self):
        print("student name is ",self.studentName , " enrollment number is ", self.enrollment)
        print("student is in ", self.studentBranch ," branch and in " ,self.semester, " semester.")

student1 = Student()
student1.setData("GECG",1024,12,"Deep parmar",140130107055,"CE",8)
College.getData(student1)
Student.getData(student1)
