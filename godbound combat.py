'''
A combat simulator for the Godbound RPG. It assumes there are just two
foes and that they just smack each other to bits until one loses. Pretty
basic with no powers or saves, just normal hits.
'''

import random

class creature:
    def __init__(self, name: str, ac:int, hp:int, attackbonus:int, attacknum:int, dmg:int, dmgBonus:int, morale:int):
        self.name = name
        self.ac = ac
        self.hp = hp
        self.hpMax = hp
        self.attackbonus = attackbonus
        self.attacknum = attacknum
        self.dmg = dmg
        self.dmgBonus = dmgBonus
        self.morale = morale

def montecarlo(simNum, cr1, cr2):
    #allows for multiple simulations
    cr1_wins, cr2_wins = 0, 0

    for i in range(simNum):
        cr1 = creature('Heavenly Army',4, 48, 4, 3, 8, 2, 10)
        cr2 = creature('Dehnet Army',4, 32, 4, 2, 8, 2, 11)
        winner = combat(cr1, cr2)
        if winner == 'cr1':
            cr1_wins += 1
        if winner == 'cr2':
            cr2_wins += 1
        if winner == 'loss':
            #print('TIE')
            pass
    print(f'{cr1.name} wins: {cr1_wins}')
    print(f'{cr2.name} wins: {cr2_wins}')

def combat(cr1, cr2):
    vic1, vic2 = False, False
    while True:

        for i in range(cr1.attacknum):
            cr1_atk = random.randint(1,20) + cr1.attackbonus + cr2.ac
            if cr1_atk >= 20:
                dmg1 = random.randint(1, cr1.dmg) + cr1.dmgBonus
                dmg1 = damageGB(dmg1)
                cr2.hp -= dmg1

        for i in range(cr2.attacknum):
            cr2_atk = random.randint(1,20) + cr2.attackbonus + cr1.ac
            if cr2_atk >= 20:
                dmg2 = random.randint(1, cr2.dmg) + cr2.dmgBonus
                dmg2 = damageGB(dmg2)
                cr1.hp -= dmg2

        if morale(cr1):
            #print(f'{cr1.name} flees!')
            vic2 = True
        if morale(cr2):
            #print(f'{cr2.name} flees!')
            vic1 = True
        if cr1.hp < 1:
            #print(f'{cr1.name} is defeated')
            
            vic2 = True
        if cr2.hp < 1:
            #print(f'{cr2.name} is defeated')
            vic1 = True

        #Allows for the possibility of both sides losing at the same time
        if vic1 == True or vic2 == True:
            if vic1 == True and vic2 == True:
                return 'loss'
            elif vic1 == True:
                return 'cr1'
                break
            elif vic2 == True:
                return 'cr2'
                break

def damageGB(num):
    #Simulates Godbound's combat damage matrix (pg 20)
    if num < 2:
        return 0
    elif num < 6:
        return 1
    elif num < 10:
        return 2
    else:
        return 4

def morale(creature):
    #Simulates morale checks, made when the combatant is at 50% HP,
    #and 10% HP.
    if creature.hp < (creature.hpMax / 2):
        roll = random.randint(1,6) + random.randint(1,6)
        if roll > creature.morale:
            return True
    elif creature.hp < (creature.hpMax * 0.1):
        roll = random.randint(1,6) + random.randint(1,6)
        if roll > creature.morale:
            return True
    else:
        return False
        

e_large = creature('Heavenly Army',4, 48, 4, 3, 8, 2, 10)
e_med = creature('Dehnet Army',4, 32, 4, 2, 8, 2, 11)
montecarlo(10000, e_large, e_med)
