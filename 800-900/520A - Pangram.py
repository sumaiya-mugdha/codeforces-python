n=int(input())
word=input()
x=word.lower()
y=set(x)
if len(y)==26:
    print("YES")
else:
    print("NO")