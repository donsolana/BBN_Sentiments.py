#import mysql.connector
import re
#from collections import Counter
import string
from bs4 import BeautifulSoup
#plt.style.use('fivethirtyeight')
import warnings
warnings.filterwarnings("ignore")


def clean_data(raw_data):
    def clean_text(text):
        text = BeautifulSoup(text, 'lxml').get_text()
        text = re.sub(r'@[A-Za-z0-9]+', '', text)
        text = re.sub(r'https?:\/\/\S+', '', text)
        text = re.sub(r'#', '', text)
        text = re.sub(r'RT[\s]+', '', text)
        text = re.sub("[^a-zA-Z]", ' ', text)
        return text
    
    raw_data["tweets"] = raw_data['Text'].apply(clean_text)
     
    return raw_data
    