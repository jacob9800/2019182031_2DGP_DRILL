import pickle

class Npc:
    def __init__(self, name, x, y):
        self.name = name
        self.x, self.y = x, y

yuri = Npc('Yuri', 100, 100)
print(yuri.__dict__) # 객체의 모든 속성은 __dict__에 자동으로 들어간다.
yuri.__dict__['age'] = 69
print(yuri.name, yuri.x, yuri.y, yuri.age)

yuri.name, yuri.x, yuri.y = 'tom', 4, 5
new_data = {'name' : 'jeny', 'x':5, 'y':100, 'age':30}
yuri.__dict__.update(new_data)
print(yuri.name, yuri.x, yuri.y, yuri.age)


tom = Npc('Jia', 100, 200)
print(tom.__dict__)
# npc_list = [yuri, tom]
#
# with open('npc.pickle', 'wb') as f:
#     pickle.dump(npc_list, f)

    