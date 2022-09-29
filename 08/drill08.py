from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global count
    global idlecount
    global dir
    global ydir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                count = 0
                idlecount = 1
                dir += 1
            elif event.key == SDLK_LEFT:
                count = 1
                idlecount = 1
                dir -= 1
            elif event.key == SDLK_UP:
                idlecount = 1
                ydir += 1
            elif event.key == SDLK_DOWN:
                idlecount = 1
                ydir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                idlecount = 0
            elif event.key == SDLK_LEFT:
                dir += 1
                idlecount = 0
            elif event.key == SDLK_UP:
                ydir -= 1
                idlecount = 0
            elif event.key == SDLK_DOWN:
                ydir += 1
                idlecount = 0


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
count = 0
idlecount = 0
x = 524
y = 512
frame = 0
dir = 0 # x축 상의 캐릭터의 방향, -1 : 왼쪽, 0 : 중립, +1 : 오른쪽
ydir = 0 # y축 상의 캐릭터의 방향, -1 : 아래쪽, 0 : 중립, +1 : 위쪽

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if idlecount == 0: # 가만히 서있을 경우
        if count == 0:
            character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)
        elif count == 1:
            character.clip_draw(frame * 100, 100 * 2, 100, 100, x, y)

    if count == 0 and idlecount == 1: # 달리기 시작
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
        if(x >= KPU_WIDTH):
            x = KPU_WIDTH
        if (y >= KPU_HEIGHT):
            y = KPU_HEIGHT
        if (y <= 0):
            y = 0
    elif count == 1 and idlecount == 1:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
        if (x <= 0):
            x = 0
        if (y >= KPU_HEIGHT):
            y = KPU_HEIGHT
        if (y <= 0):
            y = 0

    update_canvas()

    handle_events()
    frame = (frame + 1) % 8
    x += dir*5
    y += ydir*5
    delay(0.01)

close_canvas()