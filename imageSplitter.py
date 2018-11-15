import os.path
from PIL import Image

#The crop rectangle, as a (left, upper, right, lower)-tuple.
#note directory paramter isn't strictly enforce so good luck tracing relative path if you mess up
#and obviously change the png in the following line to change file format
def splitPicture(image,splice_width,splice_height,baseName,storageDirectory):
    fileNameIndex=0
    print("your storage directory \n"+storageDirectory)

    for i in range(0,image.size[1],splice_height):
        for j in range(0,image.size[0],splice_width):
            if j+splice_width>image.size[0]:
                image.crop([j,i,image.size[0],i+splice_height]).save(storageDirectory+"\\"+baseName+str(fileNameIndex)+".png")
            else:
                image.crop([j,i,j+splice_width,i+splice_height]).save(storageDirectory+"\\"+baseName+str(fileNameIndex)+".png")
            fileNameIndex=fileNameIndex+1   
        if i+splice_height>image.size[1]:
            for j in range(0,image.size[0],splice_width):
                if j+splice_width>image.size[0]:
                    image.crop([j,i,image.size[0],image.size[1]]).save(storageDirectory+"\\"+baseName+str(fileNameIndex)+".png")
                else:
                    image.crop([j,i,j+splice_width,image.size[1]]).save(storageDirectory+"\\"+baseName+str(fileNameIndex)+".png")
                fileNameIndex=fileNameIndex+1

    print("done")
    return True

def checkSplitCount(image,splice_width,splice_height):
    count=0
    for i in range(0,image.size[1],splice_height):
        for j in range(0,image.size[0],splice_width):
            if j+splice_width>image.size[0]:
                count=count+1
            else:
                count=count+1  
        if i+splice_height>image.size[1]:
            for j in range(0,image.size[0],splice_width):
                if j+splice_width>image.size[0]:
                    count=count+1
                else:
                    count=count+1
    return count

#os.path.dirname(os.path.realpath(__file__)
''' modify the below line for quick usage'''
#im = Image.open("C:/Users/someone/Downloads/3littlepig.png")
#splitPicture(im,256,256,"chunk","D://myFolder//cats")
#print(checkSplitCount(im,256,256))

