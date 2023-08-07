# coding:utf8

import os
import sys
# import pyinotify
import time, datetime
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from skimage import io, exposure


sdir = "/mnt/d/gk2a_received/LRIT/"
ddir = "/mnt/d/gk2a_color/"

def MakeIrRsImage(filename):
    fpath = filename
    # time.sleep(1)
    # print(filename.find("_FD_"))
    
    if filename.find("_FD_")>0 and filename.find("ENHANCED") == -1:
        print("source:", filename)
        dt = filename[-19:-4]  # 20210722_223506
        
        t = "%s-%s-%s %s:%s:%s" % (dt[0:4], dt[4:6], dt[6:8], dt[9:11], dt[11:13], dt[13:]) + " UTC"
        b=(time.mktime(time.strptime(dt,"%Y%m%d_%H%M%S")))
        c=datetime.datetime.fromtimestamp(b)
        d = datetime.timedelta(hours=8)  # +8
        dt = c + d
        t1 = dt.strftime('%Y-%m-%d %H:%M:%S +8')
        
        fdir = ddir + filename[-19:-11] + "_CN"
        # print(fdir)
        if not os.path.exists(fdir):  #判断是否有目标目录如果没有则创建一个目标目录
            os.makedirs(fdir)
        # 中国
        fpath1 = fdir + "/" + filename[-19:]
        if not os.path.exists(fpath1):
            print("create file CN:", fpath1)
            #fcmd = '/home/pi/sanchez-v1.0.22-linux-arm/Sanchez reproject -s "' + fpath + '" -o "' + fpath1 + '" --lon 70:140 --lat 1:56'
            fcmd = '/home/zjk/tools/sanchez-v1.0.22-linux-x64/Sanchez reproject -s "' + fpath + '" -o "' + fpath1 + '" --lon 70:140 --lat 1:56'
            print(time.time(), fcmd)
            os.popen(fcmd).read().strip()
            # print(time.time())
            #设置所使用的字体
            font = ImageFont.truetype("DejaVuSans.ttf", 24)

            #打开图片
            im1 = Image.open(fpath1)
            
            #写字
            draw = ImageDraw.Draw(im1)
            draw.text((10, 10), t, (255, 0, 0), font=font)    #设置文字位置/内容/颜色/字体
            draw.text((10, 40), t1, (255, 0, 0), font=font)    #设置文字位置/内容/颜色/字体
            draw.text((10, 70), "GK2a satellite", (255, 0, 0), font=font)    #设置文字位置/内容/颜色/字体
            draw.text((10, 100), "By BH7EUE", (255, 0, 0), font=font)    #设置文字位置/内容/颜色/字体
            
            #另存图片
            im1.save(fpath1)
        
        # 圆盘
        fdir = ddir + filename[-19:-11] + "_FD"
        # print(fdir)
        if not os.path.exists(fdir):  #判断是否有目标目录如果没有则创建一个目标目录
            os.makedirs(fdir)
        fpath1 = fdir + "/" + filename[-19:]
        if not os.path.exists(fpath1):
            print("create file FD:", fpath1)
            #fcmd = '/home/pi/sanchez-v1.0.22-linux-arm/Sanchez -s "' + fpath + '" -o "' + fpath1 + '"'
            fcmd = '/home/zjk/tools/sanchez-v1.0.22-linux-x64/Sanchez -s "' + fpath + '" -o "' + fpath1 + '"'
            #print(time.time(), fcmd)
            os.popen(fcmd).read().strip()
            # print(time.time())
            #设置所使用的字体
            font = ImageFont.truetype("DejaVuSans.ttf", 48)

            #打开图片
            im1 = Image.open(fpath1)
            
            #写字
            draw = ImageDraw.Draw(im1)
            draw.text((10, 10), t, (255, 0, 0), font=font)    #设置文字位置/内容/颜色/字体
            draw.text((10, 60), t1, (255, 0, 0), font=font)    #设置文字位置/内容/颜色/字体
            draw.text((10, 110), "GK2a satellite", (255, 0, 0), font=font)    #设置文字位置/内容/颜色/字体
            draw.text((10, 160), "By BH7EUE", (255, 0, 0), font=font)    #设置文字位置/内容/颜色/字体
            
            #另存图片
            im1.save(fpath1)
            """
            img1 = Image.open(fpath1)
            img1 = img1.convert('RGBA')
            img2 = Image.open("Samsoverlay.gif")
            img2 = img2.convert('RGBA')
            r, g, b, alpha = img2.split()
            alpha = alpha.point(lambda i: i>0 and 204)
            im3 = Image.composite(img2, img1, alpha)

            #另存图片
            im3.save(fpath1.replace(".jpg", ".png"))
            """

        # IR图覆盖地图
        fdir = ddir + filename[-19:-11] + "_IR"
        # print(fdir)
        if not os.path.exists(fdir):  #判断是否有目标目录如果没有则创建一个目标目录
            os.makedirs(fdir)
        fpath1 = fdir + "/" + filename[-19:].replace(".jpg", ".png")
        
        if not os.path.exists(fpath1):
            print("create file2 IR:", fpath1)
            img1 = Image.open(fpath)
            img1 = img1.convert('RGBA')
            img2 = Image.open("/home/zjk/zhome/Samsoverlay.gif")
            img2 = img2.convert('RGBA')
            r, g, b, alpha = img2.split()
            alpha = alpha.point(lambda i: i>0 and 204)
            img = Image.composite(img2, img1, alpha)
            # img.show()
            img.save(fpath1)

            #设置所使用的字体
            font = ImageFont.truetype("DejaVuSans.ttf", 48)
            #打开图片
            im1 = img # Image.open(fpath1)
            #写字
            draw = ImageDraw.Draw(im1)
            draw.text((10, 10), t, (255, 0, 0), font=font)    #设置文字位置/内容/颜色/字体
            draw.text((10, 60), t1, (255, 0, 0), font=font)    #设置文字位置/内容/颜色/字体
            draw.text((10, 110), "GK2a satellite", (255, 0, 0), font=font)    #设置文字位置/内容/颜色/字体
            draw.text((10, 160), "By BH7EUE", (255, 0, 0), font=font)    #设置文字位置/内容/颜色/字体

            #另存图片
            im1.save(fpath1)
            
            # 图片调暗
            img= io.imread(fpath1)
            # io.imshow(img)
            gam1= exposure.adjust_gamma(img, 2)   #调暗
            #gam2= exposure.adjust_gamma(img, 0.5)  #调亮
            io.imsave(fpath1, gam1)
            #io.imsave('d:\\w2.png',gam2)

            # CNIR图覆盖地图
            fdir = ddir + filename[-19:-11] + "_CNIR"
            # print(fdir)
            if filename[-19:-11] != "":
                if not os.path.exists(fdir):  #判断是否有目标目录如果没有则创建一个目标目录
                    os.makedirs(fdir)
                fpath2 = fdir + "/" + filename[-19:].replace(".jpg", ".png")
                #print(fpath2, not os.path.exists(fpath2))
                if not os.path.exists(fpath2):
                    img=Image.open(fpath1)
                    img1 = img.crop((0,0,1600,1100))
                    img1.save(fpath2)


def seek_folder(src):
    af = []
    if os.path.isfile(src):
        try:
            af.append(src)
        except:
            pass
    elif os.path.isdir(src):
        for item in os.listdir(src):
            itemsrc = os.path.join(src, item)
            af.extend(seek_folder(itemsrc))
        # try:
        #     af.append(src)
        # except:
        #     pass
    return af


if __name__ == "__main__":
    filename_in = ""
    filename_out = ""
    if len(sys.argv) > 1:
        filename_in = sys.argv[1]
        filename_out = "out_" + filename_in
    if len(sys.argv) > 2:
        filename_out = sys.argv[2]

    aaf = []
    if filename_in != "":
        filename = filename_in
        if filename.find("_FD_")>0 and filename.find("ENHANCED") == -1:
        # if filename.find("_FD_")>0:
            fdir = ddir + filename[-19:-11] + "_CN"
            fpath1 = fdir + "/" + filename[-19:].replace(".jpg", ".png")
            if not os.path.exists(fpath1):
                aaf.append(filename)
                #print(filename)
            else:
                fdir = ddir + filename[-19:-11] + "_IR"
                fpath1 = fdir + "/" + filename[-19:].replace(".jpg", ".png")
                if not os.path.exists(fpath1):
                    aaf.append(filename)
                    #print(filename)
                else:
                    fdir = ddir + filename[-19:-11] + "_CNIR"
                    fpath1 = fdir + "/" + filename[-19:].replace(".jpg", ".png")
                    if not os.path.exists(fpath1):
                        aaf.append(filename)
                        #print(filename)
                        
        c1 = len(aaf)
        c2 = 0
        for filename in aaf:
            print(c1, c2, filename)
            MakeIrRsImage(filename)
            c2 = c2 + 1
                        
    else:
        af = seek_folder(sdir)
        
        for filename in af:
            # print(filename)
            if filename.find("_FD_")>0 and filename.find("ENHANCED") == -1:
            # if filename.find("_FD_")>0:
                fdir = ddir + filename[-19:-11] + "_CN"
                fpath1 = fdir + "/" + filename[-19:] # .replace(".jpg", ".png")
                if not os.path.exists(fpath1):
                    aaf.append(filename)
                    print(filename)
                else:
                    fdir = ddir + filename[-19:-11] + "_IR"
                    fpath1 = fdir + "/" + filename[-19:].replace(".jpg", ".png")
                    if not os.path.exists(fpath1):
                        aaf.append(filename)
                        print(filename)
                    else:
                        fdir = ddir + filename[-19:-11] + "_CNIR"
                        fpath1 = fdir + "/" + filename[-19:].replace(".jpg", ".png")
                        if not os.path.exists(fpath1):
                            aaf.append(filename)
                            print(filename)
        
        aaf1 = sorted(aaf, reverse=True)
        c1 = len(aaf1)
        c2 = 0
        for filename in aaf1:
            print(c1, c2, filename)
            MakeIrRsImage(filename)
            c2 = c2 + 1
