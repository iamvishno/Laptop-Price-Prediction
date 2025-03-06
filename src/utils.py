import os
import sys
import pandas as pd
import numpy as np
from src.exception import CustomException

def save_prep(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)

    except Exception as e:
        raise CustomException(e,sys)