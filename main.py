"""
Program for a simple dot game
"""

import math
import arcade
from dataclasses import dataclass

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
NUM_DOTS = 5
SCL = SCREEN_WIDTH / (NUM_DOTS * 2) 
DOTS_ARR = []
RADIUS = 5
LINE_ARR =[]
PLAYER_1_SCORE = 0
PLAYER_2_SCORE = 0
TURN = 0
PREV_LINES = 0
PREV_BOXES = 0
GAME_END = 0

@dataclass
class Point:
    x: int
    y: int
    connectedTop: bool
    connectedRight: bool
    connectedBottom: bool
    connectedLeft:bool
    
class Game(arcade.Window):
    
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        createDotsArray()
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        renderDotsArray()
        if(len(LINE_ARR) >= 2):
               for i in range(int(len(LINE_ARR) / 2)):
                 if(LINE_ARR[2 * i].x == LINE_ARR[2 * i + 1].x or LINE_ARR[2 * i].y == LINE_ARR[2 * i + 1].y):
                    if(abs(LINE_ARR[2 * i].x - LINE_ARR[2 * i + 1].x) == 60 or abs(LINE_ARR[2 * i].y - LINE_ARR[2 * i + 1].y) == 60):
                        line(LINE_ARR[2 * i],LINE_ARR[2 * i + 1])
                    else:
                        line(LINE_ARR[2 * i],LINE_ARR[2 * i + 1])
                        if(len(LINE_ARR) % 2 == 0): 
                            LINE_ARR.pop(len(LINE_ARR) - 1)
                            LINE_ARR.pop(len(LINE_ARR) - 1)

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            checkDotPress(x, y)
        

def createDotsArray():
    for x in range(5):
        for y in range(5):
            DOTS_ARR.append(Point(x * SCL + (SCL * 3), y * SCL + (SCL * 3), False, False, False, False))

def renderDotsArray():
  for i in range(len(DOTS_ARR)):
        instance = DOTS_ARR[i]
        arcade.draw_circle_filled(instance.x, instance.y, RADIUS, arcade.csscolor.WHITE)

def checkDotPress(x, y):
    global LINE_ARR
    for i in range(len(DOTS_ARR)):
        dSquared = ((x - DOTS_ARR[i].x) * (x - DOTS_ARR[i].x)) + ((y - DOTS_ARR[i].y) * (y - DOTS_ARR[i].y))
        rSquared = RADIUS * RADIUS
        if(dSquared <= rSquared):
            LINE_ARR.append(DOTS_ARR[i])

def checkBox():
    global TURN
    global PREV_BOXES
    global PLAYER_1_SCORE
    global PLAYER_2_SCORE
    num_boxes = 0
    for i in range(len(DOTS_ARR)):
        if(DOTS_ARR[i].connectedBottom == True and DOTS_ARR[i].connectedRight == True and DOTS_ARR[i - 1].connectedRight == True and DOTS_ARR[i + 5].connectedBottom == True):
            num_boxes += 1
    if(num_boxes > PREV_BOXES):
        if TURN == 0:
            TURN = 1
        else:
            TURN = 0  
        print("New box formed")
        if TURN == 0:
            PLAYER_1_SCORE += (num_boxes - PREV_BOXES)
        else:
            PLAYER_2_SCORE += (num_boxes - PREV_BOXES)
        PREV_BOXES = num_boxes
        checkScore()

def checkScore():
    global GAME_END
    global PREV_BOXES
    global PLAYER_1_SCORE
    global PLAYER_2_SCORE
    print(PLAYER_1_SCORE, PLAYER_2_SCORE)
    if(PREV_BOXES == 16 and GAME_END == 0):
        print("All possible boxes formed")
        if(PLAYER_1_SCORE > PLAYER_2_SCORE):
            print("Player 1 won!")

        elif(PLAYER_1_SCORE == PLAYER_2_SCORE):
            print("Draw!")

        else:
            print("Player 2 won!")
        GAME_END = 1


def line(pt1, pt2):
    global PREV_LINES
    global TURN
    num_lines = math.floor(len(LINE_ARR) / 2)
    if(num_lines > PREV_LINES):
        PREV_LINES = num_lines
        if TURN == 0:
            TURN = 1
        else:
            TURN = 0      
    if(pt1.x > pt2.x):
        pt1.connectedLeft = True
        pt2.connectedRight = True
    elif(pt1.x < pt2.x):
        pt1.connectedRight = True
        pt2.connectedLeft = True
    elif(pt1.y > pt2.y):
        pt1.connectedBottom = True
        pt2.connectedTop = True
    elif(pt1.y < pt2.y):
        pt1.connectedTop = True
        pt2.connectedBottom = True
    checkBox()
    arcade.draw_line(pt1.x, pt1.y, pt2.x, pt2.y, arcade.color.WHITE, 3)
        
def main():
    window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, "Game")
    arcade.run()
    print(PLAYER_1_SCORE, PLAYER_2_SCORE)
main()
