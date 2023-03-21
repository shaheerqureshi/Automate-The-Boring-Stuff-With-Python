#Creating Regex Objects

import re

phoneNumRegex =re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My Phone number is 123-456-0789')

#print('Phone Number found:' + mo.group())

#Finding Area Code
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))
print(mo.group(2))

allGroups = mo.groups()
areaCode, phNum = allGroups
print(areaCode)

#Matching Multiple Groups with the Pipe

heroRgx = re.compile(r'Spiderman | Batman')
mo1 = heroRgx.search('Spiderman and Batman')
print(mo1.group())

#Optional Matching with the Question Mark

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())

mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
