def control():  
    zombies = eval(input('Insert zombies list --> '))
    plants = eval(input('Insert plants list --> '))
    zc = zombies[:]
    pc = plants[:]

    for i in range(len(min(zombies, plants, key=len))):
        if zombies[i] > plants[i]:
            plants[i] = 0
        elif zombies[i] < plants[i]:
            zombies[i] = 0
        else:
            plants[i] = 0
            zombies[i] = 0

    zombies = [el for el in zombies if el > 0]
    plants = [el for el in plants if el > 0]

    if len(plants) > len(zombies):
        print(True)
    elif len(plants) == len(zombies):
        print(sum(pc) >= sum(zc))
    else:
        print(False)
    
    if input('Do you want to insert other lists? --> ').lower() == 'yes':
        control()

control()