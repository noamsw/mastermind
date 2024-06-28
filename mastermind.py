import random
from collections import Counter

if __name__ =='__main__':
    num = str(random.randint(10000,99999))
    print(f"num: {num}")
    numcounts = Counter(num)
    guess = input('please guess a five digit number: ')
    num_guesses = 1
    while True:
        while not guess.isdigit() or len(guess) != 5:
            guess = input("sorry, please only guess a 5 digit number: ")
        if guess == num:
            print(f"wow, you guessed it in {num_guesses} guesses!")
            quit()
        guesscounts = Counter(guess)
        total_correct = 0
        in_correct_position = 0
        for i in range(5):
            if num[i] == guess[i]:
                in_correct_position+=1
        for digit,val in guesscounts.items():
            if digit in numcounts:
                total_correct += min(val, numcounts[digit])
        print('you didnt quite guess it')
        print(f'but {total_correct} of you digits are correct')
        print(f'and {in_correct_position} are in the right position')
        guess = input("try again, guess a five digit number: ")
        num_guesses += 1
    
    

    