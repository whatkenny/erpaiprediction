import pandas as pd

def preprocess_data(sales_file, stock_file):
    df_sales = pd.read_csv(sales_file)
    df_stock = pd.read_csv(stock_file)

    df_sales_daily = df_sales.groupby('ds').sum().reset_index()
    df_sales_daily = df_sales_daily.fillna(method='ffill')

    df_stock_daily = df_stock.groupby('date').sum().reset_index()
    df_stock_daily = df_stock_daily.fillna(method='ffill')

    return df_sales_daily, df_stock_daily

if __name__ == "__main__":
    df_sales_daily, df_stock_daily = preprocess_data('sales_data.csv', 'stock_data.csv')
    df_sales_daily.to_csv('sales_data_daily.csv', index=False)
    df_stock_daily.to_csv('stock_data_daily.csv', index=False)
