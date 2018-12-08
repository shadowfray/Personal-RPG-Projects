#vtm character generator

'''The goal of this program is to generate characters for the V20 roleplaying
game.'''


from random import *

def main():
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

    print('You are of sect', sect_choice)

    caitiff_choice = randrange(1, 21)
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
        
    clan_num_choice = randrange(1, (clan_range-caitiff))
    
    if sect_choice == 'Camarilla':
        clan = Cam_clans[clan_num_choice]
    if sect_choice == 'Sabbat':
        clan = Sab_clans[clan_num_choice]
    if sect_choice == 'Independent':
        clan = Ind_clans[clan_num_choice]

    print('You are of clan', clan)

for i in range(10):
    main()
    print('')
