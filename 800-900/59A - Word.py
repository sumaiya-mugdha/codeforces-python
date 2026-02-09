s=input()
count=0
count2=0
for i in range(len(s)):
    if s[i].isupper():
        count+=1
    else:
        count2+=1
if count> count2:
    print(s.upper())
else:
    print(s.lower())