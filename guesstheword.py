import random
import re

myDictionary = ["afternoon",
"alligator",
"amusement",
"another",
"anything",
"audio",
"beach",
"beam",
"big",
"blue",
"bolder",
"brook",
"car",
"carpet",
"castle",
"chair",
"charmed",
"chimney",
"chocolate",
"clock",
"clue",
"coconut",
"coffee",
"compare",
"computer",
"content",
"cow",
"cowboy",
"crocodile",
"curtain",
"database",
"dinosaur",
"dollar",
"drive",
"duck",
"duplicate",
"ears",
"elusive",
"eyes",
"fan",
"farm",
"first",
"floral",
"flying",
"grass",
"green",
"helicopter",
"honest",
"honey",
"hopper",
"horse",
"house",
"human",
"indigo",
"information",
"intuition",
"jumping",
"laptop",
"large",
"last",
"leap",
"leaves",
"light",
"llama",
"love",
"mall",
"marker",
"mint",
"minute",
"mist",
"morning",
"network",
"northern",
"nose",
"nothing",
"notification",
"novel",
"oak",
"oak",
"ocean",
"official",
"olive",
"opal",
"orange",
"original",
"park",
"park",
"pen",
"pencil",
"phone",
"pine",
"pink",
"plank",
"polygon",
"poodle",
"popsicle",
"prince",
"protocol",
"purple",
"purse",
"queen",
"radio",
"rainbow",
"rainy",
"ranch",
"real",
"record",
"ring",
"river",
"rooster",
"rose",
"round",
"running",
"second",
"shoe",
"short",
"skate",
"small",
"snowman",
"sofa",
"someone",
"sparkle",
"special",
"spot",
"spring",
"square",
"squirrel",
"store",
"story",
"strawberry",
"sunny",
"super",
"sweet",
"swing",
"table",
"tall",
"technology",
"television",
"there",
"third",
"time",
"trapezoid",
"tree",
"vanilla",
"video",
"wallet",
"water",
"website",
"western",
"wheel",
"window",
"windy",
"wonder",
"wonderful",
"words",
"xylophone",
"yellow",
"yodel",
"zebra",
"zipper"]

def show_board():
  print("\n%s # of bad guesses left: %d" % ('{0: <35}'.format("Already guessed: %s" % " ".join(wrong)), 8-len(wrong)))
  print("Word: %s" % " ".join(blanks))

def take_a_guess():
  show_board()
  guess = input('\n')  
  if not re.fullmatch('[a-zA-Z]', guess): 
    if guess == word:
      for index in range(len(letters)):   
        blanks[index] = letters[index]
      show_board()
      play_again("\nYou win! Play again? Y/N")
    else:
      if len(guess)==1:
        print("Guesses must be a letter.")
      else:
        print("No, that's not the word.")
      
      take_a_guess()
  else: 
    if guess in wrong or guess in blanks:
      print("You already guessed letter %s." % guess)
      take_a_guess()
    else:
      matches = [index for index, letter in enumerate(letters) if letter == guess]
  
      if not matches:
        wrong.append(guess)
   
        if len(wrong) == 8:
          play_again("\nYou lose! The word was: %s Play again? Y/N" % word)
        else:
          take_a_guess()
      else:
        for match in matches:
          blanks[match] = guess
 
        if blanks.count("_") == 0:
          show_board()
          play_again("\nYou win! Play again? Y/N")
        else:
          take_a_guess()

def play_again(message):
  again = input(message)
  if again == "y" or again == "Y":
    global word 
    word = random.choice(myDictionary)
    myDictionary.remove(word)
    global letters
    letters = list(word)
    global blanks 
    blanks = ["_"] * len(letters)
    global wrong
    wrong = []
    take_a_guess()
  else:
    print("\nGoodbye!")
  
          
word = random.choice(myDictionary)
myDictionary.remove(word)
letters = list(word)
blanks = ["_"] * len(letters)
wrong = []
print("\nTry and guess the letters in the word below. \nTo make a guess click any letter and press enter. \nIf you make eight bad guesses you lose. \nType the word if you think you know it. \nA wrong answer won't count against you.")
take_a_guess()
