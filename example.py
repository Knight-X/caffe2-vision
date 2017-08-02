from caffe2.proto import caffe2_pb2
from caffe2.python import model_helper
from caffe2.python import workspace
import os
MODEL = 'squeezenet', 'init_net.pb', 'predict_net.pb'

#init_net.pb is in the ~/squeezenet/init_net.pb
#predict_net.pb is in the ~/squeezenet/predict_net.pb
CAFFE_MODELS = "Your path"
INIT_NET = os.path.join(CAFFE_MODELS, MODEL[0], MODEL[1])
PREDICT_NET = os.path.join(CAFFE_MODELS, MODEL[0], MODEL[2])
pred = caffe2_pb2.NetDef()
init = caffe2_pb2.NetDef()
with open(PREDICT_NET) as f:
    pred.ParseFromString(f.read())
with open(INIT_NET) as g:
    init.ParseFromString(g.read())

import dataset.feature as feature
init_n, pred_n = feature.splitmodel(pred, init, 'pool10')
pren = workspace.Predictor(pred_n.SerializeToString(), init_n.SerializeToString())