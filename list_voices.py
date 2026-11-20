# Vypise dostupne hlasy Google Text-to-Speech.
# Pouziti: python list_voices.py [jazyk]   napr. python list_voices.py en-US
#
# set GOOGLE_APPLICATION_CREDENTIALS=<cesta k service account json>

import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from google.cloud import texttospeech

language_code = sys.argv[1] if len(sys.argv) > 1 else 'cs-CZ'

client = texttospeech.TextToSpeechClient()
response = client.list_voices(language_code=language_code)

print(f'Hlasy pro {language_code}:\n')
for voice in sorted(response.voices, key=lambda v: v.name):
    gender = texttospeech.SsmlVoiceGender(voice.ssml_gender).name
    print(f'{voice.name:34} {gender:10} {voice.natural_sample_rate_hertz} Hz')

print(f'\nCelkem: {len(response.voices)}')
