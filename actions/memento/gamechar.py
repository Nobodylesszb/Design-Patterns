"""
打过游戏的朋友一定知道，
大多数游戏都有保存进度的功能，
如果一局游戏下来，忘保存了进度，
那么下次只能从上次进度点开始重新打了。
一般情况下，保存进度是要存在可持久化存储器上，
本例中先以保存在内存中来模拟实现该场景的情形。
以模拟一个战斗角色为例。首先，创建游戏角色。
"""
import random
class GameCharacter():
    vitality = 0
    attack = 0
    defense = 0
    def displayState(self):
        print ('Current Values:')
        print ('Life:%d' % self.vitality)
        print ('Attack:%d' % self.attack)
        print ('Defence:%d' % self.defense)
    def initState(self,vitality,attack,defense):
        self.vitality = vitality
        self.attack = attack
        self.defense = defense
    def saveState(self):
        return Memento(self.vitality, self.attack, self.defense)
    def recoverState(self, memento):
        self.vitality = memento.vitality
        self.attack = memento.attack
        self.defense = memento.defense


class FightCharactor(GameCharacter):
    def fight(self):
        self.vitality -= random.randint(1,10)


class Memento:
    vitality = 0
    attack = 0
    defense = 0
    def __init__(self, vitality, attack, defense):
        self.vitality = vitality
        self.attack = attack
        self.defense = defense


if __name__=="__main__":
    game_chrctr = FightCharactor()
    game_chrctr.initState(100,79,60)
    game_chrctr.displayState()
    memento = game_chrctr.saveState()
    game_chrctr.fight()
    game_chrctr.displayState()
    game_chrctr.recoverState(memento)
    game_chrctr.displayState()

"""
Current Values:
Life:100
Attack:79
Defence:60
Current Values:
Life:91
Attack:79
Defence:60
Current Values:
Life:100
Attack:79
Defence:60
"""


