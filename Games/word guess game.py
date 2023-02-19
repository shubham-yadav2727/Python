import random
words  = ['programming', 'fire', 'happy', 'wedding', 'anime','onepiece', 'naruto', 'hunter', 'hero', 'titan', 'tiger', 'pokemon']
ran_word = random.choice(words)
print('our random word ',  ran_word)
print('******* word guessing game *******')
user_guess = ''
chances = 10
while chances>0:
    wrong_guess = 0
    for character in ran_word:
        if character in user_guess:
            print(f'correct guess: {character}')
        else:
            wrong_guess+=1
            print('_')    
    if wrong_guess==0:
        print('correct')
        print(f'word : {ran_word}')
        break
    guess = input('make a guess : ')
    user_guess+= guess
    if guess not in ran_word:
        chances-=1
        print(f'worng. You have {chances} more chances')            

        if chances == 0:
            print('game over')