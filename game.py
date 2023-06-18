from getpass import getpass as imput
import os, random, time

def guess_number():
# "answer" is for randrange and "number" is the user's guess
  print("Guess the number!")
  answer = random.randrange(1, 100)
  print("What is your guess? 1-100")
  guess = False
  while guess == False:
    number = int(input("Guess > "))
    if answer > number:
      print("")
      print("Higher")
    elif answer < number:
      print("")
      print("Lower")
    else:
      print("")
      print("Correct")
      print("")
      guess = True
  while guess == True:
    print("Round 2")
    print("")
    answer1 = random.randrange(1, 1000)
    guess = False
    while guess == False:
      
      print("What is your guess? 1-1000")
      number1 = int(input("Guess > "))
      if answer1 > number1:
        print("")
        print("Higher")
      elif answer1 < number1:
        print("")
        print("Lower")
      else:
        print("")
        print("Correct")
        print("")
        exitinput=input("Type anything to exit")
        if exitinput == "9533359":
          guess = False
          os.system('clear')
          break
        else:
          guess = False
          os.system('clear')
          break

def dice_roll(side):
  result = random.randint(1, side)
  return result

def generate_type():
  type = random.randint(1, 4)
  if type == 1:
    character = 'Human'
  elif type == 2:
    character = 'Elf'
  elif type == 3:
    character = 'Wizard'
  elif type == 4:
    character = 'Orc'
  return character

def health_stats():
  health = ((dice_roll(6)*dice_roll(12))/2)+10
  return health
  
def strength_stats():
  strength = ((dice_roll(6)*dice_roll(12))/2)+12
  return strength

def CharacterBuilder():  
  #game loop
  builder_counter = 0
  battle_round = 1
  builder = 'yes'
  while builder == 'yes':
    
  #start of charcter builder
    print('Character Builder')
    print('')
    print('Name Your Legend:')
    c1_name = input('> ')
    time.sleep(1)
    print('')
    print('Character Type (Human, Elf, Wizard, Orc):')
    c1_type = generate_type()
    
    print(c1_type)
    time.sleep(1)
    print('')
    print(c1_name)
    c1_health = health_stats()
    c1_strength = strength_stats()
    print(f'HEALTH: {c1_health}')
    print(f'STRENGTH: {c1_strength}')
    print('')
    
    time.sleep(1)
    if builder_counter == 0:
      print('Who are they versing?')
      print('')
    builder_counter = builder_counter + 1
    time.sleep(2)
    
    print('Name Your Legend:')
    c2_name = input('> ')
    time.sleep(1)
    print('')
    print('Character Type (Human, Elf, Wizard, Orc):')
    c2_type = generate_type()
    
    print(c2_type)
    time.sleep(1)
    print('')
    print(c2_name)
    c2_health = health_stats()
    c2_strength = strength_stats()
    print(f'HEALTH: {c2_health}')
    print(f'STRENGTH: {c2_strength}')
    print('')
    
    time.sleep(2)
    clear = input('Do you wish the clear the above text? ')
    if clear == 'yes':
      os.system('clear')
    
  #start of battle loop
    battle = True
    while battle == True:
      time.sleep(1)
      print('BATTLE TIME')
      print('')
      if battle_round == 1:
        print('The battle begins!')
      else:
        print('The battle continues')
      
      c1_dice = dice_roll(6)
      c2_dice = dice_roll(6)
      difference = (c1_strength - c2_strength) + 1
      if difference < 0:
        difference = difference + (difference*difference)
      time.sleep(1)
      
      if c1_dice > c2_dice:
        c2_health = c2_health - difference
        if battle_round == 1:
          print(f'{c1_name} wins the first blow')
        else:
          print(f'{c1_name} wins round {battle_round}')
      elif c1_dice < c2_dice:
        c1_health = c1_health - difference
        if battle_round == 1:
          print(f'{c2_name} wins the first blow')
        else:
          print(f'{c2_name} wins round {battle_round}')
      else:
        print(f'They attack eachother but no damage is done, they draw round {battle_round}')
      time.sleep(1)
  
      if c1_health < 0:
        c1_health = 0
      if c2_health < 0:
        c2_health = 0
      print('')
      print(c1_name)
      print(f'HEALTH = {c1_health}')
      print('')
      print(c2_name)
      print(f'HEALTH = {c2_health}')
      battle_round = battle_round + 1
      time.sleep(1)
  
      if c1_health == 0:
        print(f'{c1_name} has died.')
        time.sleep(1)
        print(f'{c2_name} WINS')
        break
      
      if c2_health == 0:
        print(f'{c2_name} has died.')
        time.sleep(1)
        print(f'{c1_name} WINS')
        break
      
    proceed = input('Do you wish to continue? ')
    if proceed == 'yes':
      continue
    else:
      builder = proceed
      os.system('clear')
      break


