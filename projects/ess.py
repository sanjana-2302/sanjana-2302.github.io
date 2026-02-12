import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import argparse
import cv2
import matplotlib.pyplot as plt
import cv2
import numpy as np
import sys
import glob
import math
import time
import os
import itertools
import tkinter.messagebox as tm
#import requests
from PIL import Image
from numpy import average, linalg, dot
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
import matplotlib.pyplot as plt
import numpy as np
import argparse
from skimage import io, color, img_as_ubyte
from skimage.feature import greycomatrix, greycoprops
from sklearn.metrics.cluster import entropy
from PIL import Image, ImageStat

from scipy.stats import kurtosis, skew

import math
import argparse
import imutils

import pywt
import pywt.data
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import math
from matplotlib.figure import Figure
#from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

def process(path):
    # load the query image and describe it
        query = cv2.imread(path)

        #name= self.t1.GetValue()

        cv2.imshow("Input MRi Image", query)
                # Load image
        original = query

        
        
        file = path
        superpixel(file)
        feature ( file )
        existingcall(file , 0, type='rect')
        o1 = ertcall(file , 0, type='rect')
        bact =0
        viral=0
        fungal=0
        prozone=0
        norm=0
         #fi= load_images("data/")
        bactr= loadtrain ("Stage1/")
        viralr= loadtrain("Stage2/")
        fungalr=loadtrain("Stage3/")
        prozoner=loadtrain("Stage4/")
        normr=loadtrain("Normal/")
        for trf in bactr :
                bact= image_similarity_vectors_via_numpy(file ,trf )
                bact += bact
        print("Stage1",bact)
        avgval = bact /len (bactr)
        for ntr in normr:
                norm=image_similarity_vectors_via_numpy(file ,ntr )
                norm+=norm
        print ("Normal=",norm)
        avgvaln = norm /len (normr)
        print( 'Avg value Stage1=',avgval)
        print ('Avg value Normal=',avgvaln)
        for dtr in viralr:
                viral=image_similarity_vectors_via_numpy(file ,dtr )
                viral+=viral
        print ("Stage2",viral)
        avgvald = viral /len (viralr)
        print ('Avg value of Stage2=',avgvald)
        for ltr in fungalr:
                fungal=image_similarity_vectors_via_numpy(file ,ltr )
                fungal+=fungal
        print ("Stage3",fungal)
        avgvall = fungal /len (fungalr)
        print ('Avg value of Stage3=',avgvall)
        for ptr in prozoner:
                prozone=image_similarity_vectors_via_numpy(file ,ptr )
                prozone+=prozone
        print ("Stage4",prozone)
        avgvallpro = prozone /len (prozoner)
        print ('Avg value of Stage4=',avgvallpro)
        print( 'Avg value Stage1=',avgval)
        print ('Avg value Normal=',avgvaln)
        print ('Avg value of Stage2=',avgvald)
        print ('Avg value of Stage3=',avgvall)
        flag=0
        if (avgvald>avgvaln and avgvall<avgvald and avgval<avgvald and avgvallpro<avgvald):
                flag=1
        if (avgvall>avgvaln and avgvald<avgvall and avgval<avgvall and avgvallpro<avgvall ):
                flag=2
        if (avgval>avgvaln and avgvald<avgval and avgvall<avgval and avgvallpro<avgval ):
                flag=3
        if(avgvallpro>avgvaln and avgvald<avgvallpro and avgvall<avgvallpro and avgval<avgvallpro):
                flag=4
        print("Flag==",flag)
        if flag==0:
                resultText='Beginin'
                aa=1
                print("Result==",resultText)
        elif flag==1:
                resultText='Stage2'
                aa=(avgvald*10)
                print("Result==",resultText)
        elif flag==2:
                resultText='Stage3'
                aa=(avgvall*10)
                print("Result==",resultText)
        elif flag==3:
                resultText='Stage1'
                aa=(avgval*10)
                print("Result==",resultText)
        else:
                resultText='Stage4'
                aa=(avgvallpro*10)
                print("Result==",resultText)
        cv2.waitKey(0)
        return resultText,round(10-aa)
        
    
        #return resultText,round(10-aa)
            
