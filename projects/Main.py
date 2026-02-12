import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import pandas as pd

import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import matplotlib.pyplot as plt
import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm

import trainalgo as TR
import predictonimage as PR
import ess as DT
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
#from skimage.feature import greycomatrix, greycoprops
from sklearn.metrics.cluster import entropy
from PIL import Image, ImageStat
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
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
import glob
from keras.models import Sequential, load_model


bgcolor="#DAF7A6"
bgcolor1="#B7C526"
fgcolor="black"
def Home():
        global window
        def clear():
            print("Clear1")
               
            txt1.delete(0, 'end')    
            txt2.delete(0, 'end')    
            txt3.delete(0, 'end')    



        window = tk.Tk()
        window.title("Liver Disease Prediction")

 
        window.geometry('1280x720')
        window.configure(background=bgcolor)
        #window.attributes('-fullscreen', True)

        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        

        message1 = tk.Label(window, text="Liver Disease Prediction Using Deep Learning" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('times', 30, 'italic bold underline')) 
        message1.place(x=100, y=20)

        

        lbl1 = tk.Label(window, text="Select Train Dataset",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl1.place(x=100, y=270)
        
        txt1 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt1.place(x=400, y=275)

        lbl2 = tk.Label(window, text="Select Test Dataset",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl2.place(x=100, y=340)
        
        txt2 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt2.place(x=400, y=345)

        lbl3 = tk.Label(window, text="Select Image",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
        lbl3.place(x=100, y=420)
        
        txt3 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
        txt3.place(x=400, y=425)
        

        def browse():
                path=filedialog.askdirectory()
                print(path)
                txt.delete(0, 'end')
                txt.insert('end',path)
                if path !="":
                        print(path)
                else:
                        tm.showinfo("Input error", "Select DataSet Folder")     

        def browse1():
                path=filedialog.askdirectory()
                print(path)
                txt1.delete(0, 'end')
                txt1.insert('end',path)
                if path !="":
                        print(path)
                else:
                        tm.showinfo("Input error", "Select Training Dataset Folder")    

        def browse2():
                path=filedialog.askdirectory()
                print(path)
                txt2.delete(0, 'end')
                txt2.insert('end',path)
                if path !="":
                        print(path)
                else:
                        tm.showinfo("Input error", "Select Test Dataset Folder")        

        def browse3():
                path=filedialog.askopenfilename()
                print(path)
                txt3.delete(0, 'end')
                txt3.insert('end',path)
                if path !="":
                        print(path)
                else:
                        tm.showinfo("Input error", "Select Input Image")        

        def preproc():
                sym=txt.get()
                if sym != "" :
                        pre.process(sym)
                        print("preprocess")
                        tm.showinfo("Input", "Preprocess Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Dataset")

        def Trainprocess():
                sym=txt1.get()
                sym1=txt2.get()
                if sym != "" and sym1 != "":
                        TR.process()
                        tm.showinfo("Input", "Training Successfully Finished")
                else:
                        tm.showinfo("Input error", "Select Train and Test Dataset Folder")

        def Predictprocess():
                sym=txt3.get()
                if sym != "" :
                        res,prob=PR.process(sym)
                        result=""
                        if res==0:
                                result="Normal"
                        if res==1:
                                result="Cancerous"
                        

                        tm.showinfo("Output", "Class :   "+str(result)+" Probability: "+str(prob))
                else:
                        tm.showinfo("Input error", "Select Input Image")
        

        def esprocess():
                sym=txt3.get()
                
                ttype=""
                stime=""
                treat=""
                if sym != "" :
                        level,lifetime=DT.process(sym)
                        if level=='Beginin':
                                tm.showinfo("Result","Diagnosis: Begining Tumor")
                                tm.showinfo("Life Expectancy","About"+str(10)+" Years")
                                tm.showinfo("Recommended Treatement","Curable")
                                ttype="Begining Tumour"
                                stime=str(10)+"years"
                                treat="Curable after surgery"
                        if level=='Stage1':
                                tm.showinfo("Result","Diagnosis:Stage 1 ")
                                tm.showinfo("Life Expectancy","About"+str(8)+" Years")
                                tm.showinfo("Recommended Treatement","Curable with partial hepatectomy")
                                ttype="Stage1 Tumour"
                                stime=str(8)+"years"
                                treat="Limited Curable after partial hepatectomy"
                        if level=='Stage2':
                                tm.showinfo("Result","Diagnosis: Stage 2")
                                tm.showinfo("Life Expectancy","About"+str(6)+" Years")
                                tm.showinfo("Recommended Treatement","Critical: Doctor can aid with treatments to help manage symptoms and reduce further complications")
                                ttype="Stage2 Tumour"
                                stime=str(6)+"years"
                                treat="Critical The doctor can advise on treatments to help manage symptoms and reduce the risk of complications."
                        if level=='Stage3':
                                tm.showinfo("Result","Diagnosis: Stage 3")
                                tm.showinfo("Life Expectancy","About"+str(5)+" Years")
                                tm.showinfo("Recommended Treatement","Critical: Transplant might be necessary")
                                ttype="Stage 3"
                                stime=str(5)+"years"
                                treat="transplant is needed"
                        if level=='Stage4':
                                tm.showinfo("Result","Diagnosis: Stage 4")
                                tm.showinfo("Life Expectancy","About"+str(1)+" Year")
                                tm.showinfo("Recommended Treatement"," Extremely Critical")
                                ttype="Stage 4"
                                stime=str(1)+"years"
                                treat="treatment won't be able to cure it"
                        
                       
                else:
                        tm.showinfo("Input error", "Select input image or Fill Patient Name")

        
        browse1 = tk.Button(window, text="Browse", command=browse1  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse1.place(x=650, y=270)

        browse2 = tk.Button(window, text="Browse", command=browse2  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse2.place(x=650, y=340)

        browse3 = tk.Button(window, text="Browse", command=browse3  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
        browse3.place(x=650, y=420)

        clearButton = tk.Button(window, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
        clearButton.place(x=950, y=200)
         
        

        TRbutton = tk.Button(window, text="Training", command=Trainprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        TRbutton.place(x=400, y=600)


        PRbutton = tk.Button(window, text="Prediction", command=Predictprocess  ,fg=fgcolor   ,bg=bgcolor1 ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        PRbutton.place(x=620, y=600)

        DCbutton = tk.Button(window, text="Predict Area", command=esprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        DCbutton.place(x=800, y=600)



        quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
        quitWindow.place(x=1030, y=600)

        window.mainloop()
Home()

