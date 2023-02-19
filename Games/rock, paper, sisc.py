import random
l = ['rock', 'paper', 'scissor']


while True:
    ccount = 0
    ucount = 0
    user_choice = int(input('''
Game start...
1 Yes
2 No | Exit    
        '''))

    if user_choice == 1:
        for i in range(1,6):
            user_input = int(input('''
1 Rock
2 Paper
3 scissor            
            '''))

            if user_input ==1:
                us_choice = 'rock'
                
            elif user_input ==2:
                us_choice = 'paper'
            
            elif user_input ==3:
                us_choice = 'scissor'
            com_choice = random.choice(l)
            
            if com_choice == us_choice:
                                
                print('user value : ', us_choice)
                print('com value : ', com_choice)

                print('game draw')

                ucount+=1
                ccount+=1

            elif (us_choice == 'rock' and com_choice == 'scissor') or (us_choice == 'paper' and com_choice == 'rock') or (us_choice == 'scissor' and com_choice == 'paper'):
                
                print('user value : ', us_choice)
                print('com value : ', com_choice)

                print('user win')

                ucount = ucount+1
                
            else:
                print('user value : ', us_choice)
                print('com value : ', com_choice)
                
                print('com win')
                
                ccount = ccount+1 

        if (ucount == ccount):
            print('\n')
            print('final scores are : ')

            print('user score : ', ucount)
            print('com score : ', ccount)
            
            print('\n')

            print('game draw')
        
        elif(ucount > ccount):
            print('\n')
            print(' The final scores are : ')

            print('user score : ', ucount)
            print('com score : ', ccount)

            print('\n')

            print('user wins the series.')

        else:
            print('\n')
            print('The final scores are : ')

            print('user score : ', ucount)
            print('com score : ', ccount) 

            print('\n')

            print('com wins the series.')     


    else:
        break 
