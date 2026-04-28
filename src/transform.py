import pandas as pd

def transform_data(df):
    # Remove null values
    df = df.dropna()

    # Convert date column
    df['order_date'] = pd.to_datetime(df['order_date'])

    # Create new column
    df['total_price'] = df['quantity'] * df['price']

    # Remove duplicates
    df = df.drop_duplicates()

    print("✅ Data Transformed")
    return df