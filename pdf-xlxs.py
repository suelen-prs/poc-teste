import PyPDF2
import openpyxl
import re

# Abrir o arquivo PDF
pdf_file = open('Associação 19-20[4061].pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Criar um arquivo Excel
workbook = openpyxl.Workbook()
sheet = workbook.active

# Loop através das páginas do PDF
for page_num in range(len(pdf_reader.pages)):
    page = pdf_reader.pages[page_num]
    text = page.extract_text()
    print(text)
    
    # Separar o texto por linhas
    lines = text.split('\n')
    
    # Escrever cada linha em uma linha separada no arquivo Excel
    for i, line in enumerate(lines):
        sheet.cell(row=i+1, column=page_num+1).value = line

# Salvar o arquivo Excel
workbook.save('Associação 19-20[4061].xlsx')