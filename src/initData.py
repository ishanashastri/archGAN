import os
import pandas as pd 
import numpy as np
import cv2

trainset_path = '../data/arch_trainset.pickle'
testset_path  = '../data/arch_testset.pickle'
dataset_path = '../data/storage/'

if not os.path.exists( trainset_path ) or not os.path.exists( testset_path ):

    for folder in os.listdir(dataset_path):
        files = np.random.choice(os.listdir(dataset_path), len(os.listdir(dataset_path)*0.75,replace=False))
        trainset = pd.DataFrame({'image_path': map(lambda x: os.path.join('../data', x), files})
    #trainset_dir = os.path.join( dataset_path, 'arch_train_original' )
    #testset_dir = os.path.join( dataset_path, 'arch_eval_gt' )

    trainset = pd.DataFrame({'image_path': map(lambda x: os.path.join( trainset_dir, x ), os.listdir(trainset_dir))})
    testset = pd.DataFrame({'image_path': map(lambda x: os.path.join( testset_dir, x ), os.listdir(testset_dir))})

    trainset.to_pickle( trainset_path )
    testset.to_pickle( testset_path )

print("-------------------")
print("Dataset Initialized")
print("-------------------")