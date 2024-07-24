import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data():
    df_sales_daily = pd.read_csv('sales_data_daily.csv')
    test_predict = np.load('test_predict.npy')
    return df_sales_daily, test_predict

def plot_sales_forecast(df_sales_daily, test_predict):
    # 分割数据
    train_size = int(len(df_sales_daily) * 0.8)
    train = df_sales_daily.iloc[:train_size]
    test = df_sales_daily.iloc[train_size:]
    test = test.reset_index(drop=True)

    # 创建预测数据框
    test['Prediction'] = test_predict

    # 绘制图表
    plt.figure(figsize=(14, 7))
    plt.plot(train['ds'], train['y'], label='Train Sales')
    plt.plot(test['ds'], test['y'], label='Actual Sales')
    plt.plot(test['ds'], test['Prediction'], label='Predicted Sales')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.title('Sales Forecast')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)

def main():
    st.title('ERP AI Prediction Dashboard')
    st.write('This dashboard displays the sales forecast using LSTM model.')

    df_sales_daily, test_predict = load_data()
    plot_sales_forecast(df_sales_daily, test_predict)

if __name__ == "__main__":
    main()
