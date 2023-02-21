# 다른 디렉토리나 컴퓨터에서 실행시 결과가 다를 수 있다

f = open('practice.txt','w+')
f.write("This is a test string")
f.close()

import os

print(os.getcwd())
print(os.listdir())

import shutil
filepath = '/Users/marmin/pythonPrac/chap10/practice.txt'
for folder, sub_folders, files in os.walk(filepath):
    print(f"currently looking at {folder}")
    print('\n')
    print('The subfolders are: ')
    for sub_fold in sub_folders:
        print(f'subfolder: {sub_fold}')
    print('\n')
    print('the files are: ')
    for f in files:
        print(f'files:{f}')
    print("\n")