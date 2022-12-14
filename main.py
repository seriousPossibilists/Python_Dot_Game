"""
Program for a simple dot game
"""

#Import the arcade module
import arcade
#Import the dataclass module
from dataclasses import dataclass

#Declaring constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
NUM_DOTS = 5
SCL = SCREEN_WIDTH / (NUM_DOTS * 2) 
DOTS_ARR = []
RADIUS = 5
LINE_ARR = []


@dataclass
class Point:
    x: int
    y: int


class Game(arcade.Window):
    
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        createDotsArray()
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        renderDotsArray()
        line()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            checkDotPress(x, y)


def createDotsArray():
    for x in range(5):
        for y in range(5):
            DOTS_ARR.append(Point(x * SCL + (SCL * 3), y * SCL + (SCL * 3)))

def renderDotsArray():
  for i in range(len(DOTS_ARR)):
        instance = DOTS_ARR[i]
        arcade.draw_circle_filled(instance.x, instance.y, RADIUS, arcade.csscolor.WHITE)

def checkDotPress(x, y):
    for i in range(len(DOTS_ARR)):
        dSquared = ((x - DOTS_ARR[i].x) * (x - DOTS_ARR[i].x)) + ((y - DOTS_ARR[i].y) * (y - DOTS_ARR[i].y))
        rSquared = RADIUS * RADIUS
        if(dSquared <= rSquared):
            LINE_ARR.append(DOTS_ARR[i])
            line()

def line():
    if(len(LINE_ARR) == 2):
            print(LINE_ARR[0], LINE_ARR[1])
            drawLine(LINE_ARR[0].x, LINE_ARR[0].y, LINE_ARR[1].x, LINE_ARR[1].y)
            LINE_ARR.clear()

def drawLine(sx, sy, ex, ey):
    arcade.draw_line(sx, sy, ex, ey, arcade.color.WHITE)

def main():
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Game")
    arcade.run()

main()
