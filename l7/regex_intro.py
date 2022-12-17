import re
search_string = "hello world"
pattern = "hello world"
match = re.match(pattern, search_string)
print(match)
if match:
    print("regex matches")
