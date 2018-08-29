import glob
import random
import subprocess
import os
import datetime
import time
import os.path
from os import path
import shlex
import json
from files import files
from subclip import subclip
from slowmo import slowmo
from concatenate import concatenate
from audio import audio
from movieeffect import movieeffect
from deletefiles import deletefiles

vlist=[]
vlistedit=[]
vcount=0
vlist2 =""
randomlen=0
randomstart=0
vduration=""
slow=""

#get list of videos
vlist=files().getfiles()

#select subclip
subclip=subclip()
subclip.getsubclip(vlist)

#slomotion random
slowmo=slowmo()
slowmo.getslowmo(subclip.vlistedit)

#concatenate all video
concatenate=concatenate()
concatenate.getconcatenate(subclip.vlistedit,subclip.vlist2)

#audio
audio=audio()
audio.audiogain()
audio.addaudio()
audio.fade()

#movieeffect
movieeffect=movieeffect()
movieeffect.filter()
movieeffect.blackbar()



# Delete tmp files
deletefiles=deletefiles()
deletefiles.getdeletefiles(vlist)

#output
print("Output file Movietrailer.mp4")
print("Completed")
input("Press any key to exit")
