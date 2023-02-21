import PyPDF2

f = open('Working_Business_Proposal.pdf','rb')

pdf_text = []

pdf_reader = PyPDF2.PdfReader(f)

for num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[num]
    pdf_text.append(page.extract_text())
print(pdf_text)