#TODO: Build a random number generator
#Many languages contain classes that allow for the functionality of a random number generator, but we want you to create your own method that does this.

import random

class Number_generator:

    def __init__(self):
        pass

    def generator(self):
        """generates a random number"""

        print(f"The number is {random.randint(range(1,1000))}")

play = Number_generator()

play.generator()
