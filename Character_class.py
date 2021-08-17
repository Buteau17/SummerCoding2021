import re


#AA1

pattern = r"[A-Z][A-Z][0-9]"

if re.search (pattern , "AH6"):
    print("Match found")
