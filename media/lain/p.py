import os

dirList = os.listdir()

result = ''

for i in dirList:
    if str(i).split('.')[1] in ['webm', 'mp4']:
        result += f'<video src="media/lain/{str(i)}" autoplay muted loop></video>\n'
        print(f'{str(i)} is a video')
    else:
        result += f'<div class="imgblock"><img src="media/lain/{str(i)}" alt=""></div>\n'

input()
print(result)
