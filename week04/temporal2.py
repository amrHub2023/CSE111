def remove_duplicates(input_list):
    unique_elements = [input_list[1]]
    for element in input_list:
      if element[0] not in unique_elements[0]:
        unique_elements.append(element)
        print(unique_elements)
        print(element[1])
        print(unique_elements[1])
        print(unique_elements[1][1])
      else:
         unique_elements[1][1]=unique_elements[1][1]+(element[1])
         print(unique_elements)
    return unique_elements

# Example usage
dulces = [["magdalena", "2"], ["piruleta", "tarta"], ["magdalena", "3"],
    ["caramelo", "7"], ["magdalena", 1], ["caramelo", "9"]]

# Removing duplicates
dulces = remove_duplicates(dulces)
print(dulces)