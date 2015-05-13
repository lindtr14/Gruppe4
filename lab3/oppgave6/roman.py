def romanAddition(x, y):
    """Function to perform addition with two roman numerals"""
    
    # Replace the x and y parameters with longer roman numerals
    suby1 = y.replace("CM", "DCCCC")
    suby2 = suby1.replace("CD", "CCCC")
    suby3 = suby2.replace("XC", "LXXXX")
    suby4 = suby3.replace("XL", "XXXX")
    suby5 = suby4.replace("IX", "VIIII")
    suby6 = suby5.replace("IV", "IIII")
    
    subx1 = x.replace("CM", "DCCCC")
    subx2 = subx1.replace("CD", "CCCC")
    subx3 = subx2.replace("XC", "LXXXX")
    subx4 = subx3.replace("XL", "XXXX")
    subx5 = subx4.replace("IX", "VIIII")
    subx6 = subx5.replace("IV", "IIII")

    # Making result into a string
    # Combining the parameters into one string
    result = ""
    add = subx6 + suby6
    result += add

    # Sorting with a condition
    valueOrder = "MDCLXVI"
    sortingList = sorted(result, key=valueOrder.index)
    

    
    str1 = ''.join(sortingList)
    
    # Replace the long roman numeral with an original roman numeral
    tmp1 = str1.replace("IIIII", "V")
    tmp2 = tmp1.replace("VV", "X")
    tmp3 = tmp2.replace("XXXXX", "L")
    tmp4 = tmp3.replace("LL", "C")
    tmp5 = tmp4.replace("CCCCC", "D")
    tmp6 = tmp5.replace("DD", "M")
    
    tmp7 = tmp6.replace("VIIII", "IX")
    tmp8 = tmp7.replace("IIII", "IV")
    tmp9 = tmp8.replace("XXXX", "XL")
    tmp10 = tmp9.replace("LXXXX", "XC")
    tmp11 = tmp10.replace("CCCC", "CD")
    tmp12 = tmp11.replace("DCCCC", "CM")
    
    return tmp12
  
def romanSubtraction(x, y):
    """Function to perform a subtraction with two roman numerals"""
                   
    # Replace the x and y parameters with longer roman numerals
    suby1 = y.replace("CM", "DCCCC")
    suby2 = suby1.replace("CD", "CCCC")
    suby3 = suby2.replace("XC", "LXXXX")
    suby4 = suby3.replace("XL", "XXXX")
    suby5 = suby4.replace("IX", "VIIII")
    suby6 = suby5.replace("IV", "IIII")
    suby7 = suby6.replace("M", "DD")
    suby8 = suby7.replace("D", "CCCCC")
    suby9 = suby8.replace("C", "LL")
    suby10 = suby9.replace("L", "XXXXX")
    suby11 = suby10.replace("X", "VV")
    suby12 = suby11.replace("V", "IIIII")
    
    subx1 = x.replace("CM", "DCCCC")
    subx2 = subx1.replace("CD", "CCCC")
    subx3 = subx2.replace("XC", "LXXXX")
    subx4 = subx3.replace("XL", "XXXX")
    subx5 = subx4.replace("IX", "VIIII")
    subx6 = subx5.replace("IV", "IIII")
    subx7 = subx6.replace("M", "DD")
    subx8 = subx7.replace("D", "CCCCC")
    subx9 = subx8.replace("C", "LL")
    subx10 = subx9.replace("L", "XXXXX")
    subx11 = subx10.replace("X", "VV")
    subx12 = subx11.replace("V", "IIIII")
    
    # Adding every character for x and y in a list
    charX = []
    for string in subx12:
        for char in string:
            charX.append(char)
                
    charY = []
    for string in suby12:
        for char in string:
            charY.append(char)
            
     # For each common character in both lists, remove it            
    for char in charX[:]:
        if char in charY:
            charX.remove(char)
            charY.remove(char)

    # Making result into a string
    result = ""
    
    sub1 = ''.join(charX)
    sub2 = ''.join(charY)
    
    sub = sub1 + sub2
    result += sub
    
    # Sorting with a condition
    valueOrder = "MDCLXVI"
    sortingList = sorted(result, key=valueOrder.index)
    

    
    str1 = ''.join(sortingList)
    
    # Replace the long roman numeral to original roman numereal
    tmp1 = str1.replace("IIIII", "V")
    tmp2 = tmp1.replace("VV", "X")
    tmp3 = tmp2.replace("XXXXX", "L")
    tmp4 = tmp3.replace("LL", "C")
    tmp5 = tmp4.replace("CCCCC", "D")
    tmp6 = tmp5.replace("DD", "M")
    
    tmp7 = tmp6.replace("VIIII", "IX")
    tmp8 = tmp7.replace("IIII", "IV")
    tmp9 = tmp8.replace("LXXXX", "XC")
    tmp10 = tmp9.replace("XXXX", "XL")
    tmp11 = tmp10.replace("DCCCC", "CM")
    tmp12 = tmp11.replace("CCCC", "CD")
    
    return tmp12
    
# Sources
# romanAddition and romanSubtraction is written in cooperation
# with Lars Martin Risdal's group
