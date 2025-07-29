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
            numerical_columns={}
            categorical_columns={}
        except Exception as  e:
            raise CustomException(e,sys)
    