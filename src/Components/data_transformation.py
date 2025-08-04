import os
import sys
import pandas as pd
import numpy as np
from dataclasses import dataclass

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.exception import CustomException
from src.util import load_object
from src.logger import logging

@dataclass
class DataTransformationConfig:
    preprocesor_object_file_path=os.path.join('artifacts',"preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.datatransformationconfig=DataTransformationConfig()

    def gat_data_transformation_object(self):
        try:
            numerical_columns=["year","selling_price","km_driven","engine","max_power","seats"]
            categorical_columns=["seller_type","transmission","owner"]
            num_pipeline=Pipeline(
                steps=[("imputer",SimpleImputer(strategy="median")),("scaler",StandardScaler())]
            )
            cat_pipeline=Pipeline(steps=[("imputer",SimpleImputer(strategy="most_frequent")),("one_hot_encoder",OneHotEncoder()),("scaler",StandardScaler(with_mean=False))])

            logging.info(f"Numerical columns: {numerical_columns}")
            logging.info(f"Categorical columns: {categorical_columns}")

            preprocessor=ColumnTransformer([("num_pipeline",num_pipeline,numerical_columns),("cat_pipelines",cat_pipeline,categorical_columns)])

            return preprocessor

        except Exception as  e:
            raise CustomException(e,sys)
    
    def initate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")
            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.gat_data_transformation_object()
            target_column_name="selling_price"

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(f"Applying preprocessing object on training dataframe and testing data frame")

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)
            train_arr = np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr,np.array(target_feature_test_df)]
            logging.info(f"Saved Preprocessing object")
            
            
        
        except Exception as e:
            raise CustomException(e,sys)
