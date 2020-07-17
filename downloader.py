import requests
import eyed3
import os

i = 1

print("Bem vindo!! Aqui você pode baixar áudios.")
print()

print("=============== Menu ===============")
print("1 - Baixar áudio")
print("2 - Sair")
opcao = int(input("Informe a opção: "))

while(opcao == 1):
    # Consultar URL
    url = input("Informe a URL: ")
    request = requests.get(url, allow_redirects=True)

    # Baixar o arquivo e nomear com o valor "1"
    file_name = "arquivo.mp3"
    open(file_name, "wb").write(request.content)

    # Variável para receber o titulo do arquivo
    audiofile = eyed3.load("arquivo.mp3")

    # Variavel recebendo o nome do arquivo.
    file_name = audiofile.tag.title

    os.rename(r'arquivo.mp3',r'{} -  {}.mp3'.format(i, file_name))
    i = i + 1