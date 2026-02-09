#228A - Is your horseshoe on the other hoof?
s1,s2,s3,s4=map(int,input().split())
colour={s1,s2,s3,s4}
if len(colour)==4:
    print("0")
elif len(colour)==3:
    print("1")
elif len(colour)==2:
    print("2")
else:
    print("3")




