# Create a class “Programmer” for storing information of few programmers working at Microsoft. 
class programmers:
    company="MIcrosoft"

    def __init__(self,name,salary,skill) -> None:
        self.name=name
        self.salary=salary
        self.skill=skill
    def getinfo(self):
        print(f"Name-{self.name} Salary-{self.salary} Skill-{self.skill}")

a=programmers("Ankush","50LPA","AI/ML")
a.getinfo()

r=programmers("Ria","50LPA","UI/UX")
r.getinfo()
