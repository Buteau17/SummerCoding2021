import re


pattern = r"eggs"
if re.match(pattern, "baconeggseggsebacon"):
    print('Match found')
else:
    print('No match found')

if re.search(pattern, "baconeggseggsbacon"): 
    print('Match found')
else:
    print("No match found")

print (re.findall(pattern, "baconeggseggsbacon"))
        




