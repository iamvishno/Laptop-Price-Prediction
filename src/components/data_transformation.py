import os
import pickle

import pandas as pd
import numpy as np
import sys


from src.logger import logging
from src.exception import CustomException
#from src.components.data_ingestion import DataIngestion
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.impute import SimpleImputer

class DataTransformation:

    def __init__(self):

        self.preprocessor = self.get_data_transformer_obj()
        current_dir = os.path.dirname(os.getcwd())
        path = os.path.dirname(current_dir)
        self.artifacts_folder_path = os.path.join(path, 'artifacts')
        os.makedirs(self.artifacts_folder_path, exist_ok=True)
        self.preprocessor_path = os.path.join(self.artifacts_folder_path,'preprocessor.pkl')


        logging.info('Data Transformation is started')


    @staticmethod
    def get_data_transformer_obj():

        try:
            numerical_features = ['Inches', 'Ram(GB)', 'SSD', 'HDD', 'TouchScreen', 'Ips_display', 'PPI']
            categorical_features = ['Company', 'TypeName', 'Cpu(processor)', 'Gpu(I,N,A)Brand', 'OS']

            num_pipe = Pipeline([('MissingValues', SimpleImputer(strategy='mean')),
                                 ('Scaling', StandardScaler())
                                 ])
            logging.info(f'Numerical Pipeline Created {numerical_features}')
            cat_pipe = Pipeline([('MissingValues', SimpleImputer(strategy='most_frequent')),
                                 ('onehot',OneHotEncoder(sparse_output=False, drop='first', handle_unknown='ignore'))])
            logging.info(f'Categorical Pipeline Created {categorical_features}')
            preprocessor = ColumnTransformer([('Numerical_pipeline', num_pipe, numerical_features),
                                              ('Categorical_pipeline', cat_pipe, categorical_features)
                                              ])
            return preprocessor

        except Exception as e:
            raise CustomException(e,sys)


    def initiate_data_transformation(self,train_path,test_path):

        try:

            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info('Read train and test data completed')



            target_column = 'Price'
            input_train_df = train_df.drop(target_column,axis=1)
            target_column_input_train_df = train_df[target_column]

            input_test_df = test_df.drop(target_column,axis=1)
            target_column_input_test_df = test_df[target_column]

            logging.info("Performing the preprocessing on the train and test data")

            input_train_array = self.preprocessor.fit_transform(input_train_df)
            input_test_array = self.preprocessor.transform(input_test_df)

            train_array = np.c_[input_train_array,np.array(target_column_input_train_df)]
            test_array = np.c_[input_test_array,np.array(target_column_input_test_df)]

            with open(self.preprocessor_path,'wb') as f:
                pickle.dump(self.preprocessor,f)
            logging.info('Saved preprocessor as pickle file preprocessor.pkl')

            return train_array,test_array,self.preprocessor_path




        except Exception as e:
            raise CustomException(e,sys)

'''obj1 = DataIngestion()
train,test = obj1.initiate_data_ingestion()
obj = DataTransformation()
obj.initiate_data_transformation(train,test)'''
