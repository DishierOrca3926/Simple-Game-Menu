from getpass import getpass as imput
import os, random, time

#copy and paste your own code under this line (Dont forget to define it as a function)


def menu():
  menu=True
  while menu==True:
    print(f'{colourchange("red", "=")}={colourchange("blue", "=")} \033[1m{colourchange("yellow", "Game Menu")}\033[0m {colourchange("blue", "=")}={colourchange("red", "=")} '.center(104), sep = '',)
    print('')
    print(f'{colourchange("red", "Games Available.")}'.center(52))
    print('1. Guess the Number'.center(40))
    print('2. Character Battle'.center(40))
    print('3. Rock Paper Scissors'.center(40))
    
    #Dont forget a way to make sure that you can play the game by adding an input and running the game when input is a certain number
    
    menuinput=int(input('> '))
    if menuinput == 1:
        #run the function that you have defined above
    else:
      print('I dont quite get that, can you please repeat that')
      time.sleep(2)
      os.system('clear')
menu()