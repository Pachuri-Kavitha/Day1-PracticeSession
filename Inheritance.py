class Developer:
    def work(self):
        print("Developer is working")
    def attendMeeting(self):
        print("Developer is attending meeting")

class JavaDeveloper(Developer):
    def work(self):
        print("JavaDeveloper is working on java")
    def doJavaProject(self):
        print("JavaDeveloper is building a java project")

class PythonDeveloper(Developer):
    def work(self):
        print("PythonDeveloper is working on python")
    def doPythonProject(self):
        print("PythonDeveloper is building a python project")

dev = Developer()
javaDev = JavaDeveloper()
pythonDev = PythonDeveloper()

javaDev.work()
javaDev.attendMeeting()
javaDev.doJavaProject()

pythonDev.work()
pythonDev.attendMeeting()
pythonDev.doPythonProject()
