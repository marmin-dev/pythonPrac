import PyPDF2

# open file
f = open('Working_Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfReader(f)
# get pdf pages
print(len(pdf_reader.pages))
# get page content
page_one = pdf_reader.pages[0]
# extract text from content
page_one_text = page_one.extract_text()
# 빈 문자열이 출력된다면 다른 라이브러리를 사용하자
print(page_one_text)
# 프로그래밍 방식으로 새 파일에 쓸 수 있다
# 이를 수행하기 위해 pdf writer 객체를 생성한다

pdf_writer = PyPDF2.PdfWriter()
# 특수한 type 이어야한다. 원래의 파이썬 문자열이 아니다
pdf_writer.add_page(page_one)
pdf_output = open('Some_BrandNew_Doc.pdf',"wb")
pdf_writer.write(pdf_output)

f.close()
pdf_output.close()
