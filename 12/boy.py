from pico2d import *

# 이벤트 정의
# RD, LD, RU, LU = 0, 1, 2, 3
RD, LD, RU, LU, TIMER, ARI = range(6) # TIMER 이벤트 추가, Auto_Run in 추가

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYUP, SDLK_RIGHT) : RU,
    (SDL_KEYUP, SDLK_LEFT) : LU,
    (SDL_KEYDOWN, SDLK_a) : ARI,
}

# 스테이트를 구현(class를 이용해서)
class IDLE:
    @staticmethod
    def enter(self,event):
        print("ENTER IDLE")
        self.dir = 0 # 정지 상태
        self.timer = 1000 # 타이머 초기화
        pass

    @staticmethod
    def exit(self):
        print("EXIT IDLE")
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1 # 시간 1씩 감소
        if self.timer == 0: # 시간이 다 되면
            self.add_event(TIMER) # 타이머 이벤트를 큐에 삽입
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        pass

class RUN:
    @staticmethod
    def enter(self, event):
        print("ENTER RUN")


        # 어떤 이벤트 때문에, RUN으로 들어왔는지 확인하고, 그 이벤트에 따라서 실제 방향을 결정
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        pass

    @staticmethod
    def exit(self):
        print("EXIT RUN")
        # RUN 상태를 나갈 때, 캐릭터의 얼굴 방향을 저장해둠
        self.face_dir = self.dir
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame+1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800) # 0부터 800까지로 고정
        pass

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        pass

class SLEEP:
    @staticmethod
    def enter(self, event):
        print("ENTER SLEEP")
        self.dir = 0  # 정지 상태
        pass

    @staticmethod
    def exit(self):
        print("EXIT SLEEP")
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100, 3.141592/2, '', self.x-25, self.y-25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592/2, '', self.x+25, self.y-25, 100, 100)
        pass

class AUTO_RUN:
    @staticmethod
    def enter(self, event):
        print("ENTER AUTO_RUN")

        # 어떤 이벤트 때문에, RUN으로 들어왔는지 확인하고, 그 이벤트에 따라서 실제 방향을 결정
        if event == ARI:
            if self.face_dir == 1:
                self.dir += 1
            elif self.face_dir == -1:
                self.dir -= 1

    @staticmethod
    def exit(self):
        print("EXIT AUTO_RUN")
        # RUN 상태를 나갈 때, 캐릭터의 얼굴 방향을 저장해둠
        self.dir = 0
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        if self.x >= 800 :
            self.x = 800
            self.dir = -1
            self.face_dir = -1
        elif self.x <= 0:
            self.x = 0
            self.dir = 1
            self.face_dir = 1
        self.x += self.dir
        self.x = clamp(0, self.x, 800)  # 0부터 800까지로 고정
        pass

    @staticmethod
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        pass


# 상대 변환

next_state = {
    SLEEP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: RUN, ARI: AUTO_RUN},
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, ARI: AUTO_RUN},
    RUN: {RU: IDLE, LU: IDLE, LD: IDLE, RD: IDLE, TIMER: RUN, ARI: AUTO_RUN},
    AUTO_RUN: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: RUN, ARI: IDLE}
}

class Boy:
    def __init__(self):
        self.x, self.y = 300, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []

        # 첫번째 초기 상태 설정과, entry action 수행
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def add_event(self, key_event):
        self.q.insert(0, key_event)

    def handle_events(self, event): # 키 입력 이벤트
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)



        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1

    def update(self):
        self.cur_state.do(self)

        if self.q: # 만약에 list 'q'에 멤버가 존재한다면 그 이벤트를 제거한다.
            event = self.q.pop() # 이벤트 확인한 후
            self.cur_state.exit(self) # 현재 상태 탈출
            self.cur_state = next_state[self.cur_state][event] # 다음 상태 계산
            self.cur_state.enter(self, event) # 다음 상태 입장
        # self.frame = (self.frame + 1) % 8
        # self.x += self.dir * 1
        # self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self)