import PyPDF2
import csv

# Abra o arquivo PDF
with open('balanco.pdf', mode='rb') as file:
    reader = PyPDF2.PdfReader(file)

    # Extraia o texto de todas as páginas do PDF
    text = ''
    for i in range(len(reader.pages)):
        text += reader.pages[i].extract_text()

    # Divida o texto em linhas
    lines = text.split('\n')

    # Escreva as linhas em um arquivo CSV
    with open('balanco.csv', mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in lines:
            writer.writerow([line])