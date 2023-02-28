import random
from sprites import welcome_screen, gameover_message, death_message, win_message, display_knight
import os

# Setup ability to clear screen between scenes
clear = lambda: os.system('clear')

# Setup Player Class
class Character:
  def __init__(self):
    self.health = 1
    self.gold = 1
    self.name = ""  

# Setup player class
class Player(Character):
  def __init__(self):
    Character.__init__(self)
    self.status = 'normal'
    self.health = 100
    self.attack = 20
    self.gold = 0
    self.goblin_kills = 0

  # Print Actions CMD
  def actions(self):
    print("CMDs: " + ', '.join(str(x) for x in cmds.keys()) + ".")

  # Clear Screen CMD
  def clear(self):
    clear()
    print(name + " is in a dark dungeon...""\n" "Would you like to explore further?")
    print("Type 'actions' to determine your next move")

  # Player Quit CMD
  def quit(self):
    clear()
    gameover_message()
    quit()

  # Player Health Check CMD
  def health(self):
    print(name + "'s Health:", self.health, "hp")

  # Fight Enemy CMD
  def fight(self):
    self.enemy = Enemy(self)
    if self.status != 'normal':
      fight_roll = random.randint(1, 10)
      if fight_roll > 5:
        self.enemy.health = (self.enemy.health - self.attack)
        self.gold = (self.gold + 5)
        self.goblin_kills += 1
        print("You rolled a", fight_roll)
        print("You killed the Goblin!")
        print("You gain 5 gold coins!")
        self.status = 'normal'
      else:
        self.health = (self.health - self.enemy.attack)
        print("You rolled a", fight_roll)
        print("You missed and the Goblin attacks you for 10hp damage!")
    else:
      print("There is nothing for you to fight...")

  # Player Run CMD
  def run(self):
    self.enemy = Enemy(self)
    if self.status != 'normal':
      run_roll = random.randint(1, 10)
      if run_roll > 5:
        print("You rolled a", run_roll)
        print("You managed to escape!")
        self.status = 'normal'
      else:
        self.health = (self.health - self.enemy.attack)
        print("You rolled a", run_roll)
        print("The golbin attacks you for 10hp damage!")
    else:
      print("You have nothing to run from...")

  # Player Explore CMD
  def explore(self):
    if self.status == 'normal':
      explore_roll = random.randint(1, 10)
      if explore_roll > 5:
        print("You rolled a", explore_roll)
        print("You find 1 gold coin!")
        self.gold = (self.gold + 1)
      else:
        print("You rolled a", explore_roll)
        print("A Goblin appears!")
        self.status = 'danger'
    else:
      print("You must face the Goblin or run away!")

  # Player Leave CMD
  def leave(self):
    if self.status == 'normal':
      leave_roll = random.randint(1, 10)
      if leave_roll > 5:
        print("You rolled a", leave_roll)
        print("You managed to leave the dungeon")
        leave_message = input("Press [ENTER] to Continue...")
        clear()
        gameover_message()
        print("End Game Stats:" "\n")
        print("Health:", self.health, "hp")
        print("Gold:", self.gold, "gold coin(s)")
        print("Goblin Kills:", self.goblin_kills)        
        end_message =input("Press [ENTER] to End Game...")
        quit()
      else:
        print("You rolled a", leave_roll)
        print("You are unable to find your way out!")
    else:
      print("You must face the Goblin or run away!")
      
  # Player Inventory CMD
  def inventory(self):
    print(name + "'s inventory:", self.gold, "gold coin(s)")
      
# Setup Enemy Class
class Enemy(Character):
  def __init__(self, player):
    Character.__init__(self)
    self.name = "Goblin"
    self.health = 20
    self.attack = 10

# Ask Player For Their Name
name = input("Enter your player name: ")

# Create A New player
new_player = Player()

# Display Starting Player Stats and character
print("\n""Name: " + name)
print("Starting Health:", new_player.health, "hp")
print("Attack:", new_player.attack, "hp")
print("Gold:", new_player.gold)
display_knight()

# Start Prompt
readyup = input("\n""Press [ENTER] to Begin...")

# Clear Screen to start game
clear()

# Intro Screen
welcome_screen()

# Basic story line for character
print(name + ",""""
You are a well traveled adventurer. You've faced many dangers and 
fought the most evil of foes. As your quest continues, you approach 
an old dungeon with torches that light the entrance. Should you choose 
to enter, you'll face your greatest challenge yet. Collect all 20 gold
coins to win the game, but beware of the goblins that lurk within.
\n
It's time to... ENTER THE DUNGEON.
""")

enter_dungeon = input("\n""Press [ENTER] to Enter...")

# Clear Screen
clear()

# Player Cmds
cmds = {
  'actions': Player.actions,
  'explore' : Player.explore,
  'fight': Player.fight,
  'run' : Player.run,  
  'health': Player.health,
  'inventory' : Player.inventory,
  'clear': Player.clear,
  'leave': Player.leave,
  'quit': Player.quit,
}

print(name + " enters a dark dungeon...""\n" "Would you like to explore further?")
print("Type 'actions' to determine your next move")

# Take cmds from player to determine their moves
while (new_player.health > 0 and new_player.gold < 20):
  line = input("~ ").lower()
  args = line.split()
  if len(args) > 0:
    commandFound = False
    for c in cmds.keys():
      if args[0] == c[:len(args[0])]:
        cmds[c](new_player)
        commandFound = True
        break
    if not commandFound:
      print("Action not listed, please try again...")

# You Died message when player health <= 0
if new_player.health <= 0:
  clear()
  death_message()
  quit_game = input("Press [ENTER] to Quit...")
  quit()

# Player wins the game after collecting 20 gold coins
if new_player.gold >= 20:  
  clear()
  win_message()
  print("End Game Stats:" "\n")
  print("Health:", new_player.health, "hp")
  print("Gold:", new_player.gold, "gold coin(s)")
  print("Goblin Kills:", new_player.goblin_kills)        
  end_message =input("\n" "Press [ENTER] to End Game...")
  quit()
  