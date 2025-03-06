
import pandas as pd
import sys
import os


from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split
from src.components.data_transformation import DataTransformation

class DataIngestion:
    def __init__(self):
        current_dir = os.path.dirname(os.getcwd())
        path = os.path.dirname(current_dir)
        self.artifacts_folder_path = os.path.join(path, 'artifacts')
        os.makedirs(self.artifacts_folder_path, exist_ok=True)
        self.raw_data_path = os.path.join(self.artifacts_folder_path,'data.csv')
        self.train_data_path = os.path.join(self.artifacts_folder_path,'train.csv')
        self.test_data_path = os.path.join(self.artifacts_folder_path,'test.csv')

        logging.info('Enter into the data ingestion')


    def initiate_data_ingestion(self):

        try:
            root_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            dataset_path = os.path.join(root_dir,'notebook/data/cleaned_data.csv')

            df = pd.read_csv(dataset_path)
            df.to_csv(self.raw_data_path,index=False)
            logging.info('The dataset as dataframe')

            logging.info('Train Test Split')
            train_data,test_data = train_test_split(df,test_size=0.2,random_state=42)


            train_data.to_csv(self.train_data_path,index=False,header=True)
            test_data.to_csv(self.test_data_path,index=False,header=True)
            logging.info('Data Ingestion is completed')

            return self.train_data_path,self.test_data_path




        except Exception as e:

            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = DataIngestion()
    train,test = obj.initiate_data_ingestion()
    train_array,test_array,preprocessor_path= DataTransformation().initiate_data_transformation(train,test)
