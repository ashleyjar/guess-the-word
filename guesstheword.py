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

class Game:
  def __init__(self, word):
    self.word = word
    self.letters = list(self.word)
    self.blanks = ["_"] * len(self.letters)
    self.wrong = []
    
  def reset(self, word):
    self.word = word
    self.letters = list(self.word)
    self.blanks = ["_"] * len(self.letters)
    self.wrong = []

def show_board():
  print("\n%s # of bad guesses left: %d" % ('{0: <35}'.format("Already guessed: %s" % " ".join(g.wrong)), 8-len(g.wrong)))
  print("Word: %s" % " ".join(g.blanks))

def take_a_guess():
  show_board()
  guess = input('\n')  
  if not re.fullmatch('[a-zA-Z]', guess): 
    if guess == g.word:
      for index in range(len(g.letters)):   
        g.blanks[index] = g.letters[index]
      show_board()
      play_again("\nYou win! Play again? Y/N: ")
    else:
      if len(guess)==1:
        print("Guesses must be a letter or word.")
      else:
        print("No, that's not the word.")
      
      take_a_guess()
  else: 
    if guess in g.wrong or guess in g.blanks:
      print("You already guessed letter %s." % guess)
      take_a_guess()
    else:
      matches = [index for index, letter in enumerate(g.letters) if letter == guess]
  
      if not matches:
        g.wrong.append(guess)
   
        if len(g.wrong) == 8:
          play_again("\nYou lose! The word was: %s. Play again? Y/N: " % g.word)
        else:
          take_a_guess()
      else:
        for match in matches:
          g.blanks[match] = guess
 
        if g.blanks.count("_") == 0:
          show_board()
          play_again("\nYou win! Play again? Y/N: ")
        else:
          take_a_guess()

def play_again(message):
  again = input(message)
  if again == "y" or again == "Y":
    if not myDictionary:
      print("\nYou guessed all the words. Goodbye!")
    else:
     g.reset(random.choice(myDictionary))
     myDictionary.remove(g.word)
     take_a_guess()
  else:
    print("\nGoodbye!")
  
          

g = Game(random.choice(myDictionary))
myDictionary.remove(g.word)

print("\nTry and guess the letters in the word below."
      "\nTo make a guess click any letter and press enter."
      "\nIf you make eight bad guesses you lose." 
      "\nType the word if you think you know it." 
      "\nA wrong answer won't count against you.")
take_a_guess()
