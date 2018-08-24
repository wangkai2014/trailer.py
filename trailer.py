import glob
import random
import subprocess
import os
import datetime
import time
import os.path
from os import path

vlist=[]
vlistedit=[]
vcount=0
vlist2 =""
randomlen=0
randomstart=0
vduration=""
slow=""

#get list of videos
for name in glob.glob('*.mp4'):
	vlist.append(name)
print(vlist)
#select subclip
for i in vlist:
	print(i)
	vcount=vcount+1
	vlistedit.append(str(vcount)+".mp4")
	print(vlistedit)
	list1 ="-i "
	vlist2 = vlist2+list1+str(vcount)+".mp4 "
	"""
	#get video duration
	vl=""
    ffprobe=subprocess.check_output("ffprobe -i "+i+" -show_entries format=duration -v quiet -of csv=\"p=0\"")
    vl += str(ffprobe[0:2])
    vduration=(vl[2:4])
	"""
	randomstart=(random.choice([1,2]))
	randomlen=(random.choice([2,3,4]))
	print("ffmpeg -i \""+i+"\" -ss 00:00:0"+str(randomstart)+" -t 00:00:0"+str(randomlen)+" -async 1 "+str(vcount)+".mp4")
	p = subprocess.Popen("ffmpeg -i \""+i+"\" -ss 00:00:0"+str(randomstart)+" -t 00:00:0"+str(randomlen)+" -async 1 "+str(vcount)+".mp4", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in p.stdout.readlines():
		print(line),
	retval = p.wait()

#slomotion random
slowmo = input("Slowmotion trailer(y/n) ? : ")
if slowmo=="y" :
	for j in vlistedit:
	#slow=(random.choice(vlistedit))
		print("random slow."+j)
		print("ffmpeg -i "+j+" -filter_complex \"[0:v]setpts=2*PTS[v];[0:a]atempo=0.5[a]\" -map \"[v]\" -map \"[a]\" slow."+j+"")

		p = subprocess.Popen("ffmpeg -i "+j+" -filter_complex \"[0:v]setpts=2*PTS[v];[0:a]atempo=0.5[a]\" -map \"[v]\" -map \"[a]\" slow."+j+"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		for line in p.stdout.readlines():
			print(line),
		retval = p.wait()

		os.remove(j)
		os.rename("slow."+j,j)

#concatenate all video

vcount=0
cmdva=""
for i in vlist:
    list2 ="["+str(vcount)+":v] ["+str(vcount)+":a] "
    vcount=vcount+1
    cmdva = cmdva+list2

print("ffmpeg "+vlist2+"-filter_complex \""+cmdva+" concat=n="+str(vcount)+":v=1:a=1 [v] [a]\" -map \"[v]\" -map \"[a]\" concatenate.mp4")

p = subprocess.Popen("ffmpeg "+vlist2+"-filter_complex \""+cmdva+" concat=n="+str(vcount)+":v=1:a=1 [v] [a]\" -map \"[v]\" -map \"[a]\" concatenate.mp4", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
	print(line),
retval = p.wait()

#check outputtrailer.mp4 exists

if path.exists("outputtrailer.mp4"):
	os.rename("outputtrailer.mp4","outputtrailer"+str(time.time())+".mp4")
	print("outputtrailer.mp4 renamed to outputtrailer"+str(time.time())+".mp4")

#audio gain -12db

print("ffmpeg -i concatenate.mp4 -vcodec copy -af \"volume=-12dB\" trailer.mp4")

p = subprocess.Popen("ffmpeg -i concatenate.mp4 -vcodec copy -af \"volume=-12dB\" trailer.mp4", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
	print(line),
retval = p.wait()

#add background song

#get list of mp3
mp3list=[]
bsong=""
for name in glob.glob('*.mp3'):
	mp3list.append(name)
if not mp3list:
	bsong = input("Enter background song path(D:\\filename.mp3) : ")
else:
	bsong=mp3list[0]
print("Selected background song : "+bsong)

print("ffmpeg -i "+bsong+" -i trailer.mp4 -filter_complex \"[0:a][1:a]amerge,pan=stereo:c0<c0+c2:c1<c1+c3[out]\" -map 1:v -map \"[out]\" -c:v copy -shortest outputtrailer.mp4")

p = subprocess.Popen("ffmpeg -i "+bsong+" -i trailer.mp4 -filter_complex \"[0:a][1:a]amerge,pan=stereo|c0<c0+c2|c1<c1+c3[out]\" -map 1:v -map \"[out]\" -c:v copy -shortest outputtrailerwf.mp4", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
for line in p.stdout.readlines():
	print(line),
retval = p.wait()

#video filter
vfilter=""
vfilter = input("Apply video filter(y/n) ? : ")
if vfilter=="y" :

	print("ffmpeg -vf eq=brightness=0.01:contrast=0.9:saturation=1.5 1.mp4")

	p = subprocess.Popen("ffmpeg -i outputtrailerwf.mp4 -vf eq=brightness=0.01:contrast=0.9:saturation=1.5 outputtrailer.mp4", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in p.stdout.readlines():
		print(line),
	retval = p.wait()
else:
	os.rename("outputtrailerwf.mp4","outputtrailer.mp4")

# Delete tmp files
vcount=0
for i in vlist:
	vcount=vcount+1;
	os.remove(str(vcount)+".mp4")
	print(str(vcount)+".mp4 deleted")
os.remove("concatenate.mp4")
os.remove("trailer.mp4")
os.remove("outputtrailerwf.mp4")


#get video resolution
vh=""
ffprobe=""
ffprobe=subprocess.check_output("ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 outputtrailer.mp4")
vh += str(ffprobe)
print("Video resolution :"+vh[2:6])
print("Note: You need to have "+vh[2:6]+".png file in your current directory")
# Movie black bar
vfilter=""
vfilter = input("Get Movie black bar(y/n) ? : ")
if vfilter=="y" :
	p = subprocess.Popen("ffmpeg -i outputtrailer.mp4 -i "+vh[2:6]+".png -filter_complex \"[0:v][1:v] overlay=0:0:enable='between(t,0,60)'\" -pix_fmt yuv420p -c:a copy Movietrailer.mp4", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	for line in p.stdout.readlines():
		print(line),
	retval = p.wait()
	print("Output file Movietrailer.mp4")


#output
print("Output file outputtrailer.mp4")
print("Completed")