class Vehicle:
    def __init__(self,name,max_speeed, mileage):
        self.name = name
        self.max_speed = max_speeed
        self.mileage = mileage
class Bus(Vehicle):
    pass
School_Bus = Bus("Volvo School Bus Model X360", 180, 12)
print("Vehicle Name:",School_Bus.name, "Speed:", School_Bus.max_speed, "Mileage:", School_Bus.mileage)