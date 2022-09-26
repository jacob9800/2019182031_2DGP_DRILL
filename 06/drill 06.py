from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

## (x,y) => (r.cos(), r.sin())

def render_all(x,y):
     clear_canvas_now()
     grass.draw_now(400,30)
     character.draw_now(x,y)
     delay(0.01)


def run_circle():
    print("circle")

    cx,cy,r = 400,300,200
    for deg in range(-90,270+1,5):
        x = cx + r*math.cos(deg/360*2*math.pi)
        y = cy + r*math.sin(deg/360*2*math.pi)
        render_all(x,y)
        

def run_rectangle():
    print("rectangle")
    #bottom line
    for x in range(50, 750+1, 10):
        render_all(x,90)
    #right line
    for y in range(90, 550+1, 10):
        render_all(750,y)
    #top line    
    for x in range(750,50-1,-10):
        render_all(x,550)
    #left line
    for y in range(550, 90-1, -10):
        render_all(50,y)


while True :
    run_circle()
    run_rectangle()
    #break




##while(True):
##    x = 0
##    y = 90
##    while(x < 800):
##        clear_canvas_now()
##        grass.draw_now(400,30)
##        character.draw_now(x,90)
##        x = x+2
##        delay(0.01)
##
##    while(y<600):
##        clear_canvas_now()
##        grass.draw_now(400,30)
##        character.draw_now(800, y)
##        y = y+2
##        delay(0.01)
##
##    while(x > 0 and y > 90):
##        clear_canvas_now()
##        grass.draw_now(400,30)
##        character.draw_now(x, 600)
##        x = x-2
##        delay(0.01)
##
##    while(y>90 and x == 0):
##        clear_canvas_now()
##        grass.draw_now(400,30)
##        character.draw_now(0, y)
##        y = y-2
##        delay(0.01)
##
##    i = 0
##    while(i<360):
##        clear_canvas_now()
##        grass.draw_now(400,30)
##        character.draw_now(x, y)
##        x = 400 + math.cos(i/360*2*math.pi) * 200
##        y = 300 + math.sin(i/360*2*math.pi) * 200
##        i = i+1
##        delay(0.01)


close_canvas()
