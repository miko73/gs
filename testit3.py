import os
path_str = "c:\\var\www\index.html"
print(os.path.basename(path_str))

import os
path_str = "c:\\home\some_str\last_str\\"
split_path = path_str.rsplit("\\",1)
print(os.path.basename(split_path[0]))


path_str = "c:\\var\www\index.html"
filename = path_str.split(os.sep)[-1]
print (filename)
file=filename.split('.')[0]
ext=filename.split('.')[1]
print (f'file name [{file}], extension [{ext}]')



line = '<p>občanské společnosti.</li></ul></p></div></td></tr>  '


line=line [:-2]
# line = line.replace('    ', ' ')
# print (line)
# line = line.replace('   ', ' ')
# print (line)
# line = line.replace('  ', ' ')
# print (line)
# line = line.replace('', ' ')
for tags in ('<li>','<ul>','<p>','<div>','<td>','<tr>','</li>','</ul>','</p>','</div>','</td>','</tr>'):
    line = line.replace(tags, '')

print(line)
# worlds = line.split(" ")
# print(worlds)
