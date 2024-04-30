"""
    Name: spaceship.py
    Author: Triumph Ogbonnia
    Created: 4/29/24
    Purpose: spaceship class and method
"""

class Spaceship:
    """Spaceship Class"""
    # Initialize the spaceship attributes
    def __init__(self, name, fuel_level, speed, cargo_capacity):
        self.name = name
        self.fuel_level = fuel_level
        self.speed = speed
        self.cargo_capacity = cargo_capacity
    
    # Method to refuel the spaceship
    def refuel(self, amount):
        self.fuel_level += amount
        print(f"{self.name} has been refueled. Current fuel level: {self.fuel_level}")
    
    # Method to accelerate the spaceship
    def accelerate(self, increment):
        self.speed += increment
        print(f"{self.name} is now traveling at {self.speed} MPH.")
    
    # Method to decelerate the spaceship
    def decelerate(self, decrement):
        # If the current speed greater than 0, decrease speed
        if self.speed - decrement >= 0:
            self.speed -= decrement
            print(f"{self.name} is now traveling at {self.speed} MPH.")
        else:
            # Otherwise, tell the user
            print(f"{self.name} cannot decelerate further.")
    
    # Method to load cargo onto the spaceship
    def load_cargo(self, cargo):
        # If the cargo is less than the capacity, add the cargo
        if cargo <= self.cargo_capacity:
            print(f"{cargo} tons of cargo loaded onto {self.name}.")
        else:
            # Otherwise, tell the user that there is not enough capacity
            print(f"Not enough capacity on {self.name} to load {cargo} tons of cargo.")