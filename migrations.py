from etl import insert_to_Collections
from pymongo import MongoClient

client = MongoClient()

song_length_inserts = insert_to_Collections('Song_Length')
session_inserts = insert_to_Collections('Session')
song_listeners_inserts = insert_to_Collections('Song_listeners')

def mongo_query():
    dbnames = client.list_database_names()
    drop_database = client.drop_database('sparkifydb')
    sparkify = client['sparkifydb']
    print('Database created')
    
    song_length_col = sparkify['song_length']
    session_col = sparkify['session']
    song_listeners_col = sparkify['song_listeners']
    print('Collections Created')
    
    song_length_col.insert_many(song_length_inserts)
    session_col.insert_many(session_inserts)
    song_listeners_col.insert_many(song_listeners_inserts)
    print('Inserts completed')
    
def mongo_find_queries():
    get_lengths_query = """SELECT artist_name, song_title, song_len FROM song_length WHERE sessionId = 338 AND itemInSession = 4;"""

get_sessions_query = """SELECT artist_name, song_name, first_name, last_name FROM session_table WHERE userId = 10 AND sessionId = 182;"""

get_listeners_query = """SELECT first_name, last_name FROM song_listeners WHERE song = 'All Hands Against His Own';"""
    
    
    