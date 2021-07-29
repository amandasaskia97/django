from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def index (request):
    #return render(request,'TA/index.html')

#def recent (request):
    #return HttpResponse('<h1>ini recent post</h1>')

from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
import tensorflow as tf
from tensorflow import Graph
from matplotlib import pyplot as plt
#from skimage import io
import string
import random
#from .imageProses import ImageTransform


# Create your views here.
def index(request):
    return render(request, 'classification/index.html', {
        'uploaded_file_url': '',
        'judul': 'Classification'
    })


def review(request):
    myfile = request.FILES['myfile']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)
    return render(request, 'classification/index.html', {
        'uploaded_file_url': uploaded_file_url,
        'judul': 'Classification'
    })


def prosesImg(request):
    filelink = request.POST.dict().get("myfile")

    tf.compat.v1.disable_eager_execution()
    img_height, img_width = 224, 224
    model_graph = tf.Graph()
    with model_graph.as_default():
        tf_session = tf.compat.v1.Session()
        with tf_session.as_default():
            models = load_model('./model/BrailleNet.h5')

    testimage = '.' + filelink

    img = image.load_img(testimage, target_size=(img_height, img_width))
    x = image.img_to_array(img)
    x = x / 255
    x = x.reshape(1, img_height, img_width, 3)
    with model_graph.as_default():
        with tf_session.as_default():
            predi = models.predict(x)

    if np.argmax(predi) == 0:
        predictedLabel = """Classification : Muda <br/>
                        Prediction       : Jika curah hujan bagus, 2,5-3 bulan akan menjadi buah setengah matang dan 3,5-4,5 bulan lagi akan matang"""

    elif np.argmax(predi) == 1:
        predictedLabel = """Classification : Setengah Matang <br/> 
                        Prediction       : Jika curah hujan bagus, 1-2 bulan lagi akan matang <br/>
                        Kandungan Protein : 9.57 % <br/>
                        Kandungan Gula : 1.428 %<br/>
                        Kandungan Lemak : 8.2 %<br/>
                        Kandungan Kafein : 0.62 %<br/>
                        pH : 5.3<br/>"""

    elif np.argmax(predi) == 2:
        predictedLabel = """Classification : Matang <br/>
                        Prediction       : Kualitas baik untuk dipanen dan bagus untuk dijadikan benih <br/>
                        Kandungan Protein : 9.61 % <br/>
                        Kandungan Gula : 1.652 %<br/>
                        Kandungan Lemak : 7.8 %<br/>
                        Kandungan Kafein : 0.65 %<br/>
                        pH : 5.5<br/>"""

    else:
        predictedLabel = """Classification : Tua <br/>
                        Prediction       : Sudah melewati masa panen <br/>
                        Kandungan Protein : 9.48 % <br/>
                        Kandungan Gula : 2.074 %<br/>
                        Kandungan Lemak : 8.5 %<br/>
                        Kandungan Kafein : 0.7 %<br/>
                        pH : 5.7<br/>"""

    # myImage = ImageTransform(testimage)
    # myImage.resize(1500,'area').edgeDetect().cropImage().rotate(90).write('output.jpg')

    # histogram


    myimgname = id_generator()
    plt.savefig("./album/" + myimgname + "_r.png")
    plt.close()


    plt.savefig("./album/" + myimgname + "_g.png")
    plt.close()



    plt.savefig("./album/" + myimgname + "_b.png")
    plt.close()

    return render(request, 'classification/hasil.html', {
        'judul': 'Result',
        'subjudul': 'RESULT',
        'histogram_img_r': "/album/" + myimgname + "_r.png",
        'histogram_img_g': "/album/" + myimgname + "_g.png",
        'histogram_img_b': "/album/" + myimgname + "_b.png",
        'banner': '/static/classification/image/oke.jpg',
        'predictedLabel': predictedLabel,
        'predi': predi,
        'uploaded_file_url': filelink,
    })


def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))