from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.color("Red")
        self.penup()
        self.back_to_start()
        self.showturtle()
        self.setheading(90)

    def go_up(self):
        self.setheading(90)
        if self.ycor() < 280:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
        else:
            self.goto(self.xcor(), 380)

    def go_down(self):
        self.setheading(270)
        if self.ycor() > -250:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
        else:
            self.goto(self.xcor(), -380)

    #def go_left(self):
    #    self.setheading(LEFT)
    #    if self.xcor() < 250:
    #        new_x = self.xcor() + MOVE_DISTANCE
    #        self.goto(self.ycor(), new_x)
    #    else:
    #        self.goto(self.ycor(), 380)

#    def go_right(self):
#        self.setheading(RIGHT)

    def is_finished(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def back_to_start(self):
        self.goto(STARTING_POSITION)