
import random, os, time
def main():  
    while True:
        all=make_sentence()
        print(all)
        print("Do you want to make another sentence? (y/n): ")
        user_res=get_valid_option()
        if user_res.lower() == "n":
            break
        
        
def get_prepositional_phrase(quantity):
  """Build and return a prepositional phrase composed   of three words: a preposition, a determiner, and a
  noun by calling the get_preposition, get_determiner,and get_noun functions.
  Parameter
      quantity: an integer that determines if the determiner and noun in the prepositional
          phrase returned from this function should be single or pluaral.
  Return: a prepositional phrase.
  """       
  preposition=get_preposition() 
  print(f"the preposition from get_prepositional_phrase is: ",preposition)
  determiner=get_determiner(quantity)
  noun=get_noun(quantity)
  sentence = f"{preposition} {determiner} {noun} "
  prepositional_phrase=sentence
#   prepositional_phrase=sentence.capitalize()
  print(f"from GET PROPOSITIONAL PHRASE the prepositional phrase is ",random.choices(prepositional_phrase))
  return random.choice(prepositional_phrase)
  
def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
     "about", "above", "across", "after", "along","around", "at", "before", "behind", "below",
     "beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of",
     "off", "on", "onto", "out", "over","past", "to", "under", "with", "without"
      Return: a randomly chosen preposition.
    """
    preposition = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]
    # Randomly choose and return a preposition.     
    return random.choice(preposition)
        
def get_valid_option():#get a valid number from the user    
        while True:
            user_input = input(" ")
            if user_input == "n" or user_input == "y":
                return user_input
            else:
                print("Invalid input. Please enter a valid option (y/n) ")
def get_valid_tense():#get a valid tense from the user
     while True:
         user_input = input(" ")         
         if user_input.lower() == "past" or user_input.lower() == "present" or user_input.lower() == "future":       
             return user_input
         else:
             print("Invalid input. Please enter a valid tense (past/present/future) ")    
def get_valid_number():#get a valid number from the user
     while True:
         user_input = input(" ")
         if user_input == "0" or user_input == "1":
             return int(user_input)
         else:
             print("Invalid input. Please enter a valid quantity (0/1) ")
def make_sentence():
        print("Enter a quantity: 0/1: ")
        quantity = get_valid_number()        
        print("Enter a tense: past/present/future: ")
        tense = get_valid_tense()       
        determiner = get_determiner(quantity)
        noun = get_noun(quantity)
        verb = get_verb(quantity,tense)
        prepositional_phrase=get_prepositional_phrase(quantity)
        print(f"from the def make sentence, the prepositional phrase is: ",prepositional_phrase)
        sentence = f"{determiner} {noun} {verb} {prepositional_phrase}."
        all=sentence.capitalize()
        return all
    
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
        return random.choice(words)
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
                noun = ["bird", "boy", "car", "cat", "child","dog", "girl", "man", "rabbit", "woman"]
        else:
                noun = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]
        # Randomly choose and return a noun        
        return random.choice(noun)

def get_verb(quantity, tense):
        """Return a randomly chosen verb. If tense is "past",
        this function will return one of these ten verbs:
            "drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"
            
        If tense is "present" and quantity is 1, this
        function will return one of these ten verbs:
            "drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"
            
        If tense is "present" and quantity is NOT 1,
        this function will return one of these ten verbs:
            "drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"
            
        If tense is "future", this function will return one of
        these ten verbs:
            "will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"
            
        Parameters
            quantity: an integer that determines if the
                returned verb is single or plural.
            tense: a string that determines the verb conjugation,
                either "past", "present" or "future".
        Return: a randomly chosen verb.
        """ 
        if tense.lower() == "past":
            verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
        elif tense.lower() == "present" :
                #ask if present to enter and there it forks into 1 and 0
            if quantity == 1: 
                verbs = ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
            else:       
                verbs = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
            
        else:
            verbs = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
        return random.choice(verbs)
        # Randomly choose and return a verb
        

main()
print("Goodbye!")
print("Thank you for using this program")
print("author: Alejandro Moreno")
time.sleep(3)