import pytesseract as pyt
from gtts import gTTS
from playsound import playsound
from googletrans import Translator
from PIL import Image
from tkinter.filedialog import askopenfilename
def lang_convert_from_input():
    files=askopenfilename()
    img=Image.open(files)
    txt=pyt.image_to_string(img)
    translator=Translator()
    translate=translator.translate(txt,dest='ml')
    txt=translate.text
    ts=gTTS(txt,lang="en")
    ts.save("voice.mp3")
    playsound("voice.mp3")
    print(txt)
lang_convert_from_input()  