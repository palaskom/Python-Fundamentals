import re

pattern = re.compile("flower")

match = pattern.match("flower power")  # search pattern at the beginning

if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())
