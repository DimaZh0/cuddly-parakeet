#
# class Student:
#
#     amount_of_students = 0
#
#     def __init__(self, name, height=160):
#         self.name = name
#         self.height = height
#         Student.amount_of_students += 1
#
#     def grow(self, value=1):
#         self.height += value
#
#     def __str__(self):
#         return f'I am a Student. My name is {self.name}'
#
#
# Nick = Student(name='Nick')
# print(Nick.height)
# Nick.grow(25)
# print(Nick.name, Nick.height)
# print(Nick)
#
# Kate = Student(name='Kate', height=170)
# print(Kate.height)
#
# print(Nick.amount_of_students)
# print(Student.amount_of_students)


import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 100
        self.alive = True

    def to_study(self):
        print('Time to study...')
        self.progress += 0.15
        self.gladness -= 5

    def to_sleep(self):
        print('I will sleep')
        self.gladness += 3

    def to_chill(self):
        if self.money >= 10:
            print('Rest time')
            self.progress -= 0.1
            self.gladness += 5
            self.money -= 10
        else:
            print("Not enough money to chill, need to work!")
            self.to_work()

    def to_work(self):
        print('Time to work...')
        self.money += 20
        self.gladness -= 4
        self.progress -= 0.05

    def is_alive(self):
        if self.progress < -0.5:
            print('Failed the course...')
            self.alive = False
        elif self.gladness <= 0:
            print('Severe depression...')
            self.alive = False
        elif self.progress > 5:
            print('Graduated as a genius!')
            self.alive = False
        elif self.money < 0:
            print("Bankrupt! Can't afford to live...")
            self.alive = False

    def end_of_day(self):
        print(f'Gladness: {self.gladness}')
        print(f'Progress: {self.progress}')
        print(f'Money: {self.money}')

    def choose_activity(self):
        if self.progress < 1:
            return "study"
        elif self.gladness < 20:
            return "chill"
        elif self.money < 20:
            return "work"
        else:
            return random.choice(["study", "sleep", "chill", "work"])

    def live(self, day):
        print(f'\nDay {day} of {self.name} life')
        activity = self.choose_activity()
        if activity == "study":
            self.to_study()
        elif activity == "sleep":
            self.to_sleep()
        elif activity == "chill":
            self.to_chill()
        elif activity == "work":
            self.to_work()

        self.end_of_day()
        self.is_alive()

nick = Student(name='Nick')
for day in range(1, 500):
    if not nick.alive:
        break
    nick.live(day)
