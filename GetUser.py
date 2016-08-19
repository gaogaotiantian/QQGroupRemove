# coding=utf-8
from bs4 import BeautifulSoup
import os
import re

def GetUsers(content):
    soup = BeautifulSoup(content.decode('utf-8', 'ignore'))
    usersRaw = soup.findAll('span', attrs={"class":"group-card"})
    users = [user.get_text().strip() for user in usersRaw]
    return users

content = open('test.html', 'r').read()
users = GetUsers(content)
filelist = open("filelist.txt", 'r').read().splitlines()
storeFile = open("PotentialRemove.txt", "w")

name_pat = re.compile(r"(gg|GG).")
badUsers = []
#users = [u"GG-荷兰/津-24-斜"]
for user in users:
    possible_name = re.split("[-~_ ]+", user)[-1]
    for f in filelist:
        if possible_name.strip().encode('utf-8') in f:
            has = 1
            break
    else:
        badUsers.append(user)

storeFile.write(str(len(badUsers))+'\n')

for user in badUsers:
    storeFile.write(user.encode('utf-8')+'\n')


