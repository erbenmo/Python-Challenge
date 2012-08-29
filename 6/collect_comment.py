import sys
import zipfile

mem = []

route = './channel/'
init = '90052'
file = '.txt'

def get(id):
    mem.append(id+file)
    filename = route + id + file
    f = open(filename, 'r')
    s = f.readline()
    i = s.find('nothing is ')
    if i != -1:
        nextid = s[i+11:]
        f.close()
        get(nextid)
    else:
        f.close()

get(init)


clear = ''
zip = zipfile.ZipFile('channel.zip', 'r')
for name in mem:
    info = zip.getinfo(name)
    clear += info.comment

print clear
