from microbit import *

class Snake:
    """ This class contains the functions that operate
        on our game as well as the state of the game.
        It's a handy way to link the two.
    """

    def __init__(self):
        """ Special function that runs when you create
            a "Snake", ie. when you run
                game = Snake()
            init stands for "Initialisation"
        """
        ## UNCOMMENT AND FILL IN THE # LINES BELOW WITH START VALUES
        ## direction is a string with up, down, left or right
        # self.direction =
        ## snake is a list of the pixels that the snake is at
        # self.snake = [[2, 2]]
        ## food is the co-ords of the current food
        # self.food =
        ## whether or not to end the game (boolean)
        # self.end =
        pass

    def handle_input(self):
        """ We'll use this function to take input from the
            user to control which direction the snake is going
            in.
        """
        pass

    def update(self):
        """ This function will update the game state
            based on the direction the snake is going.
        """
        # The line below makes a copy of the head of the snake
        # you will be working with that copy in this function
        # new_head = list(self.snake[-1])
        pass

    def draw(self):
        """ This makes the game appear on the LEDs. """
        pass

# game is an "instance" of Snake
game = Snake()

# this is called our "game loop" and is where everything
# happens
while True:
    game.handle_input()
    game.update()
    game.draw()
    # this makes our micro:bit do nothing for 500ms
    sleep(500)
