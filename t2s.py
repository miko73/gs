# python t2s.py

"""Synthesizes speech from the input string of text or ssml.

Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
from google.cloud import texttospeech
# set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\micha\Projects\google_speech\speech-test-300122-d4f7f5f35fc7.json
import pyperclip as pc

from playsound import playsound
import os

from get_data import get_url_data

from pdf_extractor import PDFExtractor, download_file

encodings = ['utf-8', 'windows-1250', 'windows-1252'] # add more


client = texttospeech.TextToSpeechClient()

voice = texttospeech.VoiceSelectionParams(
    language_code="cs-CZ", ssml_gender=texttospeech.SsmlVoiceGender.SSML_VOICE_GENDER_UNSPECIFIED
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)



APP_DIR = os.getcwd()
MUSIC_DIR = 'C:\\Users\\micha\\Music'
# Instantiates a client
# C:\Users\micha\Projects\google_speech\texts\asistenti_pedagoga_zaver.txt
# file:///C:/Users/micha/Documents/politika/priloha_859075864_0_Podn%C4%9Bty%20ob%C4%8Dan%C5%AF%20-%20ZM%C4%8C%2010-11-20%20-%20Ko%C4%8Dandrle.pdf





 # =========== get data from pdf on web  ===========
# url = "http://www.realisticky.cz/clanky/prilohy/skolstvi/Stav_skolstvi_v_cechach_2008.pdf"
# url = "https://www.clovekvtisni.cz/media/publications/1595/file/vyzkum_ap_2020.pdf"
# print(f'url {url}')
# # Downloading file locally
# APP_DIR = os.getcwd()
# downloaded_file = download_file(url, APP_DIR)
# print(downloaded_file)
# =========== get data from pdf on web  =======================


# ======================= data directly from file on FS ============================
# APP_DIR = os.getcwd()

# downloaded_file= 'C:\\Users\\micha\\Documents\\politika\\interpelace\\26_01_2021.pdf'
downloaded_file= 'C:\\C\\prednes.pdf'
# downloaded_file= 'C:\\C\\kvalita.pdf'
print(downloaded_file)

# # ======================= data directly from file on FS ============================

# creating the instance of class
pdf_extractor = PDFExtractor(APP_DIR)

# Getting desired data out
# pdf_extractor.read_pages(downloaded_file)
t_pdf_file_name = pdf_extractor.read_pages(downloaded_file)
# t_pdf_file_name = pdf_extractor.read_pages(downloaded_file, 1, 2)

# ======================== text file only =====================================
# downloaded_file = 'C:\Users\micha\Documents\politika\interpelace\\26_01_2021.pdf'
# t_pdf_file_name = downloaded_file
# ======================== text file only =====================================


location = os.path.dirname(downloaded_file)  #path only
file_name = os.path.basename(downloaded_file)  #file_name
file_base=file_name.split('.')[0]
ext = file_name.split('.')[1]
print (f'file name [{file_base}], extension [{ext}]')

# # =========== t_pdf_file_name is the source text file for mp3 convertion ===========

print (f'file_name from pdf_extractor {t_pdf_file_name}')

text_file_name = f'{MUSIC_DIR}\\{file_base}.txt'

with open(t_pdf_file_name, 'rb') as f, open(text_file_name, 'wb') as g:
    while True:
        block = f.read(16*1024*1024)  # work by blocks of 16 MB
        if not block:  # end of file
            break
        g.write(block)




rawdata = open(t_pdf_file_name, "rb").read()
import chardet
result = chardet.detect(rawdata)
encoding_str = result['encoding']

file1 = open(t_pdf_file_name, encoding=encoding_str)
Lines = file1.readlines()


# # =========== END t_pdf_file_name is the source text file for mp3 convertion ===========



# clipboard.copy("this text is now in the clipboard")
# print clipboard.paste()



 # =========== get data from html  ===========
# Lines=[]
# for data in get_url_data('https://denikn.cz/534236/politikon-ctyri-klicova-poznani-o-piratech-a-starostech-a-proc-je-pro-babise-landa-vic-nez-ockovani/?ref=tit', 'utf8'):
# 	for d in data:
# 		Lines.append(d)
# theme_name = 'dennik_N'
# file_name = f'{APP_DIR}\\texts\\{theme_name}.txt'
# # # ===============================================
# downloaded_file = file_name
# location = os.path.dirname(downloaded_file)  #path only
# file_name = os.path.basename(downloaded_file)  #file_name
# file_base=file_name.split('.')[0]
# ext=file_name.split('.')[1]
# print (f'file name [{file_base}], extension [{ext}]')

# # =============== get data from html  =================

print (f'Lines - {Lines}')


Sentences = []
Sent_Sep=('.','?','!')
Sentences.append("")
act_sentence = 0


for line in Lines:
	line=line [:-2]
	line = line.replace('    ', ' ')
	line = line.replace('   ', ' ')
	line = line.replace('  ', ' ')
	worlds = line.split(" ")
	# print(worlds)
	for x, world in enumerate(worlds):
		# print (world)
		Sentences[act_sentence] += f' {world}'
		try:
			if len(world)>2 and world[-1] in Sent_Sep and x+2 < len(worlds) and worlds[x+1][0].isupper():
				print (f'act_sentence {act_sentence} === {Sentences[act_sentence]}')
				act_sentence += 1
				Sentences.append("")
		except:
			print (f'len(world)>2 and world[-1] in Sent_Sep and x+2 < len(worlds) and worlds[x+1][0].isupper() failed with error [{world}]')

audio_file_name = f'{MUSIC_DIR}\\{file_base}.mp3'

# with open(text_file_name, "w") as text_out:
	# text_out.writelines(Sentences)


with open(audio_file_name, "wb") as out:
# Strips the newline character
	for line in Sentences:
		print("Line: {}".format(line.strip()))
		synthesis_input = texttospeech.SynthesisInput(text=line)

		# Perform the text-to-speech request on the text input with the selected
		# voice parameters and audio file type
		response = client.synthesize_speech(
		    input=synthesis_input, voice=voice, audio_config=audio_config
		)
		out.write(response.audio_content)





# with open(file_name, encoding="utf8") as fp:
#     content = fp.read()

# Set the text input to be synthesized
# chunk_size = 4999
# start=0
# end=chunk_size
# print (f'len(content) [{len(content)}]')
# while end != len(content):
# 	read_sequence = content[start:end]
# 	print(f'[start:end] [{start}:{end}]')
# 	synthesis_input = texttospeech.SynthesisInput(text=read_sequence)
# 	print (read_sequence)
# 	start = end
# 	end += min(len(content) - start, chunk_size)
# 	print (f'end {end}')



# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
# class SsmlVoiceGender(proto.Enum):
#     r"""Gender of the voice as described in `SSML voice
#     element <https://www.w3.org/TR/speech-synthesis11/#edef_voice>`__.
#     """
#     SSML_VOICE_GENDER_UNSPECIFIED = 0
#     MALE = 1
#     FEMALE = 2
#     NEUTRAL = 3


# class AudioEncoding(proto.Enum):
#     r"""Configuration to set up audio encoder. The encoding
#     determines the output audio format that we'd like.
#     """
#     AUDIO_ENCODING_UNSPECIFIED = 0
#     LINEAR16 = 1
#     MP3 = 2
#     MP3_64_KBPS = 4
#     OGG_OPUS = 3
#     MULAW = 5



# The response's audio_content is binary.
# audio_file_name = f'{APP_DIR}\\texts\\skolstvi_norsko.mp3'
# with open(audio_file_name, "wb") as out:
    # Write the response to the output file.
    # out.write(response.audio_content)

print(f'Audio content written to file {audio_file_name}')
# playsound(audio_file_name)
