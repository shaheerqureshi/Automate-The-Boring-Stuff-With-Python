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

#phoneNumberExmple
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())
mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())

#Matching with Plus
batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwowowowoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batman')
mo3 == None
#The regex Bat(wo)+man will not match the string 'The Adventures of Batman' because
#at least one wo is required by the plus sign.

#GREEDY AND NON-GREEDY MATCHING
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())