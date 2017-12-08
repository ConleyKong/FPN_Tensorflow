# -*- coding: utf-8 -*-
from __future__ import division, print_function, absolute_import
import os

# root path
ROOT_PATH = os.path.abspath('/yangxue/FPN_v2.0')

# pretrain weights path
TEST_SAVE_PATH = ROOT_PATH + '/tools/test_result'
INFERENCE_IMAGE_PATH = ROOT_PATH + '/tools/inference_image'
INFERENCE_SAVE_PATH = ROOT_PATH + '/tools/inference_result'

NET_NAME = 'resnet_v1_101'
VERSION = 'v1_sar_ship'
CLASS_NUM = 1
BASE_ANCHOR_SIZE_LIST = [32, 64, 128, 256, 512]
LEVEL = ['P2', 'P3', 'P4', 'P5', "P6"]
STRIDE = [4, 8, 16, 32, 64]
ANCHOR_SCALES = [1.]
ANCHOR_RATIOS = [1 / 3., 1., 3.0]
SCALE_FACTORS = [10., 10., 5., 5.]
OUTPUT_STRIDE = 16
SHORT_SIDE_LEN = 512
DATASET_NAME = 'SSDD'

BATCH_SIZE = 1
WEIGHT_DECAY = {'resnet_v1_50': 0.0001, 'resnet_v1_101': 0.0001}
EPSILON = 1e-5
MOMENTUM = 0.9
MAX_ITERATION = 500000
GPU_GROUP = "1"
LR = 0.001

# rpn
RPN_NMS_IOU_THRESHOLD = 0.5
MAX_PROPOSAL_NUM = 300
RPN_IOU_POSITIVE_THRESHOLD = 0.7
RPN_IOU_NEGATIVE_THRESHOLD = 0.3
RPN_MINIBATCH_SIZE = 256
RPN_POSITIVE_RATE = 0.5
IS_FILTER_OUTSIDE_BOXES = True
RPN_TOP_K_NMS = 10000

# fast rcnn
ROI_SIZE = 14
ROI_POOL_KERNEL_SIZE = 2
USE_DROPOUT = False
KEEP_PROB = 0.5
FAST_RCNN_NMS_IOU_THRESHOLD = 0.1
FAST_RCNN_NMS_MAX_BOXES_PER_CLASS = 20
FINAL_SCORE_THRESHOLD = 0.95
FAST_RCNN_IOU_POSITIVE_THRESHOLD = 0.5
FAST_RCNN_MINIBATCH_SIZE = 128
FAST_RCNN_POSITIVE_RATE = 0.25

