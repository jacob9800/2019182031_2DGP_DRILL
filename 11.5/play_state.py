# 게임 플레이 상태
from pico2d import *
import game_framework
import logo_state
import title_state
import item_state
import add_delete_state
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir = 1 # 오른쪽
        self.image = load_image('animation_sheet.png')
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')
        self.item = None
        self.speed = random.randint(10, 30) / 10

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * self.speed
        if self.x > 800:
            self.x = 800
            self.dir = -1 # 왼쪽
        elif self.x < 0:
            self.x = 0
            self.dir = 1 # 오른쪽

    def draw(self):
        if self.item == 'BigBall':
            self.big_ball_image.draw(self.x+10, self.y+50)
        elif self.item == 'Ball':
            self.ball_image.draw(self.x + 10, self.y + 50)

        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_i:
                game_framework.push_state(item_state)
            elif event.key == SDLK_b:
                game_framework.push_state(add_delete_state)



boy = None # c로 따지면 NULL과 동일
grass = None
running = True

# 게임 초기화 함수
def enter():
    global boy, grass, running
    boy = [Boy() for i in range(1)]
    grass = Grass()
    running = True

# 게임 종료 함수
def exit():
    global boy, grass
    del boy
    del grass

def update():
    global boy
    for kid in boy:
        kid.update()


def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    grass.draw()
    for kid in boy:
       kid.draw()


def pause():
    pass

def resume():
    pass