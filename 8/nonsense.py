import re, unicodedata

#input_bytes = '\x82s\x82\x88\x82\x89\x82\x93@\x82\x89\x82\x93@\x82@\x82\x93\x82\x88\x82\x89\x82\x86\x82\x94[\x82\x8a\x82\x89\x82\x93@\x82\x93\x82\x94\x82\x92\x82\x89\x82\x8e\x82\x87B'

input_bytes = '\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'

p_ascii = r'[\x00-\x7f]'
p_hw_katakana = r'[\xa1-\xdf]' # half-width Katakana
p_jis208 = r'[\x81-\x9f\xe0-\xef][\x40-\x7e\x80-\xfc]'
p_bad = r'.' # anything else

kinds = ['jis208', 'ascii', 'hwk', 'bad']

re_matcher = re.compile("(" + ")|(".join([p_jis208, p_ascii, p_hw_katakana, p_bad]) + ")")

for mobj in re_matcher.finditer(input_bytes):
    s = mobj.group()
    us = s.decode('shift-jis', 'replace')
    print ("%-6s %-9s %-10r U+%04X %s"
        % (kinds[mobj.lastindex - 1], mobj.span(), s, ord(us), unicodedata.name(us, '<no name>'))
        )