def feature ( filename ):
    img = Image.open(filename)
    stat = ImageStat.Stat(img)
    stat = ImageStat.Stat(img)
    imageFile = filename
    im1 = Image.open('2.jpg')
    rgbHistogram = im1.histogram()
    #print 'Snannon Entropy for Red, Green, Blue:'
    for rgb in range(3):
        totalPixels = sum(rgbHistogram[rgb * 256 : (rgb + 1) * 256])
        ent = 0.0
        for col in range(rgb * 256, (rgb + 1) * 256):
            freq = float(rgbHistogram[col]) / totalPixels
            if freq > 0:
                ent = ent + freq * math.log(freq, 2)
        ent = -ent
    #print ent



    im = Image.open(filename)
    im_grey = im.convert('LA') # convert to grayscale
    width,height = im.size

    total=0
    for i in range(0,width):
        for j in range(0,height):
            total += im_grey.getpixel((i,j))[0]

    mean = total / (width * height)


    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]



    g_kernel = cv2.getGaborKernel((21, 21), 8.0, np.pi/4, 10.0, 0.5, 0, ktype=cv2.CV_32F)

    img = cv2.imread(filename)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    filtered_img = cv2.filter2D(img, cv2.CV_8UC3, g_kernel)

    

    #sfta

    #binary

    img = cv2.imread(filename,0)
    ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
    ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
    ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
    ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
    images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

    for i in range(6):
        plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])

    #plt.show()




    #boader


    img = img
    edges = cv2.Canny(img,100,200)

    plt.subplot(121),plt.imshow(img,cmap = 'gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(edges,cmap = 'gray')
    plt.title('Fractal Borders '), plt.xticks([]), plt.yticks([])

    #plt.show()



    h, w = g_kernel.shape[:2]
    g_kernel = cv2.resize(g_kernel, (3*w, 3*h), interpolation=cv2.INTER_CUBIC)
   

def superpixel ( filename ):
    image = cv2.imread(filename)
    segments = slic(img_as_float(image), n_segments = 100, sigma = 5)





    # show the output of SLIC
    fig = plt.figure("Superpixels")
    ax = fig.add_subplot(1, 1, 1)
    ax.imshow(mark_boundaries(img_as_float(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)), segments))
    plt.axis("off")
    #plt.show()

    img = image
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    gray = np.float32(gray)
    dst = cv2.cornerHarris(gray,2,3,0.04)

    #result is dilated for marking the corners, not important
    dst = cv2.dilate(dst,None)

    # Threshold for an optimal value, it may vary depending on the image.
    img[dst>0.01*dst.max()]=[0,0,255]
    cv2.imshow('Feature Extraction',img)



def validate_contour(contour, img, aspect_ratio_range, area_range):
    rect = cv2.minAreaRect(contour)
    img_width = img.shape[1]
    img_height = img.shape[0]
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    X = rect[0][0]
    Y = rect[0][1]
    angle = rect[2]
    width = rect[1][0]
    height = rect[1][1]

    angle = (angle + 180) if width < height else (angle + 90)

    output = False

    if (width > 0 and height > 0) and ((width < img_width / 2.0) and (height < img_width / 2.0)):
        aspect_ratio = float(width) / height if width > height else float(height) / width
        if (aspect_ratio >= aspect_ratio_range[0] and aspect_ratio <= aspect_ratio_range[1]):
            if ((height * width > area_range[0]) and (height * width < area_range[1])):

                box_copy = list(box)
                point = box_copy[0]
                del (box_copy[0])
                dists = [((p[0] - point[0]) ** 2 + (p[1] - point[1]) ** 2) for p in box_copy]
                sorted_dists = sorted(dists)
                opposite_point = box_copy[dists.index(sorted_dists[1])]
                tmp_angle = 90

                if abs(point[0] - opposite_point[0]) > 0:
                    tmp_angle = abs(float(point[1] - opposite_point[1])) / abs(point[0] - opposite_point[0])
                    tmp_angle = rad_to_deg(math.atan(tmp_angle))

                if tmp_angle <= 45:
                    output = True
    return output


def deg_to_rad(angle):
    return angle * np.pi / 180.0


def rad_to_deg(angle):
    return angle * 180 / np.pi


def enhance(img):
    kernel = np.array([[-1, 0, 1], [-2, 0, 2], [1, 0, 1]])
    return cv2.filter2D(img, -1, kernel)





def existingcall(name, debug, type=None, **options):
    se_shape = (16, 4)

    if type == 'rect':
        se_shape = (17, 4)

    elif type == 'square':
        se_shape = (7, 6)

    raw_image = cv2.imread(name, 1)
    input_image = np.copy(raw_image)

    gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)    
    gray = enhance(gray)
    exist=gray
    gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)    
    thresh = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 11, 1)
    kernel = np.ones((3, 3), np.uint8)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE,kernel, iterations=4)    
    input_image1=input_image
    im = input_image
    im1 = input_image

    # sure background area
    sure_bg = cv2.dilate(closing, kernel, iterations=3)
   ## cv2.imshow('sure_bg', sure_bg)

    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    #sure_bg=np.unit8(sure_bg)
    lower_black = np.array([0, 0, 0], dtype="uint16")
    upper_black = np.array([70, 70, 70], dtype="uint16")
    #black_mask = cv2.inRange(sure_bg, lower_black, upper_black)
    unknown = cv2.subtract(sure_bg, sure_fg)
    #unknown = cv2.subtract(enhance(gray), sure_bg)
   ## cv2.imshow('unknown', unknown)

    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)
   # ret, markers = cv2.connectedComponents(sure_bg)

    # Add one to all labels so that sure background is not 0, but 1
    markers = markers + 1

    # Now, mark the region of unknown with zero
    markers[unknown == 255] = 0

    markers = cv2.watershed(input_image, markers)
    input_image[markers == -1] = [255, 0, 0]

    cv2.imshow('Result  watershed algo Image', input_image)

    

    return input_image




def ertcall(name, debug, type=None, **options):
    se_shape = (16, 4)

    if type == 'rect':
        se_shape = (17, 4)

    elif type == 'square':
        se_shape = (7, 6)

    raw_image = cv2.imread(name, 1)
    input_image = np.copy(raw_image)

    gray = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Image', gray)
    gray = enhance(gray)
    cv2.imshow('Enhance Image Image', gray)

    gray_blur = cv2.GaussianBlur(gray, (15, 15), 0)
    cv2.imshow('Gray Blur', gray_blur)
    thresh = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV, 11, 1)
    cv2.imshow('Threshold Image', thresh)

    kernel = np.ones((3, 3), np.uint8)
    closing = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE,kernel, iterations=4)
    cv2.imshow('Kernal Image', thresh)
    input_image1=input_image
    im = input_image
    im1 = input_image

    # sure background area
    sure_bg = cv2.dilate(closing, kernel, iterations=3)
   ## cv2.imshow('sure_bg', sure_bg)

    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(closing, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    #sure_bg=np.unit8(sure_bg)
    lower_black = np.array([0, 0, 0], dtype="uint16")
    upper_black = np.array([70, 70, 70], dtype="uint16")
    #black_mask = cv2.inRange(sure_bg, lower_black, upper_black)
    cv2.imshow('Segmented Image', sure_bg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    #unknown = cv2.subtract(enhance(gray), sure_bg)
   ## cv2.imshow('unknown', unknown)

    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)
   # ret, markers = cv2.connectedComponents(sure_bg)

    # Add one to all labels so that sure background is not 0, but 1
    markers = markers + 1

    # Now, mark the region of unknown with zero
    markers[unknown == 255] = 0

    
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    __,contours,hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(im1, contours, -1, (0, 255, 0), 1)

    cv2.imshow('Result Image', im1 )
    


    return input_image


def get_thumbnail(image, size=(128,128), greyscale=False):
    #get a smaller version of the image - makes comparison much faster/easier
    image = image.resize(size, Image.ANTIALIAS)
    if greyscale:
        #convert image to greyscale
        image = image.convert('L')
    return image

def load_images(folder):
    images = []
    for filename in os.listdir(folder):
        img = os.path.join(folder, filename)
        if img is not None:
            images.append(img)
    return images


def loadtrain(folder):
    images = []
    for filename in os.listdir(folder):
        img = os.path.join(folder, filename)
        if img is not None:
            images.append(img)
    return images

def savefile(folder):
    images = []
    for filename in os.listdir(folder):
        img =  filename
        if img is not None:
            images.append(img)
    return images

def image_similarity_vectors_via_numpy(filepath1, filepath2):
    image1 = Image.open(filepath1)
    image2 = Image.open(filepath2)

    image1 = get_thumbnail(image1)
    image2 = get_thumbnail(image2)

    images = [image1, image2]
    vectors = []
    norms = []
    for image in images:
        vector = []
        for pixel_tuple in image.getdata():
            vector.append(average(pixel_tuple))
        vectors.append(vector)
        norms.append(linalg.norm(vector, 2))
    a, b = vectors
    a_norm, b_norm = norms
    # If we did not resize the images to be equal, we would get an error here
    # ValueError: matrices are not aligned
    res = dot(a / a_norm, b / b_norm)
    return res
    
#print(process("./Stage4/Screenshot 2023-11-03 164746.png"))
#process("./Stage1/Screenshot 2023-11-27 190513.png")
#process("./Stage2/Screenshot 2023-11-03 165752.png")
#process("./Stage3/Screenshot 2023-11-03 164931.png")
