import os 
import sys

import numpy as np
import pandas as pd
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.exception import CustomException

def save_object(file_path, obj): #1
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)


def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}
        best_models = {}

        for model_name, model in models.items():

            para = params[model_name]

            grid_search = GridSearchCV(model,para,cv=5,scoring="r2",n_jobs=-1,error_score="raise")

            grid_search.fit(X_train, y_train)
            best_models[model_name] = grid_search.best_estimator_

            print(f"{model_name} Best Parameters: {grid_search.best_params_}")
            print(f"{model_name} Best CV Score: {grid_search.best_score_}")

            y_train_pred = grid_search.predict(X_train)
            y_test_pred = grid_search.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)

            report[model_name] = test_model_score

        return report,best_models

    except Exception as e:
        raise CustomException(e, sys)