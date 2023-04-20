from Student import student

class grade(student):
    def __init__(self, English, Math, Science, Filipino):
        self.English = English
        self.Math = Math
        self.Science = Science
        self.Filipino = Filipino

    def getGrade(self):
        return f'{self.English}\n {self.Math}\n {self.Science}\n {self.Filipino}'

    def getAverage(self):
        return (int(self.English) + int(self.Math) + int(self.Science) + int(self.Filipino)) / 4