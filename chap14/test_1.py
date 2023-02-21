import csv
import re
import PyPDF2
# 1
f = open('Exercise_Files/find_the_link.csv' , encoding='utf-8')
csv_data = csv.reader(f)
datalines = list(csv_data)

# print(datalines)
chars = []

for data in datalines:
    for letter in data:
        if re.match(r'\D',letter):
            chars.append(letter)

print("".join(chars))
f.close()

# 2
f = open('Exercise_Files/Find_the_Phone_Number.pdf','rb')
pdf_text = []
pdf_reader = PyPDF2.PdfReader(f)

for num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[num]
    pdf_text.append(page.extract_text())

pdf_str="".join(pdf_text)
for match in re.finditer(r'\d\d\d+',pdf_str):
    print(match)
print(pdf_str[42905:42917])
