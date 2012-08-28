def main():
    f = open('source', 'r')

    hash = {}

    str = f.readlines()
    for s in str:
        for c in s:
            if c == '\n':
                continue
            if c in hash:
                hash[c]+=1
            else:
                hash[c]=1

    clean = ''
    for s in str:
        for c in s:
            if c == '\n':
                continue
            if hash[c] == 1:
                clean += c

    print clean

if __name__ == "__main__":
    main()
