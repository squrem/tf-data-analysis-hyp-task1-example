import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 434559054 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.04         
    nobs = np.array([x_cnt, y_cnt])
    count = np.array([x_success, y_success])
    res = proportions_ztest(count, nobs, alternative = 'larger')[1]
    if (res <= alpha): 
        return True
    else:
        return False
