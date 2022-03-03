import json
import os
import numpy as np
import tensorflow as tf
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from keras.models import load_model
from keras.preprocessing import image
from tensorflow import Graph

from finalApp.models import Image

img_height, img_width = 224, 224
with open('./models/imagenet_classes.json', 'r') as f:
    labelList = f.read()

labelList = json.loads(labelList)

model_graph = Graph()
with model_graph.as_default():
    session = tf.compat.v1.Session()
    with session.as_default():
        model = load_model('./models/MobileNetModelImagenet.h5')


def index(req):
    context = {'image': "", 'label': ""}
    return render(req, 'index.html', context)


def classifyImg(req):
    fObj = req.FILES['imagePath']
    fStorage = FileSystemStorage()

    imgPath = fStorage.save(fObj.name, fObj)
    imgPath = fStorage.url(imgPath)

    img = '.' + imgPath
    img = image.load_img(img, target_size=(img_height, img_width))

    imgArr = image.img_to_array(img)
    imgArr = imgArr / 255
    imgArr = imgArr.reshape(1, img_height, img_width, 3)

    with model_graph.as_default():
        with session.as_default():
            prediction = model.predict(imgArr)

    pLabel = labelList[str(np.argmax(prediction[0]))]

    dbImage = Image()
    dbImage.path = imgPath
    dbImage.predicted_label = pLabel[1]
    dbImage.save()

    context = {'image': imgPath, 'label': pLabel[1]}
    return render(req, 'index.html', context)


def showHistory(request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'history.html', context)
