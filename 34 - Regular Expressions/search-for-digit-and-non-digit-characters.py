import re

pattern = re.compile(r"\d")  # any digit

sentence = "I want to the store and bought 5 apples, 4 oranges, and 15 plums."

print(pattern.findall(sentence))

pattern = re.compile(r"\D")  # non-digit

print(pattern.findall(sentence))
