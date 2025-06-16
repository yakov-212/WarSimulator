from datetime import datetime

def dots():
    print("...."*15)
people = [{"name": "Alice", "age": 30, "height": 165},
          {"name": "Bob", "age": 25, "height": 175},
          {"name": "Charlie", "age": 35, "height": 170}
]

age_order = sorted(people, key=lambda people: people["age"])
for person in age_order:
    print(f"{person["name"]} is {person["age"]}")

dots()

height_order = sorted(people, key=lambda people: people["height"],reverse=True)
for person in height_order:
    print(f"{person["name"]}'s height is {person["height"]}")

dots()

class Vehical:
    def __init__(self, model, year, mileage):
        self.model = model
        self.year = year  
        self.mileage = mileage
        self.penalty = (datetime.now().year - self.year) * 1000

    def age_penalty(self):
        print(f"the current year is {datetime.now().year}\n"
               f"the {self.model} was made in {self.year}\n"
               f"the age penalty is {self.penalty}")

    def __str__(self):
        return f"{self.model} {self.year} with {self.mileage} mileage"
    
red = Vehical("Honda",2008,39452)
blue = Vehical("Sudan",1995,54831)
gray = Vehical("Tesla",2016,19780)
cars = [red,blue,gray]

print(f"the car with the highest mileage is the {max(cars, key=lambda car: car.mileage)}")
print(f"the oldest car is the {min(cars, key=lambda car: car.year)}")

dots()
red.age_penalty()
dots()
blue.age_penalty()
dots()
gray.age_penalty()
dots()
print(f"the car with the most effeciant mileage is the {min(cars, key=lambda car: car.mileage + car.penalty)}")
dots()
a = {"hsai": "bye", "12": 2,8:0}
b = {"good": "no","me": "i"}
def krint(**kwargs):
    for i, b in kwargs:
        print(i)
print(a,b)