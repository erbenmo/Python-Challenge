f = open('source', 'r')
str = f.readlines()

for s in str:
    for i in range(len(s)):
        if i<=2 or i>=(len(s)-3):
            continue
        if s[i].isupper():
            continue
        if (not (s[i-3].isupper() and s[i-2].isupper() and s[i-1].isupper())):
            continue
        if (not (s[i+3].isupper() and s[i+2].isupper() and s[i+1].isupper())):
            continue
        
        # check left
        if (not (i==3)) and s[i-4].isupper():
            continue

        # check right
        if (not (i==(len(s)-4))) and s[i+4].isupper():
            continue

        print s[i]
