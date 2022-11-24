import random
from pico2d import *
import game_world
import server

class Ball:
    image = None

    def __init__(self):
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 1800), random.randint(0, 1100)

    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom

        self.image.draw(sx, sy)

    def update(self):
        if self.x <= 0:
            self.x = 50

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10


    def handle_collision(self, other, group):
        if group == 'boy:ball':
            game_world.remove_object(self)