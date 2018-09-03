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
        vfilter = input("Get Movie black bar(y/n) ? : ")
        if vfilter=="y" :
            print("ffmpeg -i filter.mp4 -vf  drawbox=x=0:y=0:w=0:h=200:color=black:t=fill,drawbox=x=0:y=880:w=0:h=200:color=black:t=fill Movietrailer.mp4")
            p = subprocess.Popen("ffmpeg -i filter.mp4 -vf  drawbox=x=0:y=0:w=0:h=200:color=black:t=fill,drawbox=x=0:y=880:w=0:h=200:color=black:t=fill Movietrailer.mp4", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in p.stdout.readlines():
                print(line),
        else:
            os.rename("filter.mp4","Movietrailer.mp4")

    def nashville(self):
        #nashville
        print("adding nashville")
        p = subprocess.Popen("ffmpeg -i Movietrailer.mp4 -vf drawbox=x=0:y=0:w=1920:h=1080:color=blue@0.1:t=fill,drawbox=x=0:y=0:w=1920:h=1080:color=red@0.05:t=fill filter.mp4", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line),

