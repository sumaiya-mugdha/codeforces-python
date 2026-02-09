s=input()
s1=s.lower()
for i in range(len(s1)):
    if s1[i]=='a' or s1[i]=='e' or s1[i]=='i' or s1[i]=='o' or s1[i]=='u' or s1[i]=='A' or s1[i]=='y':
        continue
    else:
        print("."+str(s1[i]),end="")
