import re

pattern = r"eggs(bacon)*"

if re.match (pattern, "eggsbacon"):
    print("Match found")