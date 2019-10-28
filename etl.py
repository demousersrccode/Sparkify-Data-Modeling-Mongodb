# Loads Sparkifydb collections
import os
import glob
import pandas as pd
from pymongo import MongoClient

client = MongoClient()
filepath = 'event_data/'
filename = 'event_datafile_new.csv'

# Remove Jupyter's .ipynb checkpoints
os.system('rm -rf event_data/.ipynb_checkpoints')

def process_csv_path(filepath):
    """
    get all files matching .json extension from file path
    """
    all_csv_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.csv'))
        for csv in files:
            all_csv_files.append(os.path.abspath(csv))
    return all_csv_files


def get_data():
    """
    Returns a csv file
    """
    all_datasets = process_csv_path(filepath)
    full_data_rows_list = []
    
    for index in all_datasets:
        df = pd.read_csv(index)
        df.drop(['auth', 'method', 'page', 'registration', 'status', 'ts'], axis=1, inplace=True)
        df.dropna(inplace=True)
        data = df.values.tolist()
        full_data_rows_list.append(data)
        
    cols = ['artist','firstName','gender','itemInSession','lastName','length','level','location','sessionId','song','userId']
    header = True
    for aa in full_data_rows_list:
        df1 = pd.DataFrame.from_records(aa, columns = cols)
        df1.to_csv('event_datafile_new.csv', encoding='utf-8', mode='a', header=header, index=False)
        header = False

        
def return_a_csv():
    if os.path.exists(filename):
        os.remove(filename)
        return get_data()
    else:
        return get_data()
    
# Insert Data Into Collections
def insert_to_Collections(collection_name):
    return_a_csv()
    data = pd.read_csv(filename)
# Song_length = sessionId, artist, itemInSession, song, length
    if collection_name == 'Song_Length':
        song_len = [data[['sessionId', 'artist', 'itemInSession', 'song', 'length']].to_dict('list')]
        return song_len
    
# Session = userId, sessionId, song, itemInSession, artist, firstName, lastName
    if collection_name == 'Session':
        sess = [data[['userId', 'sessionId', 'song', 'itemInSession', 'artist', 'firstName', 'lastName']].to_dict('list')]
        return sess
        
# Song_listeners = song, firstName, lastName, userId
    if collection_name == 'Song_listeners':
        song_listnr = [data[['song', 'firstName', 'lastName', 'userId']].to_dict('list')]
        return song_listnr