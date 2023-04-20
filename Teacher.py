from Person import person

class teacher(person):
    def __init__(self, id, last_name, first_name, middle_name, type, Department, Position):
        self.Department = Department
        self.Position = Position

        person.__init__(self, id, last_name, first_name, middle_name, type)

    def __str__(self) -> str:
        return super().__str__()

    def getDepartment(self):
        return self.Department

    def getPosition(self):
        return self.Position
