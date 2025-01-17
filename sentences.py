
# make_sentence()
# get_determiner()deben elegir aleatoriamente una palabra
# get_noun() de una lista y devolver la palabra elegida
# get_verb()
# main()
import random
words=["boy","girl","cat","dog","bird","house"]
word=random.choice(words)
print(word)
# given = "Michelle"
# middle = "Aya"
# surname = "Takechi"
# full_name = f"{given} {middle} {surname}"
# print(full_name)

def get_determiner(quantity):
  """Return a randomly chosen determiner. A determiner is
  a word like "the", "a", "one", "some", "many".
  If quantity is 1, this function will return either "a",
  "one", or "the". Otherwise this function will return
  either "some", "many", or "the".
  Parameter
      quantity: an integer.
          If quantity is 1, this function will return a
          determiner for a single noun. Otherwise this
          function will return a determiner for a plural
          noun.
  Return: a randomly chosen determiner.
  """
  if quantity == 1:
      words = ["a", "one", "the"]
  else:
      words = ["some", "many", "the"]
  # Randomly choose and return a determiner.
  word = random.choice(words)
  return word
def get_noun(quantity):
  """Return a randomly chosen noun.
  If quantity is 1, this function will
  return one of these ten single nouns:
      "bird", "boy", "car", "cat", "child",
      "dog", "girl", "man", "rabbit", "woman"
  Otherwise, this function will return one of
  these ten plural nouns:
      "birds", "boys", "cars", "cats", "children",
      "dogs", "girls", "men", "rabbits", "women"
  Parameter
      quantity: an integer that determines if
          the returned noun is single or plural.
  Return: a randomly chosen noun.
    """
  if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
  else:
        words = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]
# Randomly choose and return a determiner
  word = random.choice(words)
  return word