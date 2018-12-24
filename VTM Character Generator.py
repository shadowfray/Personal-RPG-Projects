#vtm character generator

'''The goal of this program is to generate characters for the V20 roleplaying
game.'''


from random import *

def main(pick=0):
    attributes = ({'strength':1,'dexterity':1,'stamina':1,'pri':0},{'charisma':1,'manipulation':1,'appearance':1,'pri':0},{'perception':1,'intelligence':1,'wits':1,'pri':0})
    talents = {'alertness':0, 'athletics':0, 'awareness':0,'brawl':0,'empathy':0,'expression':0,'intimidation':0,'leadership':0,'streetwise':0,'subterfuge':0,'pri':0}
    skills = {'animal ken':0,'crafts':0,'drive':0,'etiquette':0,'firearms':0,'larceny':0,'melee':0,'performance':0,'stealth':0,'survival':0,'pri':0}
    knowledges = {'academics':0,'computer':0,'finance':0,'investigation':0,'law':0,'medicine':0,'occult':0,'politics':0,'science':0,'technology':0,'pri':0}
    disciplines = {'animalism':0,'auspex':0,'celerity':0,'chimestry':0,'dementation':0,'dominate':0,'fortitude':0,'necromancy':0,'obfuscate':0,'obtenebration':0,'potence':0,'presence':0,
                   'protean':0,'quietus':0,'serpentis':0,'thaumaturgy':0,'vicissitude':0}
    background = {'allies':0,'alternate identity':0,'contacts':0,'domain':0,'fame':0,'generation':0,'herd':0,'influence':0,'mentor':0,'resources':0,'retainers':0,'status':0,'black hand':0,'rituals':0}
    virtues = {'conscience':1,'self-control':1,'courage':1,'humanity':0,'willpower':0}
    natdem = ['Architect','Autocrat','Bon Vivant', 'Bravo','Capitalist','Caregiver','Celebrant','Chameleon','Child','Competitor','Conformist','Conniver','Creep show', 'Curmudgeon',
              'Dabbler','Deviant','Director','Enigma','Eye of the Storm','Fanatic','Gallant','Guru','Idealist','Judge','Loner','Martyr','Masochist','Monster','Pendagogue','Pentinet'
              'Perfectionist','Rebel','Rogue','Sadist','Scientist','Sociopath','Soldier','Survivor','Thrill-seeker','Traditionalist','Trickster','Visionary']
    freebie_categories = {'attributes':0,'ability':0,'disciplines':0,'background':0,'virtue':0,'humanity':0,'willpower':0}
    thaumaturgy = {'Path of Blood':0,'Elemental Mastery':0,'The Green Path':0,'Hands of Destruction':0,'The Lure of Flames':0,"Neptune's might":0,'Movement of the Mind':0,'Path of Conjuring':0,
                    'Path of Corruption':0,'Path of Mars':0,'Path of Technomancy':0,'Path of Fathers vengance':0,'Countermagic':0,'Weather Control':0}
    necromancy = {'Sepulcher Path':0,'Ash Path':0,'Bone Path':0,'Cenotaph Path':0,'Corpse in the Monster':0,'The Graves decay':0,'Path of four Humors':0,'Vitreous Path':0}
    rituals = []

    freebies(freebie_categories)
    
    sect, clan = sect_clan()
    if pick != 0:
        clan = input('please choose a clan [Ex:Brujah]: ')
    attributes_gen(clan, attributes, freebie_categories['attributes'])
    abilities_gen(clan, talents, skills, knowledges,freebie_categories['ability'])
    disciplines_gen(clan, disciplines,freebie_categories['disciplines'])
    background_gen(clan,sect, background, freebie_categories['background'])
    virtues_gen(virtues, freebie_categories['virtue'],freebie_categories['humanity'],freebie_categories['willpower'])

    if disciplines['thaumaturgy'] > 0:
        tremereassign(disciplines, thaumaturgy)
        ritualgen(rituals, clan)
    if disciplines['necromancy'] > 0:
        necromancyassign(disciplines, necromancy)
        ritualgen(rituals, clan)
        
    while True:
        nat = randrange(0,41)
        dem = randrange(0,41)
        if nat != dem:
            break
    
    print('SECT:', sect,'\t\t CLAN:',clan)
    print('Nature:',natdem[nat],'  \t\t Demeanor:',natdem[dem])
    print('Generation:',13-background['generation'],'  \t\t Blood Pool:', randrange(1,11))
    print('='*10)
    print('Strength:',attributes[0]['strength'],'\t Charisma:',attributes[1]['charisma'],'\t\t Perception:',attributes[2]['perception'])
    print('Dexterity:',attributes[0]['dexterity'],'\t Manipulation:',attributes[1]['manipulation'],'\t Intelligence:',attributes[2]['intelligence'])
    print('Stamina:', attributes[0]['stamina'],'\t Appearance:',attributes[1]['appearance'],'\t\t Wits:',attributes[2]['wits'])
    print('='*10)

    print('Alertness:',talents['alertness'],'\t\t Animal Ken:',skills['animal ken'],'\t\t Academics:',knowledges['academics'])
    print('Athletics:',talents['athletics'],'\t\t Crafts:',skills['crafts'],'\t\t Computer:',knowledges['computer'])
    print('Awarness:',talents['awareness'],'\t\t Drive:',skills['drive'],'\t\t Finance:',knowledges['finance'])
    print('Brawl:',talents['brawl'],'\t\t Etiquette:',skills['etiquette'],'\t\t Investigation',knowledges['investigation'])
    print('Empathy:',talents['empathy'],'\t\t Firearms:',skills['firearms'],'\t\t Law:',knowledges['law'])
    print('Expression:',talents['expression'],'\t\t Larceny:',skills['larceny'],'\t\t Medicine:',knowledges['medicine'])
    print('Intimidation:',talents['intimidation'],'\t Melee:',skills['melee'],'\t\t Occult:',knowledges['occult'])
    print('Leadership:',talents['leadership'],'\t\t Performance:',skills['performance'],'\t Politics:',knowledges['politics'])
    print('Streetwise:',talents['streetwise'],'\t\t Stealth:',skills['stealth'],'\t\t Science:',knowledges['science'])
    print('Subterfuge:',talents['subterfuge'],'\t\t Survival:',skills['survival'],'\t\t Technology:',knowledges['technology'])
    print('')

    print('Disciplines:')
    printvalues(disciplines)
    print('Backgrounds:')
    printvalues(background)
    printvalues(virtues)
    
    if disciplines['thaumaturgy'] > 0:
        printvalues(thaumaturgy)
    if disciplines['necromancy'] > 0:
        printvalues(necromancy)
    if rituals != []:
        print('Rituals:',rituals[0])


