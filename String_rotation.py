def checkRotation(s1, s2): 
    temp = ''
    if len(s1) != len(s2): 
        return False
  
    # concatenating both strings
    temp = s1 + s1 
    if s2 in temp: 
        return True #returning true if 2nd string is present in concatenated string
    else: 
        return False
# Driver
string1 = "HELLO"
string2 = "LOHEL"
  
if checkRotation(string1, string2): 
    print("Given Strings are rotations of each other.")
else: 
    print("Given Strings are not rotations of each other.")
