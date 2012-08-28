import urllib2

init = "8022"
base = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

def getPage(nothing):
    req = urllib2.Request(base + nothing)
#    print base + init
    response = urllib2.urlopen(req)
    text = response.read()
    i = text.find("nothing is ")
    next_nothing = text[i+11:]
    print text
    getPage(next_nothing)
    
getPage(init)
