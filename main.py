print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************  
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

decision_1 = input("Choose Left Or Right \n").lower()

if decision_1 == 'left':
  print('good going forward.....\n')

  decision_2 = input("Do You Want To Swim Or Wait?\n").lower() 

  if decision_2 == 'wait':
    sub_decision_2 = input('The Boat has arrived, Do you want to get in?( y / n) \n')
    if sub_decision_2 == 'y':
      print('happy journey, you will reach the island in no time! ')

      decision_3 = input("Choose Which Color Door - (Red, Blue, Yellow) - ").lower()

      if decision_3 ==  'red':
        print('you got burned by fire')
      elif decision_3 == 'blue':
        print('you have been eaten by beasts')
      else:
        print('You Won')
    else:
      print('why didnt you take the boat bro!! \n you died psst!!')
  else:
    print('you died mate, alligator has killed you!')

else:
  print('You lost mate, you fell into hole')