def sect_clan():
    Cam_clans = ['Brujah', 'Gangrel', 'Malkavian', 'Nosferatu', 'Toreador', 'Tremere', 'Ventrue', 'Caitiff']
    Sab_clans = ['Lasombra', 'Tzimisce', 'Caitiff']
    Ind_clans = ['Assamite', 'Followers of Set', 'Giovanni', 'Ravnos', 'Caitiff']

    sect_num_choice = randrange(1,10)
    if sect_num_choice < 7:
        sect_choice = 'Camarilla'
    elif 6 < sect_num_choice < 9:
        sect_choice = 'Sabbat'
    elif sect_num_choice > 8:
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

def attributes_gen(clan, attributes,freebie):
    priority_val = 3
    a,b,c = 0,0,0
    att_list = [9,9,9]
    rand_category = randrange(0,3)
    start = rand_category

    while priority_val >0:
        att_list[(start%3)] = priority_val
        priority_val -= 1
        start += 1

    while freebie > 0:
        pick = randrange(0,3)
        if pick == 0:
            a += 1
        if pick == 1:
            b += 1
        if pick == 2:
            c += 1
        freebie -= 1

    for m in range(3):
        attributes[m]['pri'] = att_list[m]

    phys_names = ('strength','dexterity','stamina')
    soc_names = ('charisma','manipulation','appearance')
    ment_names = ('perception','intelligence','wits')

    attribute_assign(clan, phys_names, attributes,0,a)
    attribute_assign(clan, soc_names, attributes,1,b)
    attribute_assign(clan, ment_names, attributes,2,c)


