import pandas as pd
import time

# Load datasets
def load_data(sell_path, rent_path):
    sell_df = pd.read_csv(sell_path)
    rent_df = pd.read_csv(rent_path)
    return sell_df, rent_df

# Display function
def display_data(df, title):
    print(f"Displaying {title} Listings:")
    for index, row in df.iterrows():
        print(f"{row['created_on']} | {row['property_type']} in {row['place_name']} | Price: {row['price']} {row['currency']}")

# Main orchestration function
def orchestrate_pipeline(sell_path, rent_path):
    sell_df, rent_df = load_data(sell_path, rent_path)
    while True:
        display_data(sell_df, "Sell")
        display_data(rent_df, "Rent")

if __name__ == "__main__":
    sell_path = 'data/properati-real-estate-listings-brazil/original/properati-BR-2016-11-01-properties-sell.csv'
    rent_path = 'data/properati-real-estate-listings-brazil/original/properati-BR-2016-11-01-properties-rent.csv'
    orchestrate_pipeline(sell_path, rent_path)
