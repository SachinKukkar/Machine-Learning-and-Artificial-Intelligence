f = open("poems.txt")

c=f.read()
if("twinkle" in c ):
    print("twinkle is present in poems.txt")
else:
    print("Not found !")    

f.close()
