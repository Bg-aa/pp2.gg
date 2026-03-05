import re

email = "test@gmail.com"

pattern = r"\w+@\w+\.\w+"

if re.match(pattern, email):
    print("It's an email")