import glob, os
from PIL import Image
from math import sqrt

os.chdir("./MyImages")

path="C:/Users/kotso/PycharmProjects/MyImages/"
#save new photo here:
save_path=r"C:\Users\kotso\OneDrive\Υπολογιστής\CollagePhoto.png"

#Change picture size here
maxX=1920
maxY=1080


count=0
images=[]
open_images=[]

#read jpegs
for file in glob.glob("*.jpg"):
    count += 1
    images.append(file)

#read pngs
for file in glob.glob("*.jpeg"):
    count += 1
    images.append(file)

#read pngs
for file in glob.glob("*.png"):
    count += 1
    images.append(file)


sqr_count=sqrt(count)
if(sqr_count%1!=0):
    sqr_count=sqr_count/1-sqr_count%1

sizeX=int(maxX/sqr_count)
sizeY=int(maxY/sqr_count)

asymetrical_lines=count-(sqr_count*sqr_count)
sizeXasy=int(maxX/(sqr_count+1))


cur_line=1
for i in range(len(images)):
    if i%sqr_count==0 and i!=0:
        cur_line+=1
    #open image
    cur_path=path+str(images[i])
    open_images.append(Image.open(cur_path))
    #resize
    if cur_line>sqr_count-asymetrical_lines:
        open_images[i] = open_images[i].resize((sizeXasy, sizeY))
    else:
        open_images[i]=open_images[i].resize((sizeX,sizeY))


merged=Image.new('RGBA',(maxX,maxY),'black')

offsetX=0
offsetY=0

addX=sizeX
flag_last=False
cur_line=1
k=0
for i in range(len(open_images)):
    if i%sqr_count==0 and i!=0 and not(flag_last):
        offsetX=0
        offsetY+=sizeY
        cur_line+=1
    elif k%(sqr_count+1)==0 and flag_last:
        offsetX=0
        offsetY += sizeY

    if cur_line>sqr_count-asymetrical_lines:
        addX=sizeXasy
        flag_last=True

    if flag_last:
        k += 1

    merged.paste(open_images[i],(offsetX,offsetY))
    offsetX+=addX

merged.show()
merged.save(save_path)