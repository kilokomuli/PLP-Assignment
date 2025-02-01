# Smartphone Class with Encapsulation
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self._storage = storage  # Encapsulated attribute
        self.__battery = battery  # Private attribute

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def take_photo(self):
        print(f"{self.brand} {self.model} took a photo!")

    def get_battery_status(self):
        return f"Battery: {self.__battery}%"

# Polymorphism with Vehicles
class Vehicle:
    def move(self):
        pass  # Abstract method (implemented differently in subclasses)

class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky")

class Boat(Vehicle):
    def move(self):
        print("🚢 Sailing on the water")

# Testing the Smartphone class
phone = Smartphone("Apple", "iPhone 14", "256GB", 85)
phone.make_call("123-456-7890")
phone.take_photo()
print(phone.get_battery_status())

# Testing Polymorphism with Vehicles
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()