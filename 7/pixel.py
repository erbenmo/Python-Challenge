import sys
import Image

im = Image.open('oxygen.png')
roi = im.crop((0, 43, 608, 52))
data = roi.load()
w,h = roi.size

print w, h

prev = -1
length = 0
for x in range(w):
    a,b,c,d = data[x,0]
    if prev != a:
#        print "length: " + str(length)
        length = 0
#        print "sym: " + str(prev)
#        sys.stdout.write('\n')
        sys.stdout.write(str(prev) + ' ')
        prev = a
    else:
        length += 1
print ''
