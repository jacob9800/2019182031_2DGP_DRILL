import pickle

class Npc:
    def __init__(self, name, x, y):
        self.name = name
        self.x, self.y = x, y

with open('npc.pickle', 'rb') as f:
    npc_list = pickle.load(f)

for npc in npc_list:
    print(npc.name, npc.x, npc.y)

