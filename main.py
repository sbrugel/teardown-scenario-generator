from tkinter import *
import random

class Window():
    '''
    Gets a random number in the specified range.

    Params:
        min (int): Minimum number (included in range)
        max (int): Maximum number (included in range)
        multiplier (int): Number to multiply result by (defaults to 1)
        exclude ([int]): A list of numbers to exclude when randomizing (defaults to none)

    Returns:
        (int): Random number
    '''
    def random_number(self, min: int, max: int, multiplier = 1, exclude = []) -> int:
        x = random.randrange(min, max + 1) * multiplier
        while x in exclude:
            x = random.randrange(min, max + 1) * multiplier
        return x

    def create(self):
        first_prompts = [   ("Destroy " + str(self.random_number(3, 7)) + " structures"), 
                            ("Level " + str(self.random_number(3, 7)) + " structures to " + str(self.random_number(1, 3, 25)) + "% of their original height"),
                            ("Wreck " + str(self.random_number(3, 7)) + " vehicles"),
                            ("Destroy as much as possible within " + str(self.random_number(1, 3, 5)) + " minutes")]

        second_prompts = [  (""),
                            (" within " + str(self.random_number(1, 3, 5)) + " minutes"),
                            (" using only explosives"),
                            (" without explosives"),
                            (" using only vehicles"),
                            (" using only fire tools")]

        third_prompts = [   (""),
                            (" destroying as little else as possible"),
                            (" and clean up as much of the damage as possible afterwards")]

        first_index = second_index = third_index = 0
        first_index = self.random_number(0, len(first_prompts) - 1)
        if first_index == 3:
            second_index = self.random_number(0, len(second_prompts) - 1, 1, [1])
            third_index = self.random_number(0, len(third_prompts) - 1, 1, [1])
        else:
            second_index = self.random_number(0, len(second_prompts) - 1)
            third_index = self.random_number(0, len(third_prompts) - 1)
        
        prompt = first_prompts[first_index] + second_prompts[second_index] + third_prompts[third_index]
        self.text_lb.configure(text = prompt)

    def __init__(self):
        # set up window
        self.root = Tk()
        self.root.title("Teardown Scenario Generator")
        self.root.geometry("1000x350")
        self.root.configure(bg='black')

        # set up components
        self.create_btn = Button(self.root, text = "Create!", command = self.create, bg = "lightblue")
        self.create_btn.place(x = 20, y = 20)

        self.text_lb = Label(self.root, anchor = W, text = "", foreground = "white", background = "black")
        self.text_lb.place(x = 20, y = 50)

        # launch the window
        self.root.mainloop()

win = Window()