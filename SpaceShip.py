"""
    Name: SpaceShip.py
    Author: Triumph Ogbonnia
    Created: 4/29/24
    Purpose: spaceship class and method
"""
from rich.panel import Panel
from rich.console import Console
from rich import print

# Initialize rich console
console = Console()

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
        print(f"[bold blue]{self.name} has been refueled.\nCurrent fuel level: {self.fuel_level}")
    
    # Method to accelerate the spaceship
    def accelerate(self, increment):
        self.speed += increment
        print(f"[bold blue]{self.name} is now traveling at {self.speed} MPH.")
    
    # Method to decelerate the spaceship
    def decelerate(self, decrement):
        # If the current speed greater than 0, decrease speed
        if self.speed - decrement >= 0:
            self.speed -= decrement
            print(f"[bold blue]{self.name} is now traveling at {self.speed} MPH.")
        else:
            # Otherwise, tell the user
            print(f"[bold cyan]{self.name} cannot decelerate further.")
    
    # Method to load cargo onto the spaceship
    def load_cargo(self, cargo):
        # If the cargo is less than the capacity, add the cargo
        if cargo <= self.cargo_capacity:
            print(f"[bold blue]{cargo} tons of cargo loaded onto {self.name}.")
        else:
            # Otherwise, tell the user that there is not enough capacity
            print(f"[bold cyan]Not enough capacity on {self.name} to load {cargo} tons of cargo.")
            
# Define the main function 
def main():
    # Print progam title using rich
    console.print(
        Panel.fit(
            "    ===    Adam's Spaceship   ===    ",
            subtitle=" By Triumph Ogbonnia ",
            style="bold blue"
        )
    )
    
    # Get spaceship input from the user
    name = console.input("\n[bold blue]Enter spaceship name >> ")
    fuel_level = float(console.input("[bold blue]Enter current fuel level >> "))
    speed = float(console.input("[bold blue]Enter current speed >> "))
    cargo_capacity = float(console.input("[bold blue]Enter cargo capacity (tons) >> "))
    # Print spaceship details to the console
    print(f"\n[bold cyan]{name} has fuel level {fuel_level} with a current speed of {speed}MPH and {cargo_capacity} tons of cargo capacity")
    
    # Display menu for spaceship operations
    print()
    console.print(
        Panel.fit(
            "==== Spaceship Operations ====",
            subtitle="Press X to e(x)it",
            style="bold blue"))

    # Create a spaceship object with user input details
    spaceship = Spaceship(name, fuel_level, speed, cargo_capacity)
    
    # While loop
    while True:
        print()
        print("[yellow]1.[yellow/] [bold cyan]Refuel")
        print("[yellow]2.[yellow/] [bold cyan]Accelerate")
        print("[yellow]3.[yellow/] [bold cyan]Decelerate")
        print("[yellow]4.[yellow/] [bold cyan]Load Cargo")

        # Get user choice
        choice = console.input("\n[bold cyan]Enter your choice >> ")
        
        # Execute corresponding operation based on user choice
        if choice == '1':
            amount = float(console.input("[bold blue]Enter the amount of fuel to refuel >> "))
            spaceship.refuel(amount)
        elif choice == '2':
            increment = float(console.input("[bold blue]Enter acceleration increment (MPH) >> "))
            spaceship.accelerate(increment)
        elif choice == '3':
            decrement = float(console.input("[bold blue]Enter deceleration decrement (MPH) >> "))
            spaceship.decelerate(decrement)
        elif choice == '4':
            cargo = float(console.input("[bold blue]Enter the amount of cargo to load >> "))
            spaceship.load_cargo(cargo)
        elif choice.lower() == 'x':
            # Exit the program if user chooses x
            print("[bold green]\nExiting program. . .")
            break
        else:
            # Handle invalid input exception
            print("[bold red]Invalid choice. Please try again.")


# Call the main function
if __name__ == "__main__":
    main()