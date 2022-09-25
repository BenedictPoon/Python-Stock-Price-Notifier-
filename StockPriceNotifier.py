import pandas as pd
from alpha_vantage.techindicators import TechIndicators
import matplotlib.pyplot as plt

api_key = 'RNZPXZ6Q9FEFMEHM'

period = 60

ti = TechIndicators(key=api_key, output_format='pandas')

data_ti, meta_data_ti = ti.get_stochrsi(symbol='MSFT', interval='1min',
                                    time_period=period, series_type='close')
data_wma, meta_data_wma = ti.get_wma(symbol='MSFT', interval='1min',
                                    time_period=period, series_type='close')

print(data_ti)
print(data_wma)

