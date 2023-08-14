# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 22:20:02 2023

@author: arnav
"""

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def gordon_growth_model(ticker):
    # Define the expected market return (can be adjusted based on your preferences)
    market_return = 0.08

    # Get the historical stock data using yfinance
    stock_data = yf.download(ticker, start=datetime(2010, 1, 1), end=datetime.now())

    # Calculate the annual dividend growth rate
    if 'Dividends' in stock_data.columns:
        stock_data['Div_Growth'] = stock_data['Dividends'].pct_change()
        avg_div_growth_rate = stock_data['Div_Growth'].mean()
        latest_dividend = stock_data.iloc[-1]['Dividends']
    else:
        # If 'Dividends' data is not available, estimate the latest dividend as the last closing price
        avg_div_growth_rate = 0.0
        latest_dividend = stock_data.iloc[-1]['Close']

    # Get the required rate of return using the Capital Asset Pricing Model (CAPM)
    risk_free_rate = 0.03  # The risk-free rate (can be adjusted based on your preferences)
    beta = 1.2  # The beta of the stock (can be adjusted based on your preferences)

    required_rate_of_return = risk_free_rate + beta * (market_return - risk_free_rate)

    # Calculate the Gordon Growth Model value
    predicted_value = latest_dividend / (required_rate_of_return - avg_div_growth_rate)

    return predicted_value

 

