import glob
import random
import subprocess
from getfileinfo import getfileinfo

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
            if self.getfileinfo.vduration >=4 :
                randomstart=random.randrange(self.getfileinfo.vduration-3)
                randomlen=(random.choice([2,3,4]))
            else :
                randomstart=0
                randomlen=self.getfileinfo.vduration

            print("ffmpeg -i \""+i+"\" -ss "+str(randomstart)+" -t "+str(randomlen)+" -async 1 "+str(vcount)+".mp4")
            p = subprocess.Popen("ffmpeg -i \""+i+"\" -ss "+str(randomstart)+" -t "+str(randomlen)+" -async 1 "+str(vcount)+".mp4", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in p.stdout.readlines():
                print(line)