#I wiil be using the OS Module for this project, the PIL : Python Imaging Library
#PIL is the image processing package for python
#it includes light weight image processing tools that aids in editing creating and saving images

import ot
from PIL import Image

def watermark_picture(input_image_path, water_mark_image_path, Output_image_path):
    Real_image = Image.open(r'\Users\Mnesoma\Desktop\GITPUSH\images\laptop4.jpg')
    Watermark = Image.open(r'\Users\Mnesoma\Desktop\GITPUSH\watermarker\data 1.jpg').convert("RGBA")
    #The open() and convert() methods came along with the PIL. open helps to open the image  while 
    #convert helps to get the color mode of the image. I chose a color with transparency mask RGBA

    #lETS ADD WATERMARK TO THE IMAGE
    position = Real_image.size #this gets the size of the image and returns (width,height)
    newsize = (int(position[0]*8/100),int(position[0]*8/100)) #newsize will take a square shape as width$height are equal
    
    #adjusting watermark size to be the same with the new size of image
    Watermark = Watermark.resize(newsize)

    #This is the new position of the image
    new_position = position[0]-newsize[0]-20, position[1]-newsize[1]-20

    #I just ceated a transparent image
    transparent = Image.new(mode= 'RGBA', size = position, color=(0,0,0,0))

    #lets paste the original image into the transparent one
    transparent.paste(Real_image,(0,0))

    #Pasting the watermarked image on top of the combined transpatent and original image
    transparent.paste(Watermark, new_position, Watermark)
    image_mode = Real_image.mode
    print(image_mode)

    if image_mode == 'RGB':
        transparent = transprent.convert(image_mode)
    else:
        transparent = transparent.convert('P')

    transparent.save(output_image_path, optimize = True, quality = 100)
    print("Savng" + output_image_path + "...")

#Lets work with our sytem folders now and understand the power of the os module
folder = input('Please Enter Folder Path: ')
Watermark = input('Enter Watermark Path: ')

#this os.chdir is used to change the current working directory. it hanges the cwd to a specified path
#It only takes sigle arguments as a new directory path 
#the current working directory or cwd is the folder in which the python script is operating



#os.listdir() method is used to get the list of all files and directories in the specified directories
#os.getcwd() method is used to get the location of the current working directory
#In this code,the specified directory for the os.listdir is the cwd
files = os.listdir(os.getcwd())
print(files)

if not os.path.isdir("output"):
    os.mkdir('output')

c = 1
for f in files:
    if os.path.isfile(os.path.abspath(f)):
        if f.endswith(".png") or f.endswith(".jpg"):
            




