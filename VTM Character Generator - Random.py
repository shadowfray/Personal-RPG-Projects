#vtm character generator

'''The goal of this program is to generate characters for the V20 roleplaying
game.'''


from random import *

def main():
    attributes = ({'strength':1,'dexterity':1,'stamina':1,'pri':0},{'charisma':1,'manipulation':1,'appearance':1,'pri':0},{'perception':1,'intelligence':1,'wits':1,'pri':0})
    talents = {'alertness':0, 'athletics':0, 'awareness':0,'brawl':0,'empathy':0,'expression':0,'intimidation':0,'leadership':0,'streetwise':0,'subterfuge':0,'pri':0}
    skills = {'animal ken':0,'crafts':0,'drive':0,'etiquette':0,'firearms':0,'larceny':0,'melee':0,'performance':0,'stealth':0,'survival':0,'pri':0}
    knowledges = {'academics':0,'computer':0,'finance':0,'investigation':0,'law':0,'medicine':0,'occult':0,'politics':0,'science':0,'technology':0,'pri':0}
    background = {'allies':0,'alternate identity':0,'contacts':0,'domain':0,'fame':0,'generation':0,'herd':0,'influence':0,'mentor':0,'resources':0,'retainers':0,'status':0,'black hand':0,'rituals':0}
    virtues = {'conscience':1,'self-control':1,'courage':1,'humanity':0,'willpower':0}
    natdem = ['Architect','Autocrat','Bon Vivant', 'Bravo','Capitalist','Caregiver','Celebrant','Chameleon','Child','Competitor','Conformist','Conniver','Creep show', 'Curmudgeon',
              'Dabbler','Deviant','Director','Enigma','Eye of the Storm','Fanatic','Gallant','Guru','Idealist','Judge','Loner','Martyr','Masochist','Monster','Pendagogue','Pentinet'
              'Perfectionist','Rebel','Rogue','Sadist','Scientist','Sociopath','Soldier','Survivor','Thrill-seeker','Traditionalist','Trickster','Visionary']
    
    sect, clan = sect_clan()
    attributes_gen(clan, attributes)
    abilities_gen(clan, talents, skills, knowledges)
    background_gen(clan,sect, background)
    virtues_gen(virtues)

    while True:
        nat = randrange(0,41)
        dem = randrange(0,41)
        if nat != dem:
            break
    
    print('SECT:', sect,'         CLAN:',clan)
    print('Nature:',natdem[nat],'      Demeanor:',natdem[dem])
    
    for j in range(3):
        for i in attributes[j]:
            print(i, attributes[j][i])
        print('')

    printvalues(talents)
    printvalues(skills)
    printvalues(knowledges)
    printvalues(background)
    printvalues(virtues)

def sect_clan():
    Cam_clans = ['Brujah', 'Gangrel', 'Malkavian', 'Nosferatu', 'Toreador', 'Tremere', 'Ventrue', 'Caitiff']
    Sab_clans = ['Lasombra', 'Tzimisce', 'Caitiff']
    Ind_clans = ['Assamite', 'Followers of Set', 'Giovanni', 'Ravnos', 'Caitiff']

    sect_num_choice = randrange(1,4)
    if sect_num_choice == 1:
        sect_choice = 'Camarilla'
    elif sect_num_choice == 2:
        sect_choice = 'Sabbat'
    elif sect_num_choice == 3:
        sect_choice = 'Independent'

    caitiff_choice = randrange(1, 21)
    caitiff = 0
    if caitiff_choice == 1:
        #since Sabbat only has 3 options, this makes caitiff less prominent
        if sect_choice != 'Sabbat':
            caitiff = 1
        else:
            sab_cait = randrange(0,2)
            caitiff -= sab_cait
    else:
        caitiff = 0

    if sect_choice == 'Camarilla':
        clan_range = len(Cam_clans)
    if sect_choice == 'Sabbat':
        clan_range = len(Sab_clans)
    if sect_choice == 'Independent':
        clan_range = len(Ind_clans)
        
    clan_num_choice = randrange(0, (clan_range-caitiff))
    
    if sect_choice == 'Camarilla':
        clan = Cam_clans[clan_num_choice]
    if sect_choice == 'Sabbat':
        clan = Sab_clans[clan_num_choice]
    if sect_choice == 'Independent':
        clan = Ind_clans[clan_num_choice]

    return sect_choice, clan

def attributes_gen(clan, attributes):
    priority_val = 3
    att_list = [9,9,9]
    rand_category = randrange(0,3)
    start = rand_category

    while priority_val >0:
        att_list[(start%3)] = priority_val
        priority_val -= 1
        start += 1

    for m in range(3):
        attributes[m]['pri'] = att_list[m]

    phys_names = ('strength','dexterity','stamina')
    soc_names = ('charisma','manipulation','appearance')
    ment_names = ('perception','intelligence','wits')

    attribute_assign(clan, phys_names, attributes,0)
    attribute_assign(clan, soc_names, attributes,1)
    attribute_assign(clan, ment_names, attributes,2)


def attribute_assign(clan, names, attributes,num):
    basestat1,basestat2,basestat3 = 1,1,1
    points = (2*attributes[num]['pri'])+1
    while points > 0:
        statpick = randrange(0,3)
        if statpick == 0:
            basestat1 += 1
        if statpick == 1:
            basestat2 += 1
        if statpick == 2:
            basestat3 += 1
        points -= 1
        
    attributes[num][(names[0])] = basestat1
    attributes[num][(names[1])] = basestat2
    attributes[num][(names[2])] = basestat3

def abilities_gen(clan, talents, skills, knowledges):
    priority_val = 3
    abil_list = [10,10,10]
    rand_abil = randrange(0,3)

    while priority_val >0:
        abil_list[(rand_abil%3)] = priority_val
        priority_val -= 1
        rand_abil += 1
        
    talents['pri'] = abil_list[0]
    skills['pri'] = abil_list[1]
    knowledges['pri'] = abil_list[2]

    abilities_assign(clan, talents)
    abilities_assign(clan, skills)
    abilities_assign(clan, knowledges)

def abilities_assign(clan, abilitydict):
    abilval = [0,0,0,0,0,0,0,0,0,0,abilitydict['pri']]
    points = (4*abilitydict['pri'])+1
    pos_track = 0
    while points > 0:
        pick = randrange(0,101)
        if  pick < 10:
            abilval[0] += 1
        if 9 < pick < 20:
            abilval[1] += 1
        if 19 < pick < 30:
            abilval[2] += 1
        if 29 < pick < 40:
            abilval[3] += 1
        if 39 < pick < 50:
            abilval[4] += 1
        if 49 < pick < 60:
            abilval[5] += 1
        if 59 < pick < 70:
            abilval[6] += 1
        if 69 < pick < 80:
            abilval[7] += 1
        if 79 < pick < 90:
            abilval[8] += 1
        if 89 < pick < 101:
            abilval[9] += 1
        points -= 1

    for i in abilitydict:
        abilitydict[i] = abilval[pos_track]
        pos_track += 1


def background_gen(sect, clan, background):
    points,end = 5,13
    if sect == 'Sabbat':
        end = 15
    while points > 0:
        pick = randrange(1,end)
        if pick == 1:
            background['allies'] += 1
        if pick == 2:
            background['alternate identity'] += 1
        if pick == 3:
            background['contacts'] += 1
        if pick == 4:
            background['domain'] += 1
        if pick == 5:
            background['fame'] += 1
        if pick == 6:
            background['generation'] += 1
        if pick == 7:
            background['herd'] += 1
        if pick == 8:
            background['influence'] += 1
        if pick == 9:
            background['mentor'] += 1
        if pick == 10:
            background['resources'] += 1
        if pick == 11:
            background['retainers'] += 1
        if pick == 12:
            background['status'] += 1
        if pick == 13:
            background['black hand'] += 1
        if pick == 14:
            background['rituals'] += 1
        points -= 1

def virtues_gen(virtues):
    points = 7
    while points > 0:
        pick = randrange(1,4)
        if pick == 1:
            virtues['conscience'] += 1
        if pick == 2:
            virtues['self-control'] += 1
        if pick == 3:
            virtues['courage'] += 1
        points -= 1
    virtues['willpower'] = virtues['courage']
    virtues['humanity'] = 10 - virtues['willpower']

def printvalues(valdict):
    for i in valdict:
        if valdict[i] != 0:
            print(i, valdict[i])
    print('')
       
main()
