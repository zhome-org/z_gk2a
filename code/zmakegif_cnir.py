#import urllib.request #3+
# import urllib #2+
import time
from datetime import datetime
import imageio
import os
import sys
from PIL import Image
import getopt
import moviepy.editor as mp

def list_folder(src, target, f):
    af = []
    # print("list_folder", src, target, f)
    for item in os.listdir(src):
        itemsrc = os.path.join(src, item)
        # print(itemsrc, itemsrc.find(f)!=-1)
        if os.path.isdir(itemsrc):
            if itemsrc.find(target.replace("*",""))!=-1 and (itemsrc+"/").find(f)!=-1:
                af.append(itemsrc)
    return af

def seek_folder(src):
    af = []
    # print("seek_folder", src)
    if os.path.isfile(src):
        # print("isfile", src)
        # try:
        af.append(src)
        # except:
        #     pass
    elif os.path.isdir(src):
        # print("isdir", src)
        for item in os.listdir(src):
            itemsrc = os.path.join(src, item)
            af.extend(seek_folder(itemsrc))
        # try:
        #     af.append(src)
        # except:
        #     pass
    return af

def getshotimg(sdir, ofile, t, m="-1", w=800, h=800, f="_IR"):

    af = []
    if sdir.find("*")!=-1:
        ap = sdir.split("/")
        pp = ""
        for p in ap[:-1]:
            pp = pp + p + "/"
        print(pp)
        
        app = list_folder(pp, sdir, f)
        # return
        for p in app:
            af.extend(seek_folder(p))
    else:
        for p in sdir.split(","):
            af.extend(seek_folder(p))

    aaf = sorted(af)
    # print(sdir)

    outfilename = ofile 
    frames = []
    # print(af)
    from PIL import ImageFile
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    for filename in aaf:
        if m!="-1":
            if m.find(filename[-8:-6])==-1:
                continue
        print(">", filename, sdir, ofile, t, m, w, h)
        # im = imageio.imread(filename)
        im = Image.open(filename)
        #print(img)
        if os.path.getsize(filename) > 0:
            # im = Image.open ('C:/Users/XH/Pictures/test.jpg')
            im = im.resize((w, h), Image.ANTIALIAS)
            # im.save('C:/Users/XH/Pictures/thumbnailtest.jpg')  # 保存缩略
            frames.append(im)

    imageio.mimsave(outfilename, frames, 'GIF', duration = t)
    
    # os.remove(lockfile)
        
    # except Exception as e:
    #     print(e)
    #     try:
    #         os.remove(lockfile)
    #     except Exception as e:
    #         print(e)
        

if __name__ == '__main__':
    # if len(sys.argv) > 1:
    #     sdir = sys.argv[1]
    # else:
    #     sdir = "/mnt/d/gk2a_color/20220823_IR/"
    # getshotimg(sdir)

    # tday = time.strftime("%Y%m%d", time.localtime())
    tday = datetime.utcnow().strftime("%Y%m%d")
    sdir = "/mnt/d/gk2a_color/%s_CNIR/"%(tday)
    ofile = "/mnt/d/gk2a_video/%s_CNIR.gif"%(tday)
    #sdir = "z:/gk2a_color/%s_IR/"%(tday)
    #ofile = "z:/%s.gif"%(tday)
    t = 0.1
    m = "-1"
    w = 1600
    h = 1100
    f = "_CNIR"

    tday = datetime.utcnow().strftime("%Y%m%d")

    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv,"i:o:m:w:h:t:f:d:",["day=","help=","ifile=","ofile=","time=","minute=","width=","height="])
    except getopt.GetoptError:
        print('zmakegif.py -i <idir> -o <ofile> -t <stime>')
        sys.exit(2)

    for opt, arg in opts:
        # print(opt, opt in ("--help"))
        if opt == "--help":
            print('zmakegif.py, i:o:m:w:h:t:f:,["help=","ifile=","ofile=","time=","minute=","width=","height="]')
            sys.exit()
        elif opt in ("-i", "--idir"):
            sdir = arg
        elif opt in ("-o", "--ofile"):
            ofile = arg
        elif opt in ("-t", "--time"):
            t = arg
        elif opt in ("-m", "--minute"):
            m = arg
        elif opt in ("-w", "--width"):
            w = int(arg)
        elif opt in ("-h", "--height"):
            h = int(arg)
        elif opt in ("-f"):
            f = arg
        elif opt in ("-d"):
            tday = arg
         
    sdir = "/mnt/d/gk2a_color/%s_CNIR/"%(tday)
    ofile = "/mnt/d/gk2a_video/%s_CNIR.gif"%(tday)

    print(sdir, ofile, t, m, w, h, f)
    
    getshotimg(sdir, ofile, t, m, w, h, f)

    aifile = ofile.split(".")
    omp4file = f"{aifile[0]}.mp4"
    clip = mp.VideoFileClip(ofile)
    clip.write_videofile(omp4file)
    
    os.remove(ofile)
    print("gif to mp4>>", sdir, ofile, omp4file)
