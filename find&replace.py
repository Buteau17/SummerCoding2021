
import re
string="My name is John , Hi i'm John"
pattern = r"John"

newstring=re.sub(pattern , "Ralph", string)
print(newstring)


