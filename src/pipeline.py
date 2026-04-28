from extract import extract_data
from transform import transform_data
from load import load_to_db, save_parquet

def run_pipeline():
    df = extract_data("data/raw_data.csv")
    df = transform_data(df)
    load_to_db(df)
    save_parquet(df)

if __name__ == "__main__":
    run_pipeline()