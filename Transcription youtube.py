from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter

import os

ytlink = input('YT id:')
#yt id is what after https:// www.youtube.com/watch?v= 

lang = input('language:')


Transcriptions = YouTubeTranscriptApi.get_transcript(ytlink, languages=[lang])

#formatter in order to read easily the file 
formatter = TextFormatter()
text_formatted = formatter.format_transcript(Transcriptions)


print(text_formatted)

#use of os module in order to create and write a file with this transcription 
path = R'C:\Users\Asus\Documents\Transcriptions'
file = input('name of the file:')
with open(os.path.join(path, file), 'w', encoding='utf-8') as text_file:
    text_file.write(str(text_formatted))