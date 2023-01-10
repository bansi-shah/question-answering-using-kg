f = open('mach_pich.txt', 'r')
contents = f.read()
f.close()

f = open('mach_pich.txt.format', 'w')
questions = contents.split('---------------------------QUESTION-------------------------')
for i, q in enumerate(questions):
	f.write(q.split('---------------------------ANSWER-------------------------')[0])

f.close()

import re

f = open('mach_pich.txt.format', 'r')
contents = f.read()

t = re.sub(r'\(.*\);', '', contents)
f.close()

f1 = open('mach_pich.txt.format.re', 'w')
f1.write(t)
f1.close()