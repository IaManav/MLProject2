import sys
import pandas as pd

from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path='artifacts/model.pkl'
            preprocessor_path='artifacts/preprocessor.pkl'

            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("after loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)

            return preds
        except Exception as e:
            raise CustomException(e,sys)
    
class Custom_Data:
    def __init__(self,year:int,selling_price:int,km_driven:int,fuel:str,seller_type:str,transmission:str,owner:str,mielage:str,engine:int,max_power:int,seats:int):
        self.year=year
        self.selling_price=selling_price
        self.km_driven=km_driven
        self.fuel=fuel
        self.seller_type=seller_type
        self.transmission=transmission
        self.owner=owner
        self.mielage=mielage
        self.engine=engine
        self.max_power=max_power
        self.seats=seats

    def get_data_as_dataframe(self):
        try:
            Custom_Data_input_dict={
                "year":[self.year],
                "selling_price":[self.selling_price],
                "km_driven":[self.km_driven],
                "fuel":[self.fuel],
                "seller_type":[self.seller_type],
                "transmission":[self.transmission],
                "owner":[self.owner],
                "mielage":[self.mielage],
                "engine":[self.engine],
                "max_power":[self.max_power],
                "seats":[self.seats],
            }

            return pd.DataFrame(Custom_Data_input_dict)
            
        except Exception as e:
            raise CustomException(e,sys)