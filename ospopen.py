#!/usr/bin/python
import os
fd = "popen.txt"
file = open(fd, 'w')
file.write("HELLO")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)

#file = os.popen(fd, 'w')
#file.write("Hello")

