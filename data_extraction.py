import pyodbc
import pandas as pd

def extract_data():
    # 连接 MSSQL 数据库
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=sg-analyzer2007;'
        'DATABASE=O2MicroDW;'
        'UID=AI;'
        'PWD=AIQQm2$yX'
        'Encrypt=no;'
        'TrustServerCertificate=yes;'
        'Connection Timeout=30;'
    )
    # FCST
    query_sales = "SELECT convert(varchar(7),fcstdate,120) as FCSTDate,a.SalesId, b.salesname,Qty,amount \
              FROM vSalesFcstCSD a \
              left join vKeyAccountCurrentQ b \
              on a.customerid=b.customerid and a.salesId=b.salesid and a.customergrp = b.customergrp \
              where fcstdate between '2024-06-01' and '2024-06-30'"
    df_sales = pd.read_sql(query_sales, connection)
    
    connection.close()

    df_sales['FCSTDate'] = pd.to_datetime(df_sales['FCSTDate'])
    df_sales = df_sales.rename(columns={'FCSTDate': 'ds', 'amount': 'y'})

    return df_sales

if __name__ == "__main__":
    df_sales = extract_data()
    df_sales.to_csv('sales_data.csv', index=False)
