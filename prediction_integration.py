import pymysql
import numpy as np
import pandas as pd

def integrate_predictions(predictions_file, original_data_file):
    test_predict = np.load(predictions_file)
    df_sales_daily = pd.read_csv(original_data_file)

    connection = pymysql.connect(
        host='your-database-host',
        user='your-username',
        password='your-password',
        database='your-database'
    )

    with connection.cursor() as cursor:
        for i in range(len(test_predict)):
            date = df_sales_daily['ds'].iloc[int(len(df_sales_daily) * 0.8) + 30 + 1 + i]
            prediction = test_predict[i][0]
            sql = "INSERT INTO sales_forecast (date, prediction) VALUES (%s, %s)"
            cursor.execute(sql, (date, prediction))

    connection.commit()
    connection.close()

if __name__ == "__main__":
    integrate_predictions('test_predict.npy', 'sales_data_daily.csv')
