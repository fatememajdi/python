import moviepy.editor
from tkinter.filedialog import *

video = moviepy.editor.VideoFileClip(askopenfilename())
audio = video.audio
audio.write_audiofile("test.mp3")
print('tamam :)')
