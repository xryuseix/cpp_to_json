import re
import os
f = open('./input.txt', 'r')
line = f.readline()

code = []
formated_code = []

while line:
    code.append(line)
    line = f.readline()
f.close()

    
for i in code:
    match_obj = re.search(r'[^ ]', i)
    formated_code.append('"' + "\\t"*(int)(match_obj.start()/4) + i[match_obj.start():-1].replace('"', '\\"') + '",')

for i in formated_code:
    print(i)


path = './output.txt'
os.remove(path)
for i in formated_code:
    with open(path, mode='a') as f:
        f.write(i + '\n')
