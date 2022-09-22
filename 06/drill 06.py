from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')





while(True):
    x = 0
    y = 90
    while(x < 800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x = x+2
        delay(0.01)

    while(y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(800, y)
        y = y+2
        delay(0.01)

    while(x > 0 and y > 90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, 600)
        x = x-2
        delay(0.01)

    while(y>90 and x == 0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(0, y)
        y = y-2
        delay(0.01)

    i = 0
    while(i<360):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        x = 400 + math.cos(i/360*2*math.pi) * 200
        y = 300 + math.sin(i/360*2*math.pi) * 200
        i = i+1
        delay(0.01)


close_canvas()
