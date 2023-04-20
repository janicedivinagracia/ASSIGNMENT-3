from Person import person

class student(person):
    def __init__(self, id, last_name, first_name, middle_name, type, year, course, section):
        self.year = year
        self.course = course
        self.section = section

        person.__init__(self, id, last_name, first_name, middle_name, type)
        # super(self).__init__(self, id, last_name, first_name, middle_name, type)

    def name(self) -> str:
        return super().__str__()

    def getYrCourseSec(self):
        return f'{self.year}/{self.course}/{self.section}'