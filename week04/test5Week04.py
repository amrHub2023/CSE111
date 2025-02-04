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


# "C13H16N2O2": Aspirina (CH3COOC6H4COOH) formula[i] "Na12C1" "Na12CH"
formula = "CH3COOC6H4COOH"   
formula_list=[]
form=""
i=0
while i!= len(formula):
    list1=[]
    if (i+1)!=len(formula):
        print(f'el elemento {i} es: {formula[i]} y el elemento i+1 es {formula[i+1]} ')
        if formula[i].isalpha() and formula[i+1].isalpha():
            if formula[i+1].islower():
                j=i+2
                if j != len(formula):# j est en el limite del string
                    var2=formula[j]
                    # var1=formula[j] 
                    while j != len(formula):
                        if formula[j+1].isdigit():
                            var2= var2 + formula[j+1] 
                            j=j+1
                        else:
                            var1=formula[i] +formula[i+1]     
                            list1.append(var1)
                            list1.append(var2)
                            print(list1)
                            formula_list.append(list1)
                            i=j+1    
                            break
                else:
                    var1=formula[i]+formula[i+1]
                    list1.append(var1)
                    list1.append(1)
                    formula_list.append(list1)
                    print(formula_list)  
                    i=j
                            
            else:
                var1=formula[i]
                list1.append(var1)
                list1.append(1)
                formula_list.append(list1)
                print(formula_list)
                i=i+1
        else:
            k=i+1
            if k+1 != len(formula):# j est en el limite del string            
                var2=formula[k]
                while k+1!=len(formula):   
                  if formula[k+1].isdigit():
                    var2=var2+formula[k+1]
                    k=k+1
                  else:
                       var1=formula[i]  
                       list1.append(var1)
                       list1.append(var2)  
                       formula_list.append(list1)   
                       print(formula_list)
                       i=k+1
                       break
            else:       
                var1=formula[i]
                var2=formula[k]
                list1.append(var1)
                list1.append(var2)              
                formula_list.append(list1) 
                print(formula_list)           
                i=k+1   
    else:
         var1=formula[i]
         list1.append(var1)
         list1.append(1)
         formula_list.append(list1)
         print(formula_list)  
         break   
              
              
              

    
    
    
    
    
    
    
    
    
    
    
    
        # if i.isalpha():
        #     list1.append(i)
        #     if (i+1).isalpha():                
        #         list1.append(1)
        #     else:
        #         list1.append(i+1)    
        #     formula_list.append(list1)

