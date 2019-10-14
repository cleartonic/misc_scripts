# -*- coding: utf-8 -*-
"""
@author: cleartonic
"""

import pandas as pd
import numpy as np



def process():
    df = pd.read_csv('row_log.txt',sep='|')
    df['char_attacked'] = ''
    hp1 = 29
    hp2 = 215
    hp3 = 177
    hp4 = 23
    
    row_array = []
    for i, r in df.iterrows():
        data = df.iloc[i]
        if data[0] != hp1:
            row_array.append(1)
        elif data[1] != hp2:
            row_array.append(2)
        elif data[2] != hp3:
            row_array.append(3)
        elif data[3] != hp4:
            row_array.append(4)
        else:
            row_array.append('miss')
            
    df['char_attacked'] = row_array
    df['count'] = 1
    df = df.pivot_table(index='char_attacked',values='count',aggfunc='sum')
    df.to_csv('latest_run.csv')
    return df

df = process()