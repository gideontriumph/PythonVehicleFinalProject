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
        print(f"{self.name} has been refueled.\nCurrent fuel level: {self.fuel_level}")
    
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
           
# Define the main function 
def main():
    
    # Get spaceship input from the user
    name = input("Enter spaceship name >> ")
    fuel_level = float(input("Enter current fuel level >> "))
    speed = float(input("Enter current speed >> "))
    cargo_capacity = float(input("Enter cargo capacity (tons) >> "))
    print(f"{name} has fuel level {fuel_level} with a current speed of {speed} MPH and cargo capacity {cargo_capacity}")

    # Create a spaceship object with user input details
    spaceship = Spaceship(name, fuel_level, speed, cargo_capacity)
    
    # While loop
    while True:
        # Display menu for spaceship operations
        print("\n==== Spaceship Operations ====")
        print("Press X to e(x)it")
        print("1. Refuel")
        print("2. Accelerate")
        print("3. Decelerate")
        print("4. Load Cargo")

        # Get user choice
        choice = input("\nEnter your choice >> ")
        
        # Execute corresponding operation based on user choice
        if choice == '1':
            amount = float(input("Enter the amount of fuel to refuel >> "))
            spaceship.refuel(amount)
        elif choice == '2':
            increment = float(input("Enter acceleration increment (MPH) >> "))
            spaceship.accelerate(increment)
        elif choice == '3':
            decrement = float(input("Enter deceleration decrement (MPH) >> "))
            spaceship.decelerate(decrement)
        elif choice == '4':
            cargo = float(input("Enter the amount of cargo to load >> "))
            spaceship.load_cargo(cargo)
        elif choice == 'x'.lower():
            # Exit the program if user chooses
            print("\nExiting program. . .")
            break
        else:
            # Handle exception
            print("Invalid choice. Please try again.")


# Call the main function
if __name__ == "__main__":
    main()