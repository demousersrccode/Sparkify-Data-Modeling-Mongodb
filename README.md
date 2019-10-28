# Sparkify-Data-Modeling-Mongodb

## Summary

This project aims to model data to a NoSQL analytics database using MongoDB for a fictional music streaming service called Sparkify

## Overview
### Use-Case

Sparkify's analytics team seeks to understand what, when and how users are playing songs on the company's music app. The analysts need an easy way to query and analyze the songplay data, which is currently stored in raw csv files on a local directory.

As the data engineer assigned to the project, My main-task is to implement an ETL pipeline in python to pre-process the data using pandas. The database tables are modeled on the queries according to the principle of one table per query. I selected the primary and clustering keys for each table in order to ensure a unique identifier for each row.  

This project was initially carried out in Cassandra by Udacity for its data engineering class as a project; but i intend on using a MongoDB variant / approach.


# Pre-requisite Softwares
> ***Python 3.5 +***
 
 > ***PostgreSQL***
 
>  ***Pymongo*** (*through pip installer package => Mongo Client for python)
 
>  ***Pandas*** (*through pip installer package)
 
> ***Numpy*** (*through pip installer package)
 
>  ***JupyterLab*** (*through pip installer package)


# File Structure
```bash
├──── Event_data =>: (FOLDER)
│     │
│     └─ {.json}
│
├───── etl.py =>: (etl.py iterates through the event_data directory and then returns both a csv file and a dictionary of all the extracted data)
├───── migrations.py =>: (migrations.py inserts and executes the data output of etl.py file to the queries from sql_queries)
├───── main.py =>: (main.py is the starting point for execution for this project)
├───── test.ipynb =>: (test.ipynb is basically a notebook where queries can be tested and executed)
├───── README.md
└───── .gitignore
```

# Execution Steps

To begin execution, cd to the directory where main.py resides and run the following command on terminal

> <code> python main.py </code> 
    
The following occurs if the script executed successfully without any hassle.

1.) The database **sparkifydb** will be created

2.) The collections **song_length**, **session** and **song_listeners** will be included into the database

3.) The script will query the database to check if the data are in the database

<p>
    
    More info on the project can be viewed on the test.ipynb notebook. 

</p>