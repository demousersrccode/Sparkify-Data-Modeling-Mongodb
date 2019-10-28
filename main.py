from migrations import *
from pymongo import MongoClient

client = MongoClient()

def main():
    mongo_query()
    
    client.close()
    
    
if __name__ == '__main__':
    main()