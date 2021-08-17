import re


pattern = r"eggs"
if re.match(pattern, "baconeggseggseggsbacon"):
    print('Match found')
else:
    print('No match found')