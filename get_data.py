import os
import numpy as np
import pandas as pd 
from zipfile import ZipFile
from kaggle.api.kaggle_api_extended import KaggleApi
from sklearn.model_selection import StratifiedShuffleSplit


# Get 2 levels up in directory structure to root directory of the project
#PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) 
PROJECT_ROOT = os.getcwd()
RAW_DATA_DIR = os.path.join(PROJECT_ROOT, "data/raw")
DATASET_NAME_KAGGLE = "titanic"

RAW_FILE_PATH = os.path.join(RAW_DATA_DIR, "titanic.zip")
RAW_TRAIN_PATH = os.path.join(RAW_DATA_DIR, "train.csv")
RAW_TEST_PATH = os.path.join(RAW_DATA_DIR, "test.csv")
RAW_DISPLAY_PATH = "/data/raw"

INTERM_DATA_DIR = os.path.join(PROJECT_ROOT, "data/intermi")
INTERM_TRAIN_PATH = os.path.join(INTERM_DATA_DIR, "train.csv")
INTERM_TEST_PATH = os.path.join(INTERM_DATA_DIR, "test.csv")



def download_titanic_data_from_kaggle(redownload_flag = False):
    """
    Make sure you have added kaggle.json file in .kaggle folder in Users/username folder.
    """
    if redownload_flag is True or os.path.exists(RAW_FILE_PATH) is False:
        api = KaggleApi()
        api.authenticate()
        os.chdir(RAW_DATA_DIR)
        files = api.competition_download_files(DATASET_NAME_KAGGLE)
        print("Dataset downloaded at " + RAW_DISPLAY_PATH)
    else: 
        print("Dataset already downloaded at " + RAW_DISPLAY_PATH)
        

def unzip_data(unzip_again_flag = False):
    if unzip_again_flag is True or os.path.exists(RAW_TRAIN_PATH) is False and os.path.exists(RAW_TEST_PATH) is False:
        zip_file = ZipFile(RAW_FILE_PATH)
        zip_file.extractall(path=RAW_DATA_DIR)
        zip_file.close()
        print("Data Unziped at " + RAW_DISPLAY_PATH)
    else:
        print("Data is already unziped at " + RAW_DISPLAY_PATH)

def load_raw_data():
    return pd.read_csv(RAW_TRAIN_PATH)

    
def stratified_split_data(raw_data, category): 
    """
    Makes Stratified 20% Split and Save the Data at Intermidiate Data Directory
    For Modification of Parameter, visit function's module: get_data.py
    n_splits=1, test_size=0.2, random_state=40
    Future Condiderations: Dynamic Passing of other Arguments
    """
    split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=40)
    for train_index,test_index in split.split(raw_data, raw_data[category]):
        strat_train_set = raw_data.iloc[train_index]
        strat_test_set  = raw_data.iloc[test_index]   
    save_stratified_data(strat_train_set, strat_test_set)
    
        
def save_stratified_data(train, test):
    train.to_csv(INTERM_TRAIN_PATH, index=False)
    test.to_csv(INTERM_TEST_PATH, index=False)
    print("Saved at "+ INTERM_DATA_DIR)
    
def load_intermidiate_training_data():
    return pd.read_csv(INTERM_TRAIN_PATH)

def load_intermidiate_test_data():
    return pd.read_csv(INTERM_TEST_PATH)


def load_preprocessed_training_data():
    pass
    # return pd.read_csv(INTERM_TEST_PATH)


