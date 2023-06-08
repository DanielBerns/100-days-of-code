import random

class City:
    def __init__(self, population, size):
        self.population = population
        self.size = size
        self.people = []
        for i in range(population):
            self.people.append(Person(self))

    def simulate(self):
        for day in range(365):
            for person in self.people:
                person.do_stuff()

class Person:
    def __init__(self, city):
        self.city = city
        self.job = random.choice(["worker", "student", "unemployed"])
        self.home = random.choice(city.get_houses())

    def do_stuff(self):
        if self.job == "worker":
            self.go_to_work()
        elif self.job == "student":
            self.go_to_school()
        else:
            self.do_nothing()

    def go_to_work(self):
        self.city.get_business(self.job).add_worker(self)

    def go_to_school(self):
        self.city.get_school(self.job).add_student(self)

    def do_nothing(self):
        pass

def main():
    city = City(1000, 1000)
    city.simulate()

if __name__ == "__main__":
    main()
 