def RockPaperScissors():
  
  print("Rock paper Scissors")
  print("")
  print("select your move (R,P or S)")
  print("")
  
  player1score = 0
  player2score = 0
  win1 = "undefined"
  win2 = "undefined"
  RockPaperScissor = True
  while RockPaperScissor == True:
    print("")
    player1move = imput("Player 1 > ")
    print()
    player2move = imput("Player 2 > ")
    print()
    
    
    if player1move=="r":
      if player2move=="r":
        print("You both picked rock, draw")
      elif player2move=="s":
        print("Player 1 shatters Player 2's scissors with a rock")
        player1score += 1
      elif player2move=="p":
        print("Player 2 covers Player 1's rock with paper")
        player2score += 1
      else:
        print("invalid move Player 2")
    elif player1move=="p":
      if player2move=="p":
        print("You both picked paper, draw")
      elif player2move=="r":
        print("Player 1 covers Player 2's rock")
        player1score += 1
      elif player2move=="s":
        print("Player 2 turns Player 1's paper into confetti")
        player2score += 1
      else:
        print("Invalid move Player 2")
    elif player1move=="s":
      if player2move=="s":
        print("You both picked scissors, draw")
      elif player2move=="r":
        print("Player 2 shatters Player 1's scissors")
        player2score += 1
      elif player2move=="p":
        print("Player 1 turns Player 2's paper into confetti")
        player1score += 1
      else:
        print("Invalid move Player 2")
    else:
      print("Invalid move Player 1")
      
    if player1score == 1:
        win1 = "win"
    elif player1score == 0 or player1score == 2 or player1score == 3:
        win1 = "wins"
    
    if player2score == 1:
        win2 = "win"
    elif player2score == 0 or player2score == 2 or player2score == 3:
        win2 = "wins"
    print("Player 1 has", player1score, win1)
    print("Player 2 has", player2score, win2)
    if player1score==3 or player2score==3:
      print("Thanks for playing!")
      print("")
      print("")
      secretcode=input("Type anything to exit: ")
      if secretcode == "secretcode":
        password=input("Secret Code: ")
        if password == "9533359":
          continue
      else:
        RockPaperScissor = False
        os.system('clear')
        break

def colourchange(colour, text):
  if colour == 'red':
    return f'\033[0;31m{text}\033[0m' #red
  elif colour == 'green':
    return f'\033[0;32m{text}\033[0m' #green
  elif colour == 'blue':
    return f'\033[0;34m{text}\033[0m' #blue
  elif colour == 'yellow':
    return f'\033[1;33m{text}\033[0m' #yellow

def menu():
  menu=True
  while menu==True:
    print(f'{colourchange("red", "=")}={colourchange("blue", "=")} \033[1m{colourchange("yellow", "Game Menu")}\033[0m {colourchange("blue", "=")}={colourchange("red", "=")} '.center(104), sep = '',)
    print('')
    print(f'{colourchange("red", "Games Available.")}'.center(52))
    print('1. Guess the Number'.center(40))
    print('2. Character Battle'.center(40))
    print('3. Rock Paper Scissors'.center(40))
    menuinput=int(input('> '))
    if menuinput == 1:
      guess_number()
    if menuinput == 2:
      CharacterBuilder()
    if menuinput == 3:
      RockPaperScissors()
    else:
      print('I dont quite get that, can you please repeat that')
      time.sleep(2)
      os.system('clear')
menu()