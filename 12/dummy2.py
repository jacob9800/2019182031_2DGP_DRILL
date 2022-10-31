class Player:
    name = 'Asshole'

    def __init__(self): # self : 객체 자기 자신, 변수 이름은 뭐로 해도 상관 없음 예) My, Me 등등..
        self.x = 100

    def where(self):
        print(self.x)

player = Player()
player.where()

print(Player.name)
print(player.name)

Player.where(player)
