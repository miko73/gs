# importing the library
#import pyperclip as pc
#import clipboard as pc

# text1 = "GeeksforGeeks"

from google.cloud import texttospeech


# copying text to clipboard
# pc.copy(text1)


# set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\KočandrleMichal\Projects\speech-test-300122-d4f7f5f35fc7.json

# import pyperclip as pc
from playsound3 import playsound
import os, sys

#from get_data import get_url_data

#from pdf_extractor import PDFExtractor, download_file
import pyperclip as pc


if len (sys.argv) > 1:
	file_base=sys.argv[1]
else:
	file_base='clipboard'


# Vyber hlasu. Seznam vsech dostupnych: python list_voices.py cs-CZ
# Chirp3-HD = nejnovejsi a nejprirozenejsi rada, Wavenet-B a Standard-B jsou starsi (obe zenske).
LANGUAGE_CODE = "cs-CZ"
VOICE_NAME = "cs-CZ-Chirp3-HD-Charon"   # muzsky; zensky napr. cs-CZ-Chirp3-HD-Kore

# Service account klic. Hleda se vedle exe (resp. vedle skriptu),
# pokud neni nastavena promenna GOOGLE_APPLICATION_CREDENTIALS.
CREDENTIALS_FILE = 'speech-test-300122-d4f7f5f35fc7.json'


def app_dir():
	"""Adresar s exe (pri behu z PyInstalleru), jinak adresar se skriptem."""
	if getattr(sys, 'frozen', False):
		return os.path.dirname(sys.executable)
	return os.path.dirname(os.path.abspath(__file__))


if not os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'):
	credentials_path = os.path.join(app_dir(), CREDENTIALS_FILE)
	if not os.path.exists(credentials_path):
		sys.exit(f'Chybi soubor s klicem: {credentials_path}\n'
		         f'Zkopiruj ho vedle exe, nebo nastav GOOGLE_APPLICATION_CREDENTIALS.')
	os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

client = texttospeech.TextToSpeechClient()

voice = texttospeech.VoiceSelectionParams(
    language_code=LANGUAGE_CODE, name=VOICE_NAME
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

APP_DIR = os.getcwd()
MUSIC_DIR = './'

# pasting the text from clipboard
line = pc.paste()
#line = "ahoj tady jsem"

# print(Lines)

Sentences = []
Sent_Sep=('.','?','!')
Sentences.append("")
act_sentence = 0

line = line.replace('    ', ' ')
line = line.replace('   ', ' ')
line = line.replace('  ', ' ')
# line = line.replace(' ', ' ')
# for tags in ('<li>','<ul>','<p>','<div>','<td>','<tr>','</li>','</ul>','</p>','</div>','</td>','</tr>'):
#     line = line.replace(tags, '')



worlds = line.split(" ")
# print(worlds)
for x, world in enumerate(worlds):
	print (f'world [{world}]')
	Sentences[act_sentence] += f' {world}'
	try:
		if len(world)>2 and world[-1] in Sent_Sep and x+2 < len(worlds) and worlds[x+1][0].isupper():
			print (f'act_sentence {act_sentence} === {Sentences[act_sentence]}')
			act_sentence += 1
			Sentences.append("")
	except:
		print (f'len(world)>2 and world[-1] in Sent_Sep and x+2 < len(worlds) and worlds[x+1][0].isupper() failed with error [{world}]')

audio_file_name = os.path.join(MUSIC_DIR, f'{file_base}.mp3')


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
print (audio_file_name)
playsound(audio_file_name)
