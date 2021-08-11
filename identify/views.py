from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import load_img
import tensorflow as tf
import numpy as np
from django.http import HttpResponse
import cv2
import os


# Create your views here.
def index(request):
    if request.method == 'POST':
        myfiles = request.FILES['myfiles']
        fs = FileSystemStorage()
        filename = fs.save(myfiles.name, myfiles)
        uploaded_file_url = (fs.url(filename))[1:]
    else:
        uploaded_file_url = '';
    return render(request,'identify.html',
        {
        'judul':'Classification',
        'uploaded_file_url':uploaded_file_url,
        }
        )

def tampilkan(request):
     return render(request,'identify.html',
         {
         'judul':'Form',
         'uploaded_file_url':''
         }
         )
     myfile = request.FILES['myfiles']
     fs = FileSystemStorage()
     filename = fs.save(myfiles.name, myfiles)
     uploaded_file_url = fs.url(filename)
     return render(request, 'identify.html',{
          'uploaded_file_url':uploaded_file_url,
          'judul':'berhasil'
     })

def prosesImg(request):
    filelink = request.POST.dict().get("myfiles")

    tf.compat.v1.disable_eager_execution()
    img_height, img_width=28,28
    model_graph = tf.Graph()
    with model_graph.as_default():
        tf_session=tf.compat.v1.Session()
        with tf_session.as_default():
            models=load_model('./model/trainbaru.model')

    testimage='.'+filelink

    img = image.load_img(testimage, target_size=(img_height, img_width))
    x = image.img_to_array(img)
    x = x.reshape(1, img_height, img_width, 3)
    predictedLabel = ''
    with model_graph.as_default():
        with tf_session.as_default():
            predi = models.predict(x)

    if np.argmax(predi) == 0:
        predictedLabel = """Classification : huruf A <br/>"""

    elif np.argmax(predi) == 1:
        predictedLabel = """Classification : huruf B <br/>"""

    elif np.argmax(predi) == 2:
        predictedLabel = """Classification : huruf C <br/>"""

    elif np.argmax(predi) == 3:
        predictedLabel = """Classification : huruf D <br/>"""

    elif np.argmax(predi) == 4:
        predictedLabel = """Classification : huruf E <br/>"""

    elif np.argmax(predi) == 5:
        predictedLabel = """Classification : huruf F <br/>"""

    elif np.argmax(predi) == 6:
         predictedLabel = """Classification : huruf G <br/>"""

    elif np.argmax(predi) == 7:
        predictedLabel = """Classification : huruf H <br/>"""

    elif np.argmax(predi) == 8:
        predictedLabel = """Classification : huruf I <br/>"""

    elif np.argmax(predi) == 9:
        predictedLabel = """Classification : huruf J <br/>"""

    elif np.argmax(predi) == 10:
        predictedLabel = """Classification : huruf K <br/>"""

    elif np.argmax(predi) == 11:
        predictedLabel = """Classification : huruf L <br/>"""

    elif np.argmax(predi) == 12:
        predictedLabel = """Classification : huruf M <br/>"""

    elif np.argmax(predi) == 13:
        predictedLabel = """Classification : huruf N <br/>"""

    elif np.argmax(predi) == 14:
        predictedLabel = """Classification : huruf O <br/>"""

    elif np.argmax(predi) == 15:
        predictedLabel = """Classification : huruf P <br/>"""

    elif np.argmax(predi) == 16:
        predictedLabel = """Classification : huruf Q <br/>"""

    elif np.argmax(predi) == 17:
         predictedLabel = """Classification : huruf R <br/>"""
        #predictedLabel = """Classification : huruf C <br/>"""

    elif np.argmax(predi) == 18:
        predictedLabel = """Classification : huruf S <br/>"""

    elif np.argmax(predi) == 19:
        predictedLabel = """Classification : huruf T <br/>"""

    elif np.argmax(predi) == 20:
       predictedLabel = """Classification : huruf U <br/>"""

    elif np.argmax(predi) == 21:
        predictedLabel = """Classification : huruf V <br/>"""

    elif np.argmax(predi) == 22:
        predictedLabel = """Classification : huruf W <br/>"""

    elif np.argmax(predi) == 23:
        predictedLabel = """Classification : huruf X <br/>"""

    elif np.argmax(predi) == 24:
        predictedLabel = """Classification : huruf Y <br/>"""

    else:
        predictedLabel = """Classification : huruf Z <br/>"""

    return render(request, 'hasil.html', {
        'judul': 'Result',
        'subjudul': 'RESULT',
        'predictedLabel': predictedLabel,
        'predi': predi,
        'uploaded_file_url': filelink }
                  )