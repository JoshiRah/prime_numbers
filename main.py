#Copyright Joshua Rahmlow

while True:
    try:
        userIn = int(input('Enter the number you would like to check: '))
        break
    except:
        print('\nPlease enter a natural number')


def checkForPrime():
    for i in range(2, userIn):
        if userIn % i == 0:
            print('\n- No prime number -')
            break
    else:
        print('\n- Prime number -')

checkForPrime()