def attribute_assign(clan, names, attributes,num,frees):
    basestat1,basestat2,basestat3 = 1,1,1
    points = (2*attributes[num]['pri'])+1+frees
    while points > 0:
        statpick = randrange(0,3)
        if statpick == 0:
            if basestat1 < 6:
                basestat1 += 1
                points -= 1
        if statpick == 1:
            if basestat2 < 6:
                basestat2 += 1
                points -= 1
        if statpick == 2:
            if basestat3 < 6:
                basestat3 += 1
                points -= 1
        
    attributes[num][(names[0])] = basestat1
    attributes[num][(names[1])] = basestat2
    attributes[num][(names[2])] = basestat3

def abilities_gen(clan, talents, skills, knowledges,freebie):
    priority_val = 3
    abil_list = [10,10,10]
    a,b,c = 0,0,0
    rand_abil = randrange(0,3)

    while priority_val >0:
        abil_list[(rand_abil%3)] = priority_val
        priority_val -= 1
        rand_abil += 1

    while freebie > 0:
        pick = randrange(0,3)
        if pick == 0:
            a += 1
        if pick == 1:
            b += 1
        if pick == 2:
            c += 1
        freebie -= 1
        
    talents['pri'] = abil_list[0]
    skills['pri'] = abil_list[1]
    knowledges['pri'] = abil_list[2]

    abilities_assign(clan, talents,a)
    abilities_assign(clan, skills,b)
    abilities_assign(clan, knowledges,c)

def abilities_assign(clan, abilitydict, frees):
    abilval = [0,0,0,0,0,0,0,0,0,0,abilitydict['pri']]
    points = (4*abilitydict['pri'])+1+frees
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
        
def disciplines_gen(clan, disciplines, freebies):
    points = 3 + freebies
    ava_disc = []
    if clan == 'Caitiff':
        sect, clan = sect_clan()
    if clan == 'Assamite':
        ava_disc.append('celerity')
        ava_disc.append('obfuscate')
        ava_disc.append('quietus')
    if clan == 'Brujah':
        ava_disc.append('celerity')
        ava_disc.append('potence')
        ava_disc.append('presence')
    if clan == 'Followers of Set':
        ava_disc.append('obfuscate')
        ava_disc.append('presence')
        ava_disc.append('serpentis')
    if clan == 'Gangrel':
        ava_disc.append('animalism')
        ava_disc.append('fortitude')
        ava_disc.append('protean')
    if clan == 'Giovanni':
        ava_disc.append('dominate')
        ava_disc.append('necromancy')
        ava_disc.append('potence')
    if clan == 'Lasombra':
        ava_disc.append('dominate')
        ava_disc.append('obtenebration')
        ava_disc.append('potence')
    if clan == 'Malkavian':
        ava_disc.append('auspex')
        ava_disc.append('dementation')
        ava_disc.append('obfuscate')
    if clan == 'Nosferatu':
        ava_disc.append('animalism')
        ava_disc.append('obfuscate')
        ava_disc.append('potence')
    if clan == 'Ravnos':
        ava_disc.append('animalism')
        ava_disc.append('chimestry')
        ava_disc.append('fortitude')
    if clan == 'Toreador':
        ava_disc.append('auspex')
        ava_disc.append('celerity')
        ava_disc.append('presence')
    if clan == 'Tremere':
        ava_disc.append('auspex')
        ava_disc.append('dominate')
        ava_disc.append('thaumaturgy')
    if clan == 'Tzimisce':
        ava_disc.append('animalism')
        ava_disc.append('auspex')
        ava_disc.append('vicissitude')
    if clan == 'Ventrue':
        ava_disc.append('dominate')
        ava_disc.append('fortitude')
        ava_disc.append('presence')
    
    while points > 0:
        pick = randrange(0,3)
        disciplines[(ava_disc[pick])] += 1                        
        points -= 1

def background_gen(sect, clan, background, freebies):
    points,end = (5 + freebies), 13
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

def virtues_gen(virtues,virtfree, humfree, willfree):
    points = 7 + virtfree
    while points > 0:
        pick = randrange(1,4)
        if pick == 1:
            virtues['conscience'] += 1
        if pick == 2:
            virtues['self-control'] += 1
        if pick == 3:
            virtues['courage'] += 1
        points -= 1
    virtues['willpower'] = virtues['courage'] + willfree
    virtues['humanity'] = 10 - virtues['willpower'] + humfree - willfree

def freebies(assignment):
    freepoints = 15
    while freepoints > 0:
        pick = randrange(0,7)
        if pick == 0:
            if freepoints > 4:
                assignment['attributes'] += 1
                freepoints -= 5
        if pick == 1:
            if freepoints > 1:
                assignment['ability'] += 1
                freepoints -= 2
        if pick == 2:
            if freepoints > 6:
                assignment['disciplines'] += 1
                freepoints -= 7
        if pick == 3:
            if freepoints > 0:
                assignment['background'] += 1
                freepoints -= 1
        if pick == 4:
            if freepoints > 1:
                assignment['virtue'] += 1
                freepoints -= 2
        if pick == 5:
            if freepoints > 1:
                assignment['humanity'] += 1
                freepoints -= 2
        if pick == 6:
            if freepoints > 0:
                assignment['willpower'] += 1
                freepoints -= 2

def tremereassign(disciplines, thaumaturgy):
    maxval = disciplines['thaumaturgy']
    maxpoints = maxval
    while maxpoints > 0:
        pick = randrange(1,101)
        if pick < 41:
            thaumaturgy['Path of Blood'] += 1
        if 49 > pick > 40:
            thaumaturgy['Elemental Mastery'] += 1
        if 54 > pick > 48:
            thaumaturgy['The Green Path'] += 1
        if 60 > pick > 53:
            thaumaturgy['The Lure of Flames'] += 1
        if 65 > pick > 59:
            thaumaturgy['Hands of Destruction'] += 1
        if 66 > pick > 64:
            thaumaturgy['Path of Corruption'] += 1
        if 73 > pick > 65:
            thaumaturgy['Movement of the Mind'] += 1
        if 79 > pick > 72:
            thaumaturgy['Path of Conjuring'] += 1
        if 83 > pick > 78:
            thaumaturgy["Neptune's might"] += 1
        if 87 > pick > 82:
            thaumaturgy['Path of Technomancy'] += 1
        if 88 > pick > 86:
            thaumaturgy["Path of Father's vengance"] += 1
        if 89 > pick > 87:
            thaumaturgy['Path of Mars'] += 1
        if 93 > pick > 88:
            thaumaturgy['Countermagic'] += 1
        if 97 > pick > 92:
            thaumaturgy['Weather Control'] += 1
        maxpoints -= 1

def necromancyassign(disciplines,necromancy):
    maxval = disciplines['necromancy']
    maxpoints = maxval
    while maxpoints > 0:
        pick = randrange(1,101)
        if pick < 26:
            necromancy['Sepulcher Path'] += 1
        if 46 > pick > 25:
            necromancy['Ash Path'] += 1
        if 51 > pick > 45:
            necromancy['Bone Path'] += 1
        if 64 > pick >50:
            necromancy['Cenotaph Path'] +=1
        if 77 > pick > 63:
            necromancy['Corpse in the Monster'] += 1
        if 90> pick > 76:
            necromancy['The Graves decay'] += 1
        if 96 > pick > 89:
            necromancy['Path of four Humors'] += 1
        if pick > 95:
            necromancy['Vitreous Path'] += 1
        maxpoints -= 1

def ritualgen(rituals, clan):
    necroritual_1 = ['Call the Hungry Dead','Eldritch beacon','Insight','Knowing Stone','Minestra di Morte','Ritual of the Smoking Mirror']
    thaumritual_1 = ['Bind the Accusing Tongue','Blood Rush','Communicate with Kindred Sire','Defense of the Sacred Heaven',
                     'Deflection of Wooden Doom','Devils touch','Domino of Life','Engaging the Vessel of Transference',
                     'Illuminate the Trail of Prey','Incantation of The Shepherd','Purity of Flesh','Wake with Evenings Freshness',
                     'Widows spite']

    if clan == 'Tremere':
        pick = randrange(0,13)
        rituals.append(thaumritual_1[pick])
    if clan == 'Giovanni':
        pick = randrange(0,6)
        rituals.append(necroritual_1[pick])

def printvalues(valdict):
    for i in valdict:
        if valdict[i] != 0:
            print(i, valdict[i])
    print('')
       
main()

