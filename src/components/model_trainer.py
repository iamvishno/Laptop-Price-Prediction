import os
import pickle
import sys


from src.exception import CustomException
from src.logger import logging
from sklearn.linear_model import LinearRegression,Ridge,Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import r2_score
from src.utils import evalute_models
from sklearn.model_selection import GridSearchCV


class ModelTrainer:
    def __init__(self):
        current_dir = os.path.dirname(os.getcwd())
        path = os.path.dirname(current_dir)
        self.artifacts_folder_path = os.path.join(path, 'artifacts')
        os.makedirs(self.artifacts_folder_path, exist_ok=True)
        self.model_path = os.path.join(self.artifacts_folder_path, 'model.pkl')

    def initiate_model_trainer(self,train_array, test_array):
        try:
            logging.info('Train Test split')
            X_train,y_train,X_test,y_test = (train_array[:,:-1],train_array[:,-1],test_array[:,:-1],test_array[:,-1])

            models = {
                'LinearRegression': LinearRegression(),
                'Lasso': Lasso(),
                'Ridge': Ridge(),
                'DecisionTreeRegressor': DecisionTreeRegressor(),
                'AdaBoostRegressor': AdaBoostRegressor(),
                'RandomForestRegressor': RandomForestRegressor(),
                'Support Vector Regressor': SVR(),
                'K-Nearest Neighbors Regressor': KNeighborsRegressor(),

            }
            params = {
                'LinearRegression': {},

                'Lasso': {
                    'alpha': [0.01, 0.1, 1, 10]
                },

                'Ridge': {
                    'alpha': [0.01, 0.1, 1, 10]
                },

                'DecisionTreeRegressor': {
                    'max_depth': [None, 10, 20, 30],
                    'min_samples_split': [2, 5, 10],
                    'min_samples_leaf': [1, 2, 4]
                },

                'AdaBoostRegressor': {
                    'n_estimators': [50, 100, 200],
                    'learning_rate': [0.01, 0.1, 1]
                },

                'RandomForestRegressor': {
                    'n_estimators': [50, 100, 200],
                    'max_depth': [None, 10, 20, 30],
                    'min_samples_split': [2, 5, 10],
                    'min_samples_leaf': [1, 2, 4]
                },

                'Support Vector Regressor': {
                    'C': [0.1, 1, 10, 100],
                    'kernel': ['linear', 'poly', 'rbf', 'sigmoid']
                },

                'K-Nearest Neighbors Regressor': {
                    'n_neighbors': [3, 5, 7, 9],
                    'weights': ['uniform', 'distance']
                },


            }

            report:dict = evalute_models(X_train=X_train,y_train=y_train,X_test=X_test,y_test = y_test,models=models)# params
            best_r2_score = max(report.values()) ## best r2 score

            best_model_name = ''
            for key, val in report.items():
                if val == best_r2_score:
                    best_model_name = best_model_name + key



            best_model = models[best_model_name]


            logging.info('Best Model Found by doing training and testing the data')

            with open(self.model_path,'wb') as file:
                pickle.dump(best_model,file)

            logging.info(f'Model saved as pickle file Model.pkl {best_model}')
            predicted = best_model.predict(X_test)
            r2_square = r2_score(y_test,predicted)
            return r2_square  ## or we can direct return best_r2_score here.


        except Exception as e:
            raise CustomException(e,sys)

