# # Initialize a list with integers from 1 to 5
# my_list = [1, 2, 3, 4, 5]

# a = [1, 2, 3, 1, 2, 4, 5, 6, 5]

# # List to store duplicates
# dup = []

# # Compare each element with other elements
# for i in range(len(a)):
    # for j in range(i + 1, len(a)):

        # # If a duplicate is found and not already recorded
        # if a[i] == a[j] and a[i] not in dup:
            
            # # Add to duplicates list
            # dup.append(a[i]) 

# myList.pop(1)



# Remove and return the element at index 2 (third element) from the list
# removed_item = my_list.pop(2)
lista2= [ 
['Ac', 'Actinium', 227.0],
['Ag', 'Silver', 107.8682],
['Al', 'Aluminum', 26.9815386],
['Ar', 'Argon', 39.948],
['As', 'Arsenic', 74.9216],
['At', 'Astatine', 210.0],
['Au', 'Gold', 196.966569] ]
dulces = [["magdalena", "2"], [ "piruleta", "tarta"], [ "magdalena", "3"],
          ["caramelo2", "piruleta"],["magdalena",1], ["caramelo", "magdalena"]]
# l = [1,2,3,1,4,5,1]
# print(l.count(1))

def del_repeat(list_input):
    for i in range(len(list_input)):
       for j in range(i + 1, len(list_input)):
         if j < len(list_input):
            print(f"dulces[i][0] es {list_input[i][0]} y dulces[j][0] es {list_input[j][0]}")
            if list_input[i][0] == list_input[j][0]:
               list_input[i][1]= int(list_input[i][1])+ int(list_input[j][1])
               list_input.pop(j)        
               print(list_input[i][1])
    print(list_input)          
    return list_input           
list=del_repeat(dulces)            
      # # If a duplicate is found and not already recorded
      # if a[i] == a[j] and a[i] not in dup:





# for i in range(len(dulces)- 1):
  # j=i+1
  # var1=dulces[i][0]
  # print(f"la variable v1 de dulces[i][0] es {var1}")
  # repeat_counter= dulces[i].count(var1)
  # print("repeat_counter es :",repeat_counter)
  # while j <= repeat_counter:
    # if dulces[i][0] == dulces[j][0]:
        #  dulces[i][1]= int(dulces[i][1])+ int(dulces[j][1])
        #  print(dulces[i][1])
    # j=j+1    
  # print(dulces[i], dulces[i + 1])
  # print(dulces[i][0][1], dulces[i + 1][0])
  
  
  
  
  
  
# caramelos_únicos = []
# k=0
# for dulce in dulces:
  # repeat_counter=dulces.count(dulce)
  # i=0
  # K=dulces.index(dulce)
  
  # while i <= repeat_counter:
    # k=k+1  
    # if dulce == dulces[k]:
      
  
  # if dulce not in caramelos_únicos:
    # caramelos_únicos.append(dulce)

# print(caramelos_únicos)


# def find_and_add_second_elements(list_of_lists):
  # seen_elements = set()
  # result = []
  # for sublist in list_of_lists:
    # if sublist[0] in seen_elements:
      # result.append(sublist[1])
    # else:
      # seen_elements.add(sublist[0])
  # return result

# # Example usage
# list_of_lists = [
  # [1, 'a'],
  # [2, 'b'],
  # [1, 'c'],
  # [3, 'd'],
  # [2, 'e']
# ]

# print(find_and_add_second_elements(list_of_lists))
# for i in range(len(dulce) - 1):
  # print(dulce[i], dulce[i + 1])
