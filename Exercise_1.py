while True:
    sides = eval(input('Insert list --> '))
    sides.sort()

    print(sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2)
    message = input('Do you want to insert other list? --> ')

    if message.lower() == 'no':
        break
print('Thank you. Goodbye!')