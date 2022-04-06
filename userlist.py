import json
import os
import re
# 用户发言统计
dir_path = './doc'
out_path = './userlist'
files = os.listdir(dir_path)
for filename in files:
    userList = ''
    end = filename.find('.')
    with open(dir_path + '/' + filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        if line.startswith('####') and line[4] != '#':
            newLine = re.split(' |\n', line)
            userName = newLine[2]
            if userName not in userList:
                userList = userList + userName + '\n'
    with open(out_path + '/' + 'userlist' + filename[1:end] + '.txt', 'w', encoding='utf-8') as out:
        out.write(userList)