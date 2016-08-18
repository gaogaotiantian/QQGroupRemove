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
files = os.listdir('./')

name_pat = re.compile(r"(gg|GG).")
badUsers = []
for user in users:
    possible_name = re.split("[-~_ ]+", user)
    for n in possible_name:
        has = 0
        for f in files:
            if n.strip().encode('utf-8') in f:
                has = 1
                break
        if has == 0:
            badUsers.append(user)
            break

print len(badUsers)

for user in badUsers:
    print user
