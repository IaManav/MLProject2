import sys
import os
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.exception import CustomEception
from src.logger import logging

@dataclass
class DataInjestionConfig:
    train_data_path:str=os.path.join("artifacts","train.csv")
    test_data_path:str=os.path.join("artifacts","test.csv")
    raw_data_path:str=os.path.join("artifacts","data.csv")

class DataInjestion:
    def __init__(self):
        self.injestionconfig=DataInjestionConfig()
    
    def initiate_data_conf(self):
        logging.info("Entered data injestion")
        try:
            df=pd.read_csv("notebook/data/used_cars.csv")
            logging.info("Read the dataset as dataframe")
            os.makedirs(os.path.dirname(self.injestionconfig.train_data_path),exist_ok=True)

            logging.info("train_test_split initiated")
            train_set,test_set=train_test_split(df,random_state=20,test_size=0.22)
            train_set.to_csv(self.injestionconfig.train_data_path,index=False,header=True)
            test_set.to_csv(self.injestionconfig.test_data_path,index=False,header=True)

            logging.info("Ingestion of data is complete")

            return{
                self.injestionconfig.train_data_path,
                self.injestionconfig.test_data_path
            }
        except Exception as e:
            raise CustomEception(e,sys)



