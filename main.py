import turtle as trtl
ali = trtl.Turtle()


#This will run if the game they choose is ABC

def alphabetGame(name):
  ali.penup()
  ali.goto(20,-70)
  ali.pendown()
  ali.fillcolor("red")
 
 # Assigning each letter input a coordinate 
  letterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']
  coord = [(20,-60), (10,-30), (50,-40), (40,-30), (90,10), (70,20), (80,50), (50,40), (50,50),(30,40), (40,90), (20,70), (0,100), (-20,70), (-40,80), (-30,30), (-50, 60), (-50, 40), (-80, 50), (-70,20), (-90,10), (-40,-20), (-50, -40), (0,-30), (20, -70), (20, -60)]
  
  
  #Asking for input and if correct it will move Ali to associated coordinate
  alphabet = 0
  while alphabet < 26:
    ali.begin_fill()
    val = input("what's the next letter of the alphabet")
    if val == letterList[alphabet]:
      ali.goto(coord[alphabet])
      alphabet = alphabet + 1
    elif val != letterList[alphabet]:
      print("That answer is close! Please try again " + name)
  ali.end_fill()    
      
  print("Good job " + name + "! Now you know your ABC´s! :)")
  
#this will run if the number game is chosen  
def numberGame(name):
  #assinging each number a coordinate
  numList = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
  coord = [(90,60), (80,50), (60,60), (40,50), (20,60), (0,50), (20,100), (50,120), (80,100), (90,100), (90,110),  (100,100), (110, 110), (110, 100), (120, 100), (150,120), (180,100), (200,50), (180, 60), (160,50), (140,60), (120,50), (110,60), (110,40), (100,60), (90,40) ] 
  
  ali.penup()
  ali.goto(90,40)
  ali.pendown()
  ali.fillcolor("black")
  
  
  #Asking for input and if correct it will move Ali to associated coordinate
  numbers = 0
  while numbers < 26:
    ali.begin_fill()
    val = int(input("What number is next: "))
    if val == numList[numbers]:
      ali.goto(coord[numbers])
      numbers = numbers + 1
    elif val != numList[numbers] or val == None:
      print("That answer is close! Please try again " + name)
  ali.end_fill()

  print("Good job "+ name + "! Now you know your numbers! :)")

      



#Will ask to play another game after they finish playing  
my_name = input("What is your name?")
stillPlaying = True  
while stillPlaying == True:
  game = input("Hi " + my_name + "! Do you want to play a game? yes or no")
  
  if game == "yes":
    gameChoice = input("Ok! What game would you like to play? ABC's or numbers")
    
    if gameChoice == "ABC's":
      alphabetGame(my_name)
  

    elif gameChoice == "numbers":
      numberGame(my_name)
  
  if game == "no":
    print("Okay! Thank you for playing " + my_name + "!")
    stillPlaying = False
