# 게임 플레이 상태
from pico2d import *
import game_framework
import logo_state
import title_state

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
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir *2
        if self.x > 800:
            self.x = 800
            self.dir = -1 # 왼쪽
        elif self.x < 0:
            self.x = 0
            self.dir = 1 # 오른쪽

    def draw(self):
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)



boy = None # c로 따지면 NULL과 동일
grass = None
running = True

# 게임 초기화 함수
def enter():
    global boy, grass, running
    boy = Boy()
    grass = Grass()
    running = True

# 게임 종료 함수
def exit():
    global boy, grass
    del boy
    del grass

def update():
    boy.update()

def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()