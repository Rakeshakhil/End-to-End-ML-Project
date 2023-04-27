import pandas as pd
import numpy as np
import pymongo
import json

from pymongo.mongo_client import MongoClient
# Create a new client and connect to the server
client =pymongo.MongoClient("mongodb+srv://Rakesh:Rakesh26@cluster0.vj4c6b7.mongodb.net/?retryWrites=true&w=majority")

# Create a new client and connect to the server


# Send a ping to confirm a successful connection
#try:
    #client.admin.command('ping')
    #print("Pinged your deployment. You successfully connected to MongoDB!")
#except Exception as e:
    #print(e)
#Creating a database in MongoDB
Data_file_path=(r'C:\Users\rakei\OneDrive\Desktop\End to End ML Project\End-to-End-ML-Project\insurance.csv')
Database_name='Insurance'
collection_name='Insurance_Project'


if __name__=='__main__':
    df=pd.read_csv(Data_file_path)
    print(f'Rows and columns:{df.shape}')
    
    df.reset_index(drop=True,inplace=True)
    
#Since we are using MongoDb we need to transform the excel into a dictionary(json format)   
    json_str = df.T.to_json()
    json_obj = json.loads(json_str)
    json_record = list(json_obj.values())
    print(json_record[0])
#Insert a all the rows to database in MongoDB
    client[Database_name][collection_name].insert_many(json_record)