import os
import sys
import pandas as pd
import numpy as np
from src.exception import CustomException
from sklearn.metrics import r2_score
from src.logger import logging

def evalute_models(X_train,y_train,X_test,y_test,models):
    try:
        report = { }
        for i in range(len(models.values())):
            model = list(models.values())[i]


            model.fit(X_train,y_train) #Fit and training the data to the different models

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_r2score = r2_score(y_train,y_train_pred)
            test_r2score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] = test_r2score


        return report
    except Exception as e:
        raise CustomException(e,sys)





