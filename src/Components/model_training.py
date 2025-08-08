import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging

from src.utils import save_object,evaluate_models

@dataclass
class ModelTrainingConfig:
    trained_model_file_path=os.path.join("artifacts","models.pkl")

class ModelTraining:
    def __init__(self):
        self.Model_Training_Config=ModelTrainingConfig()

    def initiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and test info")
            X_train,Y_train,X_test,Y_test=(train_array[:,:-1],train_array[:,-1],test_array[:,:-1],test_array[:,-1])

            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "XGBRegressor": XGBRegressor(),
                "CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }

            model_report:dict=evaluate_models(X_train=X_train,X_test=X_test,y_test=Y_test,y_train=Y_train,models=models)
            best_model_score=max(sorted(model_report.values()))

            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model=models[best_model_name]

            if(best_model_score<0.6) :
                raise CustomException("no best model found")
            logging.info(f"Best found model on both train and test data")

            save_object(file_path=self.Model_Training_Config.trained_model_file_path,obj=best_model)
            predicted=best_model.predict(X_test)
            r2_square=r2_score(Y_test,predicted)
            return r2_square

        except Exception as e:
            raise CustomException(e,sys)
