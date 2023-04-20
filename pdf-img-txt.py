import pytesseract
from pdf2image import convert_from_path
import openai



# Defina o caminho do seu arquivo PDF e o caminho onde deseja salvar o arquivo TXT
pdf_path = 'associacao.pdf'
txt_path = 'associacao-txt.txt'

# Converta o arquivo PDF em uma lista de imagens
images = convert_from_path(pdf_path)

# Inicialize o conteúdo do arquivo TXT como uma string vazia
txt_content = ''

# Extraia o texto de cada imagem e adicione-o ao conteúdo do arquivo TXT
for i, image in enumerate(images):
    text = pytesseract.image_to_string(image, lang='por')
    txt_content += f'--- Página {i+1} ---\n{text}\n\n'

# Salve o conteúdo extraído em um arquivo TXT
with open(txt_path, 'w', encoding='utf-8') as file:
    file.write(txt_content)


openai.api_key = "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"

arquivo = open('cvale-txt.txt')

response = openai.Completion.create(
    model="text-davinci-003",
    prompt= f'{arquivo} extraia alguns valores desse arquivo',
    max_tokens=1000
    )
print(response)