from django.shortcuts import render,HttpResponse
from django.core.files.storage import FileSystemStorage
import matplotlib.pyplot as plt
import cv2
import tensorflow as tf
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np

def prepare(filepath):
    IMG_SIZE = 50
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    # plt.imshow(img_array)
    # plt.show()
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    # plt.imshow(new_array)
    # plt.show()
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

def mainpage(request):
    return render(request,'mainpage.html')

def aboutAlgorithm(request):
    return render(request,'aboutAlgorithm.html')

def predictImage(request):
    fileObj = request.FILES['filePath']
    fs = FileSystemStorage()
    filePathName = fs.save(fileObj.name,fileObj)
    filePathName = fs.url(filePathName)
    model = tf.keras.models.load_model('.\\models\\farmproduceclassifier.h5')
    path = 'D:\\Study Material\\FARM PRODUCE CLASSIFICATION\pscproject\\media\\'
    path += fileObj.name
    prediction = model.predict([prepare(path)])
    res = ""
    filePathName = 'D:\WhatsApp Image 2022-11-30 at 5.25.45 PM'
    print(filePathName)
    if (prediction[0][0] == 1): res = "Rotten"
    else: res = "Fresh"
    context = {'filePathName' : filePathName,'prediction' : res}
    return render(request,'ansFile.html',context)