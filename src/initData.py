import os
import pandas as pd 
import numpy as np
import cv2

# trainset_path = '../data/arch_trainset.pickle'
# testset_path  = '../data/arch_testset.pickle'
# dataset_path = '../data/storage/'

def pickler(trainset_path, testset_path, dataset_path):
    trfiles = []
    tsfiles = []

    trainset = pd.DataFrame()
    testset = pd.DataFrame()
    
    for folder in os.listdir(dataset_path):
        if not os.path.isdir(os.path.join(dataset_path, folder)): #Ignore individual files
            continue
        tr = np.random.choice(os.listdir(os.path.join(dataset_path, folder)), #Split 0.75 of data into training set
                                 round(len(os.listdir(os.path.join(dataset_path, folder)))*0.75), replace=False) 
        #trfiles = np.append(trfiles, tr) #DEBUGGING: Append local list to global list of files to check length
        
        loctr = pd.DataFrame({'image_path': [os.path.join(dataset_path, folder, i) for i in list(tr)]}) #Create DataFrame
        trainset = trainset.append(loctr) #Append local dataframe to global dataframe of files
        
    for folder in os.listdir(dataset_path):
        ts = []
        if not os.path.isdir(os.path.join(dataset_path, folder)):
            continue
        for file in os.listdir(os.path.join(dataset_path, folder)):
            if file not in trfiles: #Place remaining files into test set
                ts = np.append(ts, file)
                tsfiles = np.append(tsfiles, file) #DEBUGGING: Append local list to global list of files to check length
        locts = pd.DataFrame({'image_path': [os.path.join(dataset_path, folder, i) for i in list(ts)]}) 
        testset = testset.append(locts)
        
    #Check to make sure it's initialized properly
    if np.array_equal(trfiles, tsfiles):
        print("you done fucked up.")

    trainset.to_pickle(trainset_path)
    testset.to_pickle(testset_path)

    print("-------------------")
    print("Dataset Initialized")
    print("-------------------")

    return trainset, testset