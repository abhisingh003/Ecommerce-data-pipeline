import sqlite3

def load_to_db(df):
    conn = sqlite3.connect("ecommerce.db")
    df.to_sql("orders", conn, if_exists="replace", index=False)
    conn.close()
    print("✅ Data Loaded into DB")

def save_parquet(df):
    df.to_parquet("output/clean_data.parquet", index=False)
    print("✅ Saved as Parquet")