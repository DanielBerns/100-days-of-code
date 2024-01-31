# https://nanonets.com/blog/extract-text-from-pdf-file-using-python/

# importing required modules
from PyPDF2 import PdfReader
import textract



resource = "./recibo-noviembre.pdf"
# creating a pdf reader object
reader = PdfReader(resource)

# printing number of pages in pdf file
print(len(reader.pages))

# getting a specific page from the pdf file
page = reader.pages[0]

# extracting text from page
text_pypdf = page.extract_text()
print("-"*80)
print(text_pypdf)

text_textract = textract.process(resource)
print("-"*80)
print(str(text_textract))

from pydub import AudioSegment

resource = "/home/dberns/Code/github/Uberi/speech_recognition/examples/english.wav"
some_audio = AudioSegment.from_file(resource, format="wav")
audio_resource = "audio.mp3"
some_audio.export(audio_resource, format="mp3")
text_audio = textract.process(audio_resource)
print("-"*80)
print("audio to text")
print(str(text_audio))
