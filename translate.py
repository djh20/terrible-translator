import time
from googletrans import Translator
translator = Translator()

file = open("languages.txt", "r")
languages = file.read().split("\n")
file.close()

text = input("Input Text: ")
print("\n----------------------")
print("Translating...\n")
    
translation = text
for i in range(0, len(languages)):
    try:
        print("- Translating to " + languages[i] + " (" + str(i+1) + "/" + str(len(languages)) + ")")
        translation = translator.translate(translation, dest=languages[i])
        translation = translation.text
        print("- Translation output: " + translation + "\n")
    except:
        print("- Skipping " + languages[i])
        
translation = translator.translate(translation, dest='en')
print("\nOutput: " + translation.text)
print("----------------------\n")
time.sleep(1000)
