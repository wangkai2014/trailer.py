import os
import glob
class deletefiles:

    def getdeletefiles(self,vlist):
        # Delete tmp files
        print("Deleting tmp files...")
        vcount=0
        for i in vlist:
            vcount=vcount+1
            os.remove(str(vcount)+".mp4")
        os.remove("concatenate.mp4")
        os.remove("audiogain.mp4")
        os.remove("addaudio.mp4")
        os.remove("fade.mp4")
        os.remove("filter.mp4")
        os.remove("output.png")
        print("Delete all .mp4.tmp files")
        list(map(os.remove , glob.glob('*.mp4.tmp')))
        print("Deleted tmp files...")