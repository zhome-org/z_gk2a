# z_gk2a
GK2a卫星云图后处理工具软件

## 优化云图
### code/zmakeirimage.py   
根据xrit-rx获取的最新卫星云图，利用Sanchez对图像按指定经纬度截取中国区的平面云图，生成全彩圆盘图，对IR图调整对比度和亮度，叠加文字等   
#### 示例  
##### 自动处理xrit-rx接收文件夹的所有FD文件，每个文件生成四张图IR,CNIR,FD,CN：
python3 zmakeirimage.py
##### 自动处理指定FD文件，生成四张图IR,CNIR,FD,CN：
python3 zmakeirimage.py /media/LRIT/20230814/FD/IMG_FD_044_IR105_20230814_072006.jpg

## 生成视频
### code/zmakegif.py   
对指定目录的图片生成GIF动画，并转换为Mp4格式视频   
#### 示例
##### 生成当天视频mp4
python3 zmakegif.py
##### 生成指定日期的视频
python3 zmakegif.py -d 20230814

## gif转mp4
### code/zgiftomp4.py   
gif动画转mp4视频   

## 依赖
- python3   
- Pillow   
- imageio   
- moviepy   
- Sanchez   


