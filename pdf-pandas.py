import PyPDF2
import pandas as pd

# abre o arquivo PDF e cria um objeto PdfFileReader
pdf_file = open('balanco.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# lista para armazenar as informações extraídas
data = []

# loop pelas páginas do PDF
for page_num in range(len(pdf_reader.pages)):
    # extrai o texto da página
    page = pdf_reader.pages[page_num]
    text = page.extract_text()

    # separa as informações por espaços e cria um dicionário com as informações
    info = {}
    lines = text.split('\n')
    for line in lines:
        parts = line.split()
        if len(parts) >= 1:
            key = ' '.join(parts[:-1])
            value = parts[-1]
            info[key] = value

    # adiciona as informações à lista
    data.append(info)

# cria um DataFrame a partir dos dados extraídos
df = pd.DataFrame(data)

# exporta o DataFrame para um arquivo XLSX
df.to_excel('dados.xlsx', index=False)