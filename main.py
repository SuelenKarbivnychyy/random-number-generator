import random

class Number_generator:

    def __init__(self):
        pass

    def generator(self):
        """Generates a random number"""

        generated_num = random.randint(1, 1000)
        print(f"The number is {generated_num}")

play = Number_generator()

play.generator()
