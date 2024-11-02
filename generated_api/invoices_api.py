import sqlite3
import pandas as pd

def load_filtered_aggregated_invoices_by_country(db_path, min_total, start_date, end_date):
    """
    Load invoices from the SQLite database, filter by minimum total and date range, 
    and aggregate the total amount by country.
    
    Parameters:
    db_path (str): Path to the SQLite database.
    min_total (float): Minimum total amount to filter invoices.
    start_date (str): Start date for filtering invoices (inclusive).
    end_date (str): End date for filtering invoices (inclusive).
    
    Returns:
    pd.DataFrame: Aggregated total amount by country.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    
    # SQL query to filter and aggregate invoices
    query = f"""
    SELECT BillingCountry, SUM(Total) as TotalAmount
    FROM invoices
    WHERE Total >= {min_total} AND InvoiceDate BETWEEN '{start_date}' AND '{end_date}'
    GROUP BY BillingCountry
    ORDER BY TotalAmount DESC;
    """
    
    # Execute the query and load the data into a DataFrame
    df = pd.read_sql_query(query, conn)
    
    # Close the database connection
    conn.close()
    
    return df

# Sample call to the function
db_path = 'data/chinook.db'
min_total = 5.0
start_date = '2009-01-01'
end_date = '2011-12-31'

result = load_filtered_aggregated_invoices_by_country(db_path, min_total, start_date, end_date)
print(result)