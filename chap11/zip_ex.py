# # zip 파일 생성하기
# f = open('fileone.txt', 'w+')
# f.write('ONE FILE')
# f.close()
# f = open('filetwo.txt', 'w+')
# f.write('Two FILE')
# f.close()
# # 파이썬 내장 함수로 파일을 압축하기 위해 활용이 가능하며
# # zip파일을 만든 다음 개별 파일을 압축하여 zip 파일에 삽입할 수 있게 해준다
# import zipfile
# # zip file create
# comp_file = zipfile.ZipFile('comp_file.zip','w')
# # compress the txt file and write in zipfile
# comp_file.write('fileone.txt',compress_type=zipfile.ZIP_DEFLATED)
# comp_file.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)
# comp_file.close()
# # read
# zip_obj = zipfile.ZipFile('comp_file.zip','r')
# # extract all file from zip
# zip_obj.extractall('extracted_content')
import shutil
dir_to_zip = '/Users/marmin/pythonPrac/chap11/extracted_content'
output_filename = 'example'
# compress dir
shutil.make_archive(output_filename,'zip',dir_to_zip)
shutil.unpack_archive('example.zip','final_unzip','zip')