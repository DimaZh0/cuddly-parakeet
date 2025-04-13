import random

class Pet:
    def __init__(self, name="Fluffy"):
        self.name = name
        self.hunger = 50
        self.happiness = 50

    def eat(self):
        self.hunger += 10
        if self.hunger > 100:
            self.hunger = 100

    def play(self):
        self.happiness += 10
        self.hunger -= 5
        if self.happiness > 100:
            self.happiness = 100
        if self.hunger < 0:
            self.hunger = 0

    def live_day(self):
        self.hunger -= 5
        self.happiness -= 3
        if self.hunger < 0:
            self.hunger = 0
        if self.happiness < 0:
            self.happiness = 0

class Human:

    def __init__(self, name='Human', job=None, home=None, car=None, pet=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home
        self.pet = pet

    def get_home(self):
        pass

    def get_car(self):
        pass

    def get_job(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def shopping(self):
        pass

    def chill(self):
        pass

    def clean_home(self):
        pass

    def to_repair(self):
        pass

    def days_indexes(self, day):
        pass

    def is_alive(self):
        pass

    def play_with_pet(self):
        if self.pet:
            print(f"{self.name} is playing with {self.pet.name}")
            self.pet.play()
            self.gladness += 5

    def feed_pet(self):
        if self.pet:
            print(f"{self.name} is feeding {self.pet.name}")
            self.pet.eat()
            self.money -= 5

    def live(self, day):
        print(f"\nDay {day}:")
        if self.pet:
            self.play_with_pet()
            self.feed_pet()
            self.pet.live_day()
            print(f"{self.pet.name}'s hunger: {self.pet.hunger}, happiness: {self.pet.happiness}")
        else:
            print(f"{self.name} has no pet.")
        return True

class Auto:

    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]['fuel']
        self.strength = brand_list[self.brand]['strength']
        self.consumption = brand_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('Car cannot move')
            return False

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']

brands_of_car = {
    'BMW': {'fuel': 100, 'strength': 100, 'consumption': 7},
}

job_list = {
    'Python developer': {'salary': 40, 'gladness_less': 3},
}

pet = Pet("Buddy")
nick = Human("Nick", pet=pet)

for day in range(1, 4):
    if not nick.live(day):
        break