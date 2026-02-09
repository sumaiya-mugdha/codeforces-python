s=input()
t=input()
if len(s)!=len(t):
    print("NO")
    exit()
x=s[::-1]

if x==t:
    print("YES")
else:
    print("NO")