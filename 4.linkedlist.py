#-*- coding: utf-8 -*-
__author__ = "tongzhengyu"

# http://www.pythonchallenge.com/pc/def/linkedlist.php

import re
from urllib.request import urlopen

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345'
# and the next nothing is 44827
pattern = "and the next nothing is (\d+)"
# Yes. Divide by two and keep going.
patternDivide = "Divide by two"
n = "0"
for i in range(400):
    print('round ', i)
    with urlopen(url) as response:
        for line in response:
            lineContent = line.decode('utf-8')
            print(lineContent)
            matches = re.search(pattern, lineContent)
            if matches != None:
                n = matches.groups()[0]
                print(n)
                url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + n
                print(url)
                break

            matches = re.search(patternDivide, lineContent)
            if matches != None:
                m = eval(n) / 2
                n = str(m)
                print(n)
                url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + n
                print(url)
                break
        else:
            print("???")
    
end='peak.html'