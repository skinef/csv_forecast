import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import io

def do_forecast():
    df = pd.read_csv('C://Users/pc/Desktop/Flask/myself/forecast_data.csv',index_col='sales_date',parse_dates=True)

    #train_data = df.iloc[:69] 
    #test_data = df.iloc[69:]

    ##mul = multiplicative , seasonal_period = row value in periods    
    final_model = ExponentialSmoothing(df['total_sales'],trend='mul',seasonal='mul',seasonal_periods=30).fit()

    ##Howmany period do you want forecast for the future.
    forecast_predictions = final_model.forecast(60)

    #train_data['total_sales'].plot(legend=True,label='TRAIN',figsize=(6,4))
    #test_data['total_sales'].plot(legend=True,label='TEST',figsize=(6,4))
    df['total_sales'].plot(legend=True,label='MAIN',figsize=(6,4))
    forecast_predictions.plot(legend=True,label='FORECAST_PREDICTION',figsize=(6,4))
    
    ##Here is for show on flask.
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image

