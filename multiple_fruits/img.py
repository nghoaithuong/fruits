import cv2
import tensorflow as tf
import sys
import os
import random

train_dir = '/home/hoaithuong/PycharmProjects/multiple_fruits/train'
test_dir = '/home/hoaithuong/PycharmProjects/multiple_fruits/test'
#print(len(train_dir))
#sys.exit()
#creat filename of banana and apple
train_apples = ['/home/hoaithuong/PycharmProjects/multiple_fruits/train/{}'.format(i) for i in os.listdir(train_dir) if 'apple' in i]
train_bananas = ['/home/hoaithuong/PycharmProjects/multiple_fruits/train/{}'.format(i) for i in os.listdir(train_dir) if 'banana' in i]
train_plums  = ['/home/hoaithuong/PycharmProjects/multiple_fruits/train/{}'.format(i) for i in os.listdir(train_dir) if 'plum' in i]
train_kiwis  = ['/home/hoaithuong/PycharmProjects/multiple_fruits/train/{}'.format(i) for i in os.listdir(train_dir) if 'kiwi' in i]
train_pineapples  = ['/home/hoaithuong/PycharmProjects/multiple_fruits/train/{}'.format(i) for i in os.listdir(train_dir) if 'pinea' in i]

#train_img = train_apples + train_bananas + train_plums + train_kiwis + train_pineapples
#print(train_img)
print(len(train_apples))
print(len(train_bananas))
print(len(train_plums))
print(len(train_kiwis))
print(len(train_pineapples))
train_img = train_apples + train_bananas + train_plums + train_kiwis + train_pineapples
print(len(train_img))
