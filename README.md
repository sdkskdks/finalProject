## Title

Python final project


##
Installation

pip install django

pip install tensorflow

pip install keras

pip install Pillow

##
Usage

Import django.urls

import Views

import models

import requests






##
Example

with model_graph.as_default():
    session = tf.compat.v1.Session()
    with session.as_default():
        model = load_model('./models/MobileNetModelImagenet.h5')

with open('./models/imagenet_classes.json', 'r') as f:
    labelList = f.read()

labelList = json.loads(labelList)
    
    
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd1t2donk1el9m1',
        'USER': 'llponbsnkqzzos',
        'PASSWORD': '3e2710cf69ff7a2a4677bc850d8dfcb137be957d69ca797ba86b578b2b1188d7',
        'HOST': 'ec2-176-34-105-15.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',
    }
}





