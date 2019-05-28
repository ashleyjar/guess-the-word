import random

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

def take_a_guess():
  print("")
  guess = input('Choose a letter and click enter:')  
  if guess in wrong or guess in found:
    print("")
    print("You already guessed that letter.")
    take_a_guess()
  else:
    matches = [index for index, letter in enumerate(letters) if letter == guess]
  
    if len(matches) == 0:
      wrong.append(guess)
      chances = 8-len(wrong)
      print("")
      print("Already guessed: %s" % " ".join(wrong))
      print("# of bad guesses left: %d" % chances)
      print("Word: %s" % " ".join(blanks))
      if len(wrong) == 8:
        print("")
        print("You lose!")
      else:
        take_a_guess()
    else:
      found.append(guess)
      for match in matches:
        blanks[match] = guess
      chances = 8-len(wrong)
      print("")
      print("Already guessed: %s" % " ".join(wrong))
      print("# of bad guesses left: %d" % chances)
      print("Word: %s" % " ".join(blanks))
      if blanks.count("_") == 0:
        print("")
        print("You win!")
      else:
        take_a_guess()


word = random.choice(myDictionary)
myDictionary.remove(word)
letters = list(word)
blanks = ["_"] * len(letters)
found = []
wrong = []

print("")
chances = 8-len(wrong)
print("")
print("Already guessed: %s" % " ".join(wrong))
print("# of bad guesses left: %d" % chances)
print("Word: %s" % " ".join(blanks))
take_a_guess()
