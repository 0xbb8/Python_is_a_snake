# OOP: Inheritance - Polymorphism

# Example - 1

import time

class TrackedVehicle:
    def controltrack(left, stop):
        pass

    def turn(left):
        controltrack(left, True)
        time.sleep(0.25)
        controltrack(left, False)


class WheeledVehicle:
    def turnfrontwheels(left, on):
        pass
    
    def turn(left):
        turnfrontwheels(left, True)
        time.sleep(0.25)
        turnfrontwheel(left, False)

# Example - 2
# Keeping the common function in a superclass and other 'abstract' function in the subclasses.
import time

class Vehicle:
    def changedirection(left, on):
        pass

    def turn(left):
        changedirection(left, True)
        time.sleep(0.25)
        changedirection(left, False)

class TrackedVehicle(Vehicle):
    def controltrack(left, stop):
        pass

    def changedirection(left, on):
        controltrack(left, on)

class WheeledVehicle(Vehicle):
    def turnfrontwheels(left, on):
        pass

    def changedirection(left, on):
        turnfrontwheels(left, on)

# Example - 3
# NOTE: Composition is the process of composing an object using other different objects.
import time

class Tracks:
    def changedirection(self, left, on):
        print("tracks: ", left, on)

class Wheels:
    def changedirection(self, left, on):
        print("wheels: ", left, on)

class Vehicle:
    def __init__(self, controller):
        self.controller = controller

    def turn(self, left):
        self.controller.changedirection(left, True)
        time.sleep(0.25)
        self.controller.changedirection(left, False)

wheeled = Vehicle(Wheels())
tracked = Vehicle(Tracks())

wheeled.turn(True)
t racked.turn(False)

# NOTE:
"""
It can be said that:

    -> inheritance extends a class's capabilities by adding new components and modifying existing ones;
       in other words, the complete recipe is contained inside the class itself and all its ancestors;
       the object takes all the class's belongings and makes use of them;
    
    -> composition projects a class as a container able to store and use other objects 
       (derived from other classes) where each of the objects implements a part of a desired class's behavior.

"""
