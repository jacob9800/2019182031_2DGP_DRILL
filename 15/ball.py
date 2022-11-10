import random
from pico2d import *
import game_world

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1600), 70, 0

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed
        if self.y <= 50:
         self.y = 70

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def stop(self):
        self.fall_speed = 0


    def handle_collision(self, other, group):
        if group == 'boy:ball':
            game_world.remove_object(self)
        if group == 'grass:ball':
            self.stop()

class BigBall(Ball): # Ball을 상속받는 Bigball 클래스 생성
    MIN_FALL_SPEED = 50
    MAX_FALL_SPEED = 200
    image = None

    def __init__(self):
        if BigBall.image == None:
            BigBall.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1600-1), 500
        self.fall_speed = random.randint(BigBall.MIN_FALL_SPEED, BigBall.MAX_FALL_SPEED)

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20


