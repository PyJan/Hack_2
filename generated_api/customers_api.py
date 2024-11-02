import sqlite3
import pandas as pd

def load_and_aggregate_customers_by_country(database_path):
    """
    Connects to the SQLite database, loads customer data from the 'customers' table,
    filters out customers without a company, and aggregates the data by country.
    
    Parameters:
    database_path (str): Path to the SQLite database file.
    
    Returns:
    pd.DataFrame: A DataFrame with the aggregated customer data by country.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)
    
    # Load customer data into a DataFrame
    query = "SELECT * FROM customers"
    df = pd.read_sql_query(query, conn)
    
    # Close the database connection
    conn.close()
    
    # Filter out customers without a company
    df_filtered = df[df['Company'].notna()]
    
    # Aggregate data by country
    df_aggregated = df_filtered.groupby('Country').agg(
        Total_Customers=('CustomerId', 'count'),
        Total_Companies=('Company', 'count')
    ).reset_index()
    
    return df_aggregated

# Sample call to the function
database_path = 'data/chinook.db'
result = load_and_aggregate_customers_by_country(database_path)
print(result)