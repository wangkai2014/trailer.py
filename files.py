import glob
import subprocess

class files:
    def getfiles(self):
        vlist=[]
        for name in glob.glob('*.MP4'):
	        vlist.append(name)
        for name in glob.glob('*.AVI'):
	        vlist.append(name)
        for name in glob.glob('*.MKV'):
	        vlist.append(name)
        for name in glob.glob('*.MOV'):
	        vlist.append(name)
        for name in glob.glob('*.3GP'):
	        vlist.append(name)
        print("Selected Videos :",vlist)
        return vlist