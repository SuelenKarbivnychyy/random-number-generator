import time

class Number_generate:

    def __init__(self):
        pass

    def generator(self, stop_number):
        """Generates a random number"""
        
        current_time = round(time.time()*1000)
        print(f"The random generated number is: {current_time%stop_number}")       

play = Number_generate()

play.generator(20)
