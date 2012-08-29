route = './channel/'
init = '90052'
file = '.txt'

def get(id):
    print id
    filename = route + id + file
    f = open(filename, 'r')
    s = f.readline()
    i = s.find('nothing is ')
    if i != -1:
        nextid = s[i+11:]
        f.close()
        get(nextid)
    else:
        print s
        f.close()

get(init)
