class Vehicle:
    def __init__(self, vid, model, year):
        self.vid = vid
        self.model = model
        self.year = year

    def __str__(self):
        return "VID: " + self.vid + " | " + self.model + " (" + str(self.year) + ")"

    def __eq__(self, other):
        return self.vid == other.vid

    def is_new(self, n):
        return (2026 - self.year) <= n

class Car(Vehicle):
    def __init__(self, vid, model, year, fuel_type, doors):
        super().__init__(vid, model, year)
        self.fuel_type = fuel_type
        self.doors = doors

    def __str__(self):
        return "[Car] " + super().__str__() + " | Fuel: " + self.fuel_type + " | " + str(self.doors) + " Doors"

class Truck(Vehicle):
    def __init__(self, vid, model, year, max_load, axles):
        super().__init__(vid, model, year)
        self.max_load = max_load
        self.axles = axles

    def __str__(self):
        return "[Truck] " + super().__str__() + " | Load: " + str(self.max_load) + "kg | " + str(self.axles) + " Axles"

class Motorcycle(Vehicle):
    def __init__(self, vid, model, year, engine_cc, v_type):
        super().__init__(vid, model, year)
        self.engine_cc = engine_cc
        self.v_type = v_type

    def __str__(self):
        return "[Motorcycle] " + super().__str__() + " | Eng: " + str(self.engine_cc) + "cc | Type: " + self.v_type


virtual_file = []

def save_fleet_to_file(vehicles, filename):

    for v in vehicles:
        if isinstance(v, Car):
            line = "Car," + v.vid + "," + v.model + "," + str(v.year) + "," + v.fuel_type + "," + str(v.doors)
        elif isinstance(v, Truck):
            line = "Truck," + v.vid + "," + v.model + "," + str(v.year) + "," + str(v.max_load) + "," + str(v.axles)
        elif isinstance(v, Motorcycle):
            line = "Motorcycle," + v.vid + "," + v.model + "," + str(v.year) + "," + str(v.engine_cc) + "," + v.v_type
        virtual_file.append(line)

def load_fleet_from_file(filename):
#file gibiymiş gibi liste yaptık
    reconstructed_vehicles = []
    for line in virtual_file:
        parts = line.split(",")
        category = parts[0]
        if category == "Car":
            reconstructed_vehicles.append(Car(parts[1], parts[2], int(parts[3]), parts[4], int(parts[5])))
        elif category == "Truck":
            reconstructed_vehicles.append(Truck(parts[1], parts[2], int(parts[3]), int(parts[4]), int(parts[5])))
        elif category == "Motorcycle":
            reconstructed_vehicles.append(Motorcycle(parts[1], parts[2], int(parts[3]), int(parts[4]), parts[5]))
    return reconstructed_vehicles

# 6 Araç oluşturma
fleet_data = [
    Car("V001", "Tesla Model 3", 2023, "Electric", 4),
    Car("V002", "Toyota Corolla", 2018, "Petrol", 4),
    Truck("T101", "Volvo FH16", 2019, 25000, 6),
    Truck("T102", "Mercedes Actros", 2021, 18000, 4),
    Motorcycle("M301", "Yamaha R1", 2024, 998, "Sport"),
    Motorcycle("M302", "Harley Davidson", 2015, 1200, "Cruiser")
]


save_fleet_to_file(fleet_data, "fleet.txt")
loaded_items = load_fleet_from_file("fleet.txt")

print("All Vehicles ---")
for item in loaded_items:
    print(item)

print("\nRecent Vehicles (Last 4 Years) ---")
for item in loaded_items:
    if item.is_new(4):
        print(item)

print("\nElectric Cars Only ---")
for item in loaded_items:
    if isinstance(item, Car) and item.fuel_type == "Electric":
        print(item)
