
class FormulaError(ValueError):
    """FormulaError is the type of error that the parse_formula
    function will raise if a formula is invalid.
    """


def parse_formula(formula, periodic_table_dict):
    """Convert a chemical formula for a molecule into a compound
    list that stores the quantity of atoms of each element
    in the molecule. For example, this function will convert
    "H2O" to [["H", 2], ["O", 1]] and
    "PO4H2(CH2)12CH3" to [["P", 1], ["O", 4], ["H", 29], ["C", 13]]

    Parameters
        formula is a string that contains a chemical formula
        periodic_table_dict is the compound dictionary returned
            from make_periodic_table
    Return: a compound list that contains chemical symbols and
        quantities like this [["Fe", 2], ["O", 3]]
    """
    assert isinstance(formula, str), \
        "wrong data type for parameter formula; " \
        f"formula is a {type(formula)} but must be a string"
    assert isinstance(periodic_table_dict, dict), \
        "wrong data type for parameter periodic_table_dict; " \
        f"periodic_table_dict is a {type(periodic_table_dict)} " \
        "but must be a dictionary"
    #  "C13H16N2O2": Aspirina (CH3COOC6H4COOH)
    i=0
    formula_list=[]
    while i!= len(formula):
        list1=[]
        if (i+1)!=len(formula):
            print(f'el elemento {i} es: {formula[i]} y el elemento i+1 es {formula[i+1]} ')
            if formula[i].isalpha() and formula[i+1].isalpha():
                if formula[i+1].islower():
                    j=i+2
                    if j != len(formula):# j est en el limite del string
                        var2=formula[j]                        
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
    # return formula_list
    for row in formula_list:
        if row[0] in 
          
    
    
    
    
        
    
    
    
    


            
      



    def parse_quant(formula, index):
        quant = 1
        if index < len(formula) and formula[index].isdecimal():
            if formula[index] == "0":
                raise FormulaError("invalid formula, "
                    "quantity begins with zero (0), perhaps "
                    "you meant to type capital O for Oxygen "
                    "instead of zero", formula, index)
            start = index
            index += 1
            while index<len(formula) and formula[index].isdecimal():
                index += 1
            quant = int(formula[start:index])
        return quant, index

    def get_quant(elem_dict, symbol):
        return 0 if symbol not in elem_dict else elem_dict[symbol]

    def parse_r(formula, index, level):
        start_index = index
        start_level = level
        elem_dict = {}
        while index < len(formula):
            ch = formula[index]
            if ch == "(":
                group_dict, index = parse_r(formula,index+1,level+1)
                quant, index = parse_quant(formula, index)
                for symbol in group_dict:
                    prev = get_quant(elem_dict, symbol)
                    curr = prev + group_dict[symbol] * quant
                    elem_dict[symbol] = curr
            elif ch.isalpha():
                symbol = formula[index:index+2]
                if symbol in periodic_table_dict:
                    index += 2
                else:
                    symbol = formula[index:index+1]
                    if symbol in periodic_table_dict:
                        index += 1
                    else:
                        raise FormulaError("invalid formula; "
                            f"unknown element symbol: {symbol}",
                            formula, index)
                quant, index = parse_quant(formula, index)
                prev = get_quant(elem_dict, symbol)
                elem_dict[symbol] = prev + quant
            elif ch == ")":
                if level == 0:
                    raise FormulaError("invalid formula; "
                        "unmatched close parenthesis",
                        formula, index)
                level -= 1
                index += 1
                break
            else:
                if ch.isdecimal():
                    # Decimal digit not preceded by an
                    # element symbol or close parenthesis
                    message = "invalid formula"
                else:
                    # Illegal character: [^()0-9a-zA-Z]
                    message = "invalid formula; " + \
                        f"illegal character: {ch}"
                raise FormulaError(message, formula, index)
        if level > 0 and level >= start_level:
            raise FormulaError("invalid formula; "
                "unmatched open parenthesis",
                formula, start_index - 1)
        return elem_dict, index

    # Return the compound list of element symbols and
    # quantities. Each element in the compound list
    # will be a list in this form: ["symbol", quantity]
    elem_dict, _ = parse_r(formula, 0, 0)
    return list(elem_dict.items())
