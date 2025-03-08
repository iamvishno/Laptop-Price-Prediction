import sys
import os

import numpy as np
from send2trash.util import preprocess_paths

from src.exception import  CustomException
import pandas as pd
import pickle

from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:

            model_path = 'artifacts/model.pkl'
            preprocess_path = 'artifacts/preprocessor.pkl'
            with open(model_path, 'rb') as file:
                model = pickle.load(file)
            with open(preprocess_path, 'rb') as file:
                preprocessor = pickle.load(file)



            data_scaled = preprocessor.transform(features)
            preds = model.predict(data_scaled)
            output = np.exp(preds)
            return output[0]
        except Exception as e:
            raise CustomException(e,sys)






class CustomData:
    def __init__(self,
                 Company:str,TypeName:str,Inches: float,Ram:int,Cpu:str,Gpu:str,
                 SSD:str,HDD:str,TouchScreen:int,Ips_display:int,Os:str,Resolution:str):
        self.Company = Company,
        self.TypeName = TypeName,
        self.Inches = Inches,
        self.Ram = Ram,
        self.Cpu = Cpu,
        self.Gpu = Gpu,
        self.SSD = SSD,
        self.HDD = HDD,
        self.TouchScreen = TouchScreen,
        self.Ips_display = Ips_display,
        self.Os = Os,
        self.Resolution = Resolution



    def get_data_as_df(self):
        try:
            dict_input_data = {"Company":[self.Company[0]],
                               "TypeName":[self.TypeName[0]],
                               "Inches":[self.Inches[0]],
                               "Ram(GB)":[self.Ram[0]],
                               "Cpu(processor)":[self.Cpu[0]],
                               "Gpu(I,N,A)Brand":[self.Gpu[0]],
                               "SSD":[self.SSD[0]],
                               "HDD":[self.HDD[0]],
                               "TouchScreen":[self.TouchScreen[0]],
                               'Ips_display':[self.Ips_display[0]],
                               'OS':[self.Os[0]],
                               }
            df = pd.DataFrame(dict_input_data)
            X_res,Y_res = self.Resolution.split('x')[0],self.Resolution.split('x')[1]
            PPI = np.sqrt(int(X_res)**2+int(Y_res)**2)/self.Inches
            df['PPI'] = PPI
            return df
        except Exception as e:
            raise CustomException(e,sys)