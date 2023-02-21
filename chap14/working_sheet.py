import csv

# open the file
data = open('example.csv', encoding='utf-8')
# csv.render
csv_data = csv.reader(data)
# reformat it into a python object list of list
datalines = list(csv_data)

print(datalines[0])
print(len(datalines))
# 원하는 행 추출하기
for line in datalines[:5]:
    print(line)
# print single value
print(datalines[5][3])
all_emails = []
for line in datalines[1:15]:
    all_emails.append(line[3])
print(all_emails)

print(datalines[10])
full_names = []
for line in datalines[1:]:
    full_names.append(line[1]+' '+line[2])
# write csv file
# 오버라이드할 파일설정, write 모드, 새 라인을 빈 문자열로 지정
file_to_output = open('to_save_file.csv',mode='w',newline='')
# delimiter => 구분자 설정
csv_writer = csv.writer(file_to_output, delimiter=',')
# csv.writer은 csv.reader의 자매이다
csv_writer.writerow(['a','b','c'])
csv_writer.writerows([['1','2','3'],['4','5','6']])
# 파일 닫기
file_to_output.close()
# 오버라이딩 하지 않고 추가하기
f = open('to_save_file.csv', mode='a')
csv_writer = csv.writer(f)
csv_writer.writerow([1,2,3])
f.close()