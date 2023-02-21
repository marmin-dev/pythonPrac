import shutil
import os
import re
# print(os.listdir())
# shutil.unpack_archive('example.zip','help','zip')

text = "my phone num is 010-4444-1111"
pattern = r'\d{3}-\d{4}-\d{4}'

phone = re.findall(pattern,text)
phone2 = re.finditer(pattern,text)
print(phone)
for phone1 in phone2:
    print(phone1)

phone3 = re.search(pattern,text)
print(phone3)

def search_phone(file, pattern=r'\d{3}-\d{4}-\d{4}'):
    f = open(file,'r')
    text = f.read()
    if re.search(pattern,text):
        return re.search(pattern,text)
    else:
        return ""

import os
# results = []
# for folder, sub_folders, files in os.walk(os.getcwd()):
#     for f in files:
#         full_path = folder+'/'+f
#         results.append(search_phone(full_path))
# for r in results:
#     if r != '':
#         print(r.group())