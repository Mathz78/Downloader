import requests
import eyed3
import os

i = 1

print("Welcome!! Here you can download some audios.")
print()

print("=============== Menu ===============")
print("1 - Download audio")
print("2 - Exit")
option = int(input("Enter the option: "))

while(option == 1):
    # Query the URL
    url = input("Enter the URL: ")
    request = requests.get(url, allow_redirects=True)

    # Download the file and name with value "audio.mp3"
    file_name = "audio.mp3"
    open(file_name, "wb").write(request.content)

    # Variable receive the information of the file.
    audiofile = eyed3.load("audio.mp3")

    # Variable receive the title of the file.
    file_name = audiofile.tag.title

    os.rename(r'audio.mp3',r'{} -  {}.mp3'.format(i, file_name))
    i = i + 1
    
    print("The file was successfully downloaded!!")
