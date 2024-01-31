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

# https://alphacephei.com/vosk/install
# from pydub import AudioSegment
# import os
# import pdb
# 
# 
# opus_path = "/home/dberns/Info/mtt/chat-1/AUD-20230811-WA0003.opus"
# wav_path = "/home/dberns/Desktop/Code/github/DanielBerns/100-days-of-code/code/047/audio.wav"
# os.system(f'ffmpeg -i "{opus_path}" -vn "{wav_path}"')
# 
# some_audio = AudioSegment.from_file(wav_path, format="wav")
# audio_resource = "audio.mp3"
# pdb.set_trace()
# some_audio.export(audio_resource, format="mp3")
# text_audio = textract.process(audio_resource)
# print("-"*80)
# print("audio to text")
# print(str(text_audio))
