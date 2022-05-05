import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


scoreboard = Scoreboard()
cm = CarManager()
p = Player()
s = Screen()
s.title("Turtle Crossing Waaah!!!")
s.setup(width=600, height=600)
s.tracer(0)

s.listen()
s.onkeypress(p.go_up, "Up")
s.onkeypress(p.go_down, "Down")
#s.onkeypress(p.go_left, "Left")
#s.onkeypress(p.go_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    s.update()

    cm.create_car()
    cm.move_cars()

    for car in cm.all_cars:
        if car.distance(p) < 20:
            scoreboard.game_over()
            game_is_on = False

    if p.is_finished():
        p.back_to_start()
        cm.level_up()
        scoreboard.level_up_score()

s.exitonclick()
