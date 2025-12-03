class Car:
    def __init__(self, brand, model, year, fuel_level, is_running, fuel_capcity = 0):
        self.brand = brand
        self.model = model
        self.year = year
        self.fuel_capacity = fuel_capcity
        self.fuel_level = fuel_level
        self.is_running = is_running

        print("Welcome to young's car yard.")

    def start(self):
        self.is_running = True
        if self.is_running:
            print(f"The {self.brand} {self.model} {self.year} engine is running")
        else:
            print(f"Check the fuel level and start the {self.brand} {self.model} {self.year} engine.")

    def stop(self):
        self.is_running = True
        if self.is_running:
            print(f"The {self.brand} {self.model} {self.year} engine is not running")
        else:
            print(f"The {self.brand} {self.model} {self.year} engine is now off.")

    def refuel(self):
        if self.fuel_level < 0.25:
            print(f"please refuel {self.brand} {self.model} {self.year}")
        else:
            print(f"The {self.brand} {self.model} {self.year} car is ready for a drive")

    def drive(self):
        self.is_running = False
        if self.is_running:
            print(f"The {self.brand} {self.model} {self.year} can be driven off")
        else:
            print("Start the car to drive")

    def display_car_info(self):
        print(f"The selected car is a {self.brand} {self.model} {self.year} with {self.fuel_level} the tank fuel, and a {self.fuel_capacity} litre fuel capacity.")

mycar = Car("Toyota", "Avensis", 2019, 1/5, True, 60)
mycar.display_car_info()
mycar.refuel()
mycar.stop()
