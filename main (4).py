import random
HP=100
eHP=10
#СHead - coefficient Head- переменная на которую будет множиться урон в голову (В дальнейшем нужно будет перевести в статы врагов и возможно оружия)
#CChest - коэф грудной клетки (торса)
#CHand - коэф рук
#CFoot - коэф ног
enemy = random.randint(0, 2)
def enemys(enemy):
    if enemy == 0:
        eHP = 100
        edamage = 10
    elif  enemy == 1:
        eHP = 200
        edamage = 5
    elif enemy == 2:
        eHP = 50
        edamage = 20
    return eHP, edamage
def fight(HP, eHP):
    import random
    enemys(enemy)
    eHP,edamage = enemys(enemy)
    #СHead - coefficient Head- переменная на которую будет множиться урон в голову (В дальнейшем нужно будет перевести в статы врагов и возможно оружия)
    #CChest - коэф грудной клетки (торса)
    #CHand - коэф рук
    #CFoot - коэф ног
    CHead = 3
    CСhest = 1
    CHand =  1
    CFoot = 1
    N=1
    while HP > 0 and eHP > 0:
        print('Номер хода:', N)
        answer = str(input('Выбери куда хочешь ударить: в голову, в торс, в руки, в ноги '))
        print(answer)
        if answer == 'голова' or 'Голова' or 'd ujkjdf' or 'd Ujkjdf'  or 'ГОЛОВА' or 'в голову' or 'в Голову' or'ujkjdf' or 'Ujkjdf':
            roll = random.randint(0, 100)
            if roll >= 80:
                damage = random.randint(1, 20)
                eHP = eHP - damage * CHead 
                if eHP > 0:
                    print("Своим мощным ударом в голову ты оставил врагу жалкие", eHP, " ХП")
                else:
                    eHP=0
                    print("Своим ударом Сайтамы ты низвел до атомов врага")
            else:
                print("Ты промахнулся")
        elif answer == 'в торс' or 'd njhc' or 'в тело' or 'd ntkj' or 'В грудь' or 'В тело':
            roll = random.randint(0, 100)
            if roll >= 25:
                damage = random.randint(1, 20)
                eHP = eHP - damage * CСhest
                if eHP > 0:
                    print("Ты ударил врага в торс,  у него осталось ", eHP, " ХП")
                else:
                    eHP=0
                    print("У врага не осталось ХП ")
            else:
                print("Ты промахнулся")
        elif answer == 'ноги' or 'В ноги' or 'в ноги' or 'в ногу' or 'd yjub' or 'D yjub': 
            roll = random.randint(0, 100)
            if roll >= 60:
                damage = random.randint(1, 20)
                eHP = eHP - damage * CFoot
                if eHP > 0:
                    print("Ты ударил врага в ноги,  у него осталось ", eHP, " ХП")
                else:
                    eHP=0
                    print("У врага не осталось ХП ")
            else:
                print("Ты промахнулся")
        else:
            roll = random.randint(0, 100)
            if roll >= 60:
                damage = random.randint(1, 20)
                eHP = eHP - damage * CHand
                if eHP > 0:
                    print("Ты ударил врага в руки,  у него осталось ", eHP, " ХП")
                else:
                    eHP=0
                    print("У врага не осталось ХП ")
            else:
                print("Ты промахнулся")
        if eHP > 0:
            eroll= random.randint(-2, 10)
            if eroll >= 1:  
                    HP = HP - edamage
                    if HP > 0:
                        print("У тебя осталось ", HP, " ХП")
                    else:
                        print("У тебя не осталось ХП")
            else:
                    print("Враг промахнулся")
        else:
            break
        N=N+1
    if HP <= 0:
        print('Ты погиб')
    if eHP <= 0:
        print('Враг погиб')
    return HP, eHP
fight(HP, eHP)