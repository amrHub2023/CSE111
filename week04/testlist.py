# main_list = []
# inner_list1 = []
# inner_list1.append("dato1")
# inner_list1.append("dato2")
# inner_list2 = []
# inner_list2.append("dato3")
# inner_list2.append("dato4")
# main_list.append(inner_list1)
# main_list.append(inner_list2)
# print(main_list)


# "C13H16N2O2": Aspirina (CH3COOC6H4COOH)
formula = "C13H16N2O2"   
formula_list=[]
form=""
i=0
for row in formula:
    list1=[]
    if (i+1)!=len(formula):
        if row.isalpha() and (row+1).isalpha():
            if (row+1).islower():
                j=i+2
                row2=formula(j)
                var1=row(j)
                while j != len(formula):
                    if (j+1).isdigit():
                        var2= var2 + (j+1)
                        j=j+1
                    else:
                        var1=i+(i+1)    
                        list1.append(var1)
                        list1.append(var2)
                        print(list1)
                        formula_list.append(list1)
                    i=j+1    
                    break
            else:
                var1=i
                list1.append(var1)
                list1.append(1)


    
    
    
    
    
    
    
    
    
    
    
    
  
  
           
  
  
  
  


            
       
