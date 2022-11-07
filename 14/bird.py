from pico2d import *
import game_world
from ball import Ball
import game_framework
import random



PIXEL_PER_METER = (10.0 / 0.3) # 10 pixel 30 cm
RUN_SPEED_KMPH = 50.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5

class RUN:
    def enter(self, event):
        print('ENTER RUN')
        if self.face_dir == 1:
            self.dir = 1

    def exit(self, event):
        print('EXIT RUN')

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

        if self.face_dir == 1 and self.x >= 800:
            self.x = 800
            self.dir = -1
            self.face_dir = -1
        elif self.face_dir == -1 and self.x <= 0:
            self.x = 0
            self.dir = 1
            self.face_dir = 1

        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(0, self.x, 1600)

    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(int(self.frame)*183, 330, 183, 168, 0, '', self.x, self.y, 150, 100)
        elif self.face_dir == -1:
            self.image.clip_composite_draw(int(self.frame)*183, 330, 183, 168, 0, 'h', self.x, self.y, 150, 100)


class Bird:

    def __init__(self, x = 400, y = 300):
        self.x, self.y = x, y
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('bird_animation.png')

        self.timer = 100

        self.event_que = []
        self.cur_state = RUN
        self.cur_state.enter(self, None)
        self.font = load_font('ENCR10B.TTF', 16)

    def update(self):
        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                pass
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)

    def add_event(self, event):
        self.event_que.insert(0, event)


next_state = {RUN:  {}}