player=input()
x=0
for i in range(0,len(player)):
    if i + 6 < len(player) and player[i] == player[i + 1] == player[i + 2] == player[i + 3] == player[i + 4] == player[i + 5] == player[i + 6]:
        x=1

if x==1:
    print("YES")
else:
    print("NO")

