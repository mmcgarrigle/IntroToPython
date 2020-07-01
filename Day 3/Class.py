class Student:

    def __init__(self, name, age, classTaken, score):
        self.name = name
        self.age = age
        self.classTaken = classTaken
        self.score = score


john = Student("John", "21", "2B", "85")
jane = Student("Jane", "22", "5A", "92")
joan = Student("Joan", "19", "1A", "78")
johan = Student("Johan", "35", "4C", "80")


john_score = getattr(john, "score")
jane_score = getattr(jane, "score")
joan_score = getattr(joan, "score")
johan_score = getattr(johan, "score")

total_score = int(john_score) + int(jane_score) + int(joan_score) + int(johan_score)
print(total_score / 4)
