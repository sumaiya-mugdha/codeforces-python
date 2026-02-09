guest=input()
host=input()
pile=input()
x= len(guest)
y= len(host)

if len(pile)!= x+y:
    print("NO")
    exit()
all_letter= guest+host
count= 0

for i in all_letter:
    if all_letter.count(i)!=pile.count(i):
        count=1
        break
if count==0:
    print("YES")
else:
    print("NO")