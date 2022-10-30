import logging

import pandas as pd
import json
#import mysql.connector
import re
#from collections import Counter
import string
#plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings("ignore")
from preprocess import clean_data
from transformers import pipeline
import torch
from predict import predict
from get_data import get_data


def main():
    logging.info('App Start')
    
    raw_data =  pd.read_csv('https://github.com/Crownthirst/Big_brother_naija/blob/main/bbn_tweets.csv')
    print('file read!')
    logging.info('File Read')

    proc_data = clean_data(raw_data)
    print('Data Cleaned!')
    logging.info('File Read')

    # Make prediction using model loaded from disk as per the data.
    final_data = predict(proc_data)
    print("Sentiment Analysed!")
    logging.info('Sentiment Analysed')
    
    return final_data


table =  main()
table.to_csv('bbn_tweets.csv')
print("finished!!")
