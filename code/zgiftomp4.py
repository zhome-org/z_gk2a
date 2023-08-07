#import urllib.request #3+
# import urllib #2+
import time
import imageio
import os
import sys
from PIL import Image
import getopt
import moviepy.editor as mp



if __name__ == '__main__':
    if len(sys.argv) > 1:
        ifile = sys.argv[1]
    else:
        ifile = ""

    if len(sys.argv) > 2:
        ofile = sys.argv[2]
    else:
        aifile = ifile.split(".")
        ofile = f"{aifile[0]}.mp4"
    
    if ifile != "":
        clip = mp.VideoFileClip(ifile)
        clip.write_videofile(ofile)
        print("gif to mp4>>", ifile, ofile)
    else:
        print("error input file.")
