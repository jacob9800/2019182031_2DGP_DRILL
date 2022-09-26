from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('sprite.png')
character2 = load_image('spriteno2.png')

def run_front():
    frame = 0
    frame2 = 0
    a = 0
    for x in range(0, 790, 5):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 90, 260, 100, 132, x, 90)  ## x좌표(사진), y좌표(사진), 출력 넓이, 출력 높이, 화면 x,y좌표
        if(x >= 100):
            character2.clip_draw(frame2*96,0,95,104,a,90)
            a += 5
        update_canvas()
        frame2 = (frame2 + 1) % 10
        frame = (frame + 1) % 12
        delay(0.03)
        get_events()

def run_down():
    frame = 0
    frame2 = 0
    a = 0
    for y in range(0, 510, 5):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 90, 130, 100, 132, 20, 600-y)  ## x좌표(사진), y좌표(사진), 출력 넓이, 출력 높이, 화면 x,y좌표
        if (y >= 100):
            character2.clip_draw(frame2 * 96, 312, 95, 104, 20, 600-a)
            a += 5
        update_canvas()
        frame2 = (frame2 + 1) % 10
        frame = (frame + 1) % 12
        delay(0.03)
        get_events()

def run_up():
    frame = 0
    frame2 = 0
    a = 0
    for y in range(0, 510, 5):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 90, 0, 100, 132, 790, 90+y)  ## x좌표(사진), y좌표(사진), 출력 넓이, 출력 높이, 화면 x,y좌표
        if (y >= 100):
            character2.clip_draw(frame2 * 96, 102, 95, 104, 790, 90+a)
            a += 5
        update_canvas()
        frame2 = (frame2 + 1) % 10
        frame = (frame + 1) % 12
        delay(0.03)
        get_events()

while(1):
    run_front()
    run_up()
    run_down()
    #break; # use only to stop loop

close_canvas()
