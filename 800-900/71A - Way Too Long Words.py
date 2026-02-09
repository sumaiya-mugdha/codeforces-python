n=int(input())
for i in range(n):
    word=input()
    if len(word)<=10:
        print(word)
    else:
        print(str(word[0])+str(len(word)-2)+str(word[len(word)-1]))