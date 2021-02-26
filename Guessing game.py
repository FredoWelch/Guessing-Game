from random import randint

anwser = randint(1,10)
print(anwser)
while True:
    try:
        guess = int(input('Guess a number between 1-10: '))
        if 0 < guess < 11:
            if guess == anwser:
                print('You were reading my mind huh? ')
                break
            else:
                print('Not what I was thinking')
        else:
            print('Numbers 1-10 only')



    except ValueError:
        print('Please enter a number')



