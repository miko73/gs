# testit2.py

import os
import sys

APP_DIR = os.getcwd()
# Instantiates a client
# C:\Users\micha\Projects\google_speech\texts\asistenti_pedagoga_zaver.txt
theme_name = 'realisticky_stav_skolstvi'

file_name = 'C:\\Users\\micha\\Music\\prednes.txt'


file1 = open(file_name, encoding="utf8")

Lines = file1.readlines()

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
				Sentences.append("\n")
		except:
			print (f'len(world)>2 and world[-1] in Sent_Sep and x+2 < len(worlds) and worlds[x+1][0].isupper() failed with error [{world}]')

	with open('text_file.txt', "w", encoding="utf-8") as text_out:
		text_out.writelines(Sentences)
	# ==============================================================================



	# if len (temp_sent) > 1:
	# 	for sent in temp_sent:
	# 		Sentences.append(sent[0])
	# 		print (f'sent {sent}')
	# else:
	# 	if len(Sentences)>0:
	# 		Sentences[-1] += temp_sent[0]
	# 		print (f'Sentences[-1] {Sentences[-1]}')
	# 	else:
	# 		Sentences.append(temp_sent[0])
	# 		print (f'Sentences.add {temp_sent[0]}')

# for sent in Sentences:
# 	print (sent)
# print (f'act_sentence {act_sentence} === {Sentences[act_sentence]}')
Lines = ''

print (f'sys.getsizeof(Sentences) [{sys.getsizeof(Sentences)}] sys.getsizeof(Lines) [{sys.getsizeof(Lines)}]')

