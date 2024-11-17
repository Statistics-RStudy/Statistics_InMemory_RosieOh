import pandas as pd
import numpy as np


# 테스트 데이터
def analyze_data():
    data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Scores': [85, 90, 78]}
    df = pd.DataFrame(data)
    mean_score = df['Scores'].mean()
    result = {
        'average_score': mean_score,
        'data': df.to_dict(orient='records')
    }
    return result