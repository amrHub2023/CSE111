# name = ["susan","Chris"]
# print(len(name))
# name.insert(0,"Ale")
# print(name)
# name.sort()
# print(name)
# name.append("Manu")
# print(name)
# present= name[1:3]
# print(name)
# print(present)
# person={"first":"Chris"}
# person["last"]= "Harrison"
# print(person)
# print(person["first"])






    # # Create an empty list that will hold fabric names.
    # fabrics = []
    # # Add three elements at the end of the fabrics list.
    # fabrics.append("velvet")
    # fabrics.append("denim")
    # fabrics.append("gingham")
    # # Insert an element at the beginning of the fabrics list.
    # fabrics.insert(0, "chiffon")
    # print(fabrics)
    # # Determine if gingham is in the fabrics list.
    # if "gingham" in fabrics:
        # print("gingham is in the list.")
    # else:
        # print("gingham is NOT in the list.")
    # # Get the index where velvet is stored in the fabrics list.
    # i = fabrics.index("velvet")
    # # Replace velvet with taffeta.
    # fabrics[i] = "taffeta"
    # # Remove the last element from the fabrics list.
    # fabrics.pop()
    # # Remove denim from the fabrics list.
    # fabrics.remove("denim")
    # # Get the length of the fabrics list and print it.
    # n = len(fabrics)
    # pri   nt(f"The fabrics list contains {n} elements.")
    # print(fabrics)
    # # Call main to start this program.
    # if __name__ == "__main__":
    # main()
word=["apple","banana","cherry","date","elderberry","fig","grape"]    
import random
def main(): 
    w_list = []       
    numbers = [16.2,75.1,52.3]
    append_random_numbers(numbers) 
    print(f"con quantity = 1")
    print(numbers)
    append_random_numbers(numbers,3) 
    print(f"con quantity = 3")
    print(numbers)
    append_random_words(w_list)
    print(w_list)
    append_random_words(w_list,3)
    print(w_list)
def append_random_words(w_list,quantity=1): 
    for _ in range(quantity):        
        w_list.append(random.choice(word))
    
def append_random_numbers(number_list,quantity=1):
    for _ in range(quantity):
        temp=round(random.uniform(0,100),1)        
        number_list.append(temp)        
if __name__ == "__main__":        
    main()    
    
