import glob
import random
import subprocess
from getfileinfo import getfileinfo
import os

class subclip:
    vlistedit=[]
    vlist2 =""
    getfileinfo=getfileinfo()
    def getsubclip(self,vlist):
        vcount=0
        for i in vlist:
            print("Output vidoes : ",i)
            self.getfileinfo.getvideoinfo(i)
            vcount=vcount+1
            self.vlistedit.append(str(vcount)+".mp4")
            print(self.vlistedit)
            list1 ="-i "
            self.vlist2 = self.vlist2+list1+str(vcount)+".mp4 "
            print("vduration = ",self.getfileinfo.vduration)
            if self.getfileinfo.vduration >=3 :
                randomstart=random.randrange(self.getfileinfo.vduration-random.choice([2,3]))
                randomlen=(random.uniform(1, 3))
            else :
                randomstart=(random.uniform(0, 0.5))
                randomlen=self.getfileinfo.vduration

            print("ffmpeg -i \""+i+"\" -ss "+str(randomstart)+" -t "+str(randomlen)+" -async 1 "+str(vcount)+".mp4")
            p = subprocess.Popen("ffmpeg -i \""+i+"\" -ss "+str(randomstart)+" -t "+str(randomlen)+" -async 1 "+str(vcount)+".mp4", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in p.stdout.readlines():
                print(line)

        #fade in fade out
        print("ffmpeg -i 1.mp4 -y -vf fade=in:st=0:d=2 fade1.mp4")
        p = subprocess.Popen("ffmpeg -i 1.mp4 -y -vf fade=in:0:100 fade1.mp4", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
        os.remove("1.mp4")
        os.rename("fade1.mp4","1.mp4")
        print("ffmpeg -i "+self.vlistedit[-1]+" -y -vf fade=out:st=0:d=2 fade2.mp4")
        p = subprocess.Popen("ffmpeg -i "+self.vlistedit[-1]+" -y -vf fade=out:st=0:d=2 fade2.mp4", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)
        os.remove(self.vlistedit[-1])
        os.rename("fade2.mp4",self.vlistedit[-1])