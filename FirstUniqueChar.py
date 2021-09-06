# using while loop
s = "charanrajgowda"
while s != "":
   slen0 = len(s)
   ch = s[0]
   s = s.replace(ch, "")
   slen1 = len(s)
   if slen1 == slen0-1:
      print ("First non-repeating character is: ",ch)
      break;
   else:
    print ("No Unique Character Found!")
