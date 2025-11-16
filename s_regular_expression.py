# | Function       | Purpose
# | -------------- | ------------------------------------
# | `re.search()`  | Find first match in the text
# | `re.findall()` | Find all matching results
# | `re.sub()`     | Replace text
# | `re.match()`   | Check match **at beginning** of text

# | Pattern | Meaning
# | `\d`    | digits (0-9)
# | `\w`    | letters, digits, underscore
# | `\s`    | whitespace (space, tab, newline)
# | `.`     | any character except newline
# | `^`     | start of string
# | `$`     | end of string

import re

text = "I bought 3 apples, 4 oranges and 12 bananas."
numbers = re.findall(r"\d+", text)
print(numbers)
print()

text = "My phone numbers are 0712345678 and +254712345678."
phones = re.findall(r"(?:\+254|0)\d{9}", text)
print(phones)
print()

import re
text = "My Name Is Susan"
caps = re.findall(r"[A-Z]+", text)
print(caps)
