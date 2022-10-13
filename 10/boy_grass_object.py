import random
from pico2d import *

# Game object class here

class Grass: # 잔디 클래스
    def __init__(self): # 생성자 : 객체의 생성시 초기값
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy: # 소년 클래스(완성)
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x, self.y = random.randint(10,300), 90 # 초기 x축 좌표
        self.frame = random.randint(0,7) # 초기 프레임

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

    def update(self): # 소년의 행위 구현(왼쪽 -> 오른쪽)
        self.x += 5 # 속성 값을 바꿈으로써, 행위를 구현(우측으로 이동)
        self.frame = (self.frame + 1) % 8

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code(게임 월드 초기화 코드)
open_canvas()

# team = []
# for i in range(11+1):
#     team += [Boy()]

team = [Boy() for i in range(11)] # list comprehension을 통한 코드 간략화
grass = Grass() # 잔디 객체 생성

running = True

# game main loop code
while running:

    handle_events()

    # Game logic
    # grass에 대한 상호작용 : 안움직이니까 굳이 필요 X
    for boy in team:
       boy.update() # 소년의 상호작용(team 11명 전부 업데이트)


    # Game drawing
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
        update_canvas() # 11명이 동일 위치에 서있기 때문에 1명으로 보인다.

    delay(0.05)

# finalization code

