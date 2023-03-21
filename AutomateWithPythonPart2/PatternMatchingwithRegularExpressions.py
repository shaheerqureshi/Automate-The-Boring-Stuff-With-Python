#Creating Regex Objects

import re

phoneNumRegex =re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My Phone number is 123-456-0789')

print('Phone Number found:' + mo.group())
