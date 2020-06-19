# import keras
import keras

# import keras_retinanet
from keras_retinanet import models
from keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
from keras_retinanet.utils.visualization import draw_box, draw_caption
from keras_retinanet.utils.colors import label_color
from keras_retinanet.utils.gpu import setup_gpu

# import miscellaneous modules
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
import time

# use this to change which GPU to use
gpu = 0

# set the modified tf session as backend in keras
setup_gpu(gpu)

# adjust this to point to your downloaded/trained model
# models can be downloaded here: https://github.com/fizyr/keras-retinanet/releases
model_path = os.path.join('saved_models', 'resnet101_csv_05_converted.h5')

# load retinanet model
model = models.load_model(model_path, backbone_name='resnet101')

# if the model is not converted to an inference model, use the line below
# see: https://github.com/fizyr/keras-retinanet#converting-a-training-model-to-inference-model
#model = models.convert_model(model)

#print(model.summary())

# load label to names mapping for visualization purposes
labels_to_names = {1: 'tops', 2: 'trousers', 3: 'outerwear', 4: 'dresses', 5: 'skirts'}


import glob

image_paths = []
for filename in glob.glob('../data/val/val/*.jpg'):
    # folder, file = filename.split('/')
    tmp = filename.split('/')
    x = ""
    for i in range(len(tmp)-1): x += tmp[i]

    folder, file = x, tmp[-1]
    idx, typ = file.split('.')
    image_paths.append([int(idx), file])

res = []
for idx, image in image_paths:
    # load image
    image = read_image_bgr('../data/val/val/'+image)

    # preprocess image for network
    image = preprocess_image(image)
    image, scale = resize_image(image)

    # process image
    boxes, scores, labels = model.predict_on_batch(np.expand_dims(image, axis=0))

    # correct for image scale
    boxes /= scale

    # extract boxes with greater than 0.5 confidence
    for box, score, label in zip(boxes[0], scores[0], labels[0]):
        # scores are sorted so we can break
        if score < 0.5: break

        # add to res
        x1, y1, x2, y2 = list(box)
        tmp = {
                "image_id": int(idx),
                "category_id": int(label)+1,
                "bbox": [
                    int(x1), int(y1), int(x2-x1), int(y2-y1)
                ],
                "score": float(score)
            }
        res.append(tmp)


res.sort(key=lambda x: x['image_id'])

import json
with open('ans.json', 'w') as outfile:
    json.dump(res, outfile)