# Dice roll simulation
import random
repeat = True
while repeat:
    print("You rolled",random.randint(1, 6))
    print("Do you wnna roll again? Y/N")
    repeat = "Y" in input()


# Guess the number
import random
attempts = 5
secret_number = random.randint(1, 100)

for attempt in range(attempts):
    guess = int(input('Cmon take a guess: '))

    if guess < secret_number:
        print ('Just a little higher...')
    elif guess > secret_number:
        print ('Just a little lower...')
    else:
        print()
        print('Boiiii you got it! The secret number was', secret_number)
        print('You guessed it in', attempts, 'attempts')

        break

if guess != secret_number:
    print()
    print('Ohh no! better luck next time.')
    print('The correct guess was', secret_number)
