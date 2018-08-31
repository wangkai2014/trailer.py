import glob
import random
import subprocess
import os
from pathlib import Path
import urllib.request
from getfileinfo import getfileinfo

class movieeffect:
    getfileinfo=getfileinfo()
    def filter(self):
        #slomotion random
        #video filter
        vfilter="y"
        #vfilter = input("Apply video filter(y/n) ? : ")
        if vfilter=="y" :

            print("ffmpeg -i fade.mp4 -vf eq=brightness=0.01:contrast=0.9:saturation=1.5 filter.mp4")

            p = subprocess.Popen("ffmpeg -i fade.mp4 -vf eq=brightness=0.01:contrast=0.9:saturation=1.5 filter.mp4", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in p.stdout.readlines():
                print(line),
        else:
            os.rename("fade.mp4","filter.mp4")
    
    def blackbar(self):
        # Movie black bar
        # Download input.png if not exsist
        my_file = Path("input.png")
        if my_file.exists():
            print("input.png found")
        else:
            print('downloading input.png')
            url = 'https://github.com/initedit-project/trailer.py/raw/master/input.png'  
            urllib.request.urlretrieve(url, 'input.png')
        
        vfilter="y"
        #vfilter = input("Get Movie black bar(y/n) ? : ")
        self.getfileinfo.getvideoinfo("filter.mp4")
        if vfilter=="y" :
            print("ffmpeg -i input.png -vf scale="+str(self.getfileinfo.w)+":"+str(self.getfileinfo.h)+" output.png")
            p = subprocess.Popen("ffmpeg -i input.png -vf scale="+str(self.getfileinfo.w)+":"+str(self.getfileinfo.h)+" output.png", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in p.stdout.readlines():
                print(line),
            print("ffmpeg -i filter.mp4 -i output.png -filter_complex \"[0:v][1:v] overlay=0:0:enable='between(t,0,"+str(self.getfileinfo.vduration+4)+")'\" -pix_fmt yuv420p -c:a copy Movietrailer.mp4")
            p = subprocess.Popen("ffmpeg -i filter.mp4 -i output.png -filter_complex \"[0:v][1:v] overlay=0:0:enable='between(t,0,"+str(self.getfileinfo.vduration+4)+")'\" -pix_fmt yuv420p -c:a copy Movietrailer.mp4", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in p.stdout.readlines():
                print(line),



