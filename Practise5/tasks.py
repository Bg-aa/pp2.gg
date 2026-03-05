#ex1:
import re 
s = input()
if re.fullmatch(r"ab*", s):
    print("Match")
else:
    print("No match")

#ex2:
import re
s = input()
if re.fullmatch(r"ab{2,3}", s):
    print("Match")
else:
    print("No match") 

#ex3:
import re
s = input()
ans = re.findall(r"[a-z]+_[a-z]+", s)
print(ans)

#ex4:
import re
s = input()
ans = re.findall(r"[A-Z][a-z]+", s)
print(ans) 

#ex5:
import re
s = input()
if re.fullmatch(r"a.*b", s):
    print("Match")
else:
    print("No match")

#ex6:
import re
s = input()
ans = re.sub(r"[ , .]" ":", s)
print(ans)

#ex7:
import re
s = input()
ans = re.sub(r"_([a-z])", lambda x: x.group(1).upper(), s)
print(ans)

#ex8:
import re
s = input()
ans = re.findall(r"[A-Z][a-z]*", s)
print(ans)

#ex9:
import re
s = input()
ans = re.sub(r"([A-Z])", r" \1", s)
print(ans.strip())  

#ex10:
import re
s = input()
ans = re.sub(r"([A-Z])", r"_\1", s).lower().lstrip("_")
print(ans) 
