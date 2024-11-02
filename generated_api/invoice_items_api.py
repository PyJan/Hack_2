import sqlite3
import pandas as pd

def load_and_aggregate_invoice_items(db_path, min_quantity, min_unit_price):
    """
    Load data from the invoice_items table, filter by minimum quantity and unit price,
    and aggregate the total sales amount per invoice.
    
    Parameters:
    db_path (str): Path to the SQLite database.
    min_quantity (int): Minimum quantity to filter the invoice items.
    min_unit_price (float): Minimum unit price to filter the invoice items.
    
    Returns:
    pd.DataFrame: Aggregated data with total sales amount per invoice.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    
    # Load data from the invoice_items table
    query = """
    SELECT InvoiceId, UnitPrice, Quantity
    FROM invoice_items
    WHERE Quantity >= ? AND UnitPrice >= ?
    """
    df = pd.read_sql_query(query, conn, params=(min_quantity, min_unit_price))
    
    # Calculate total sales amount for each invoice
    df['TotalAmount'] = df['UnitPrice'] * df['Quantity']
    
    # Aggregate total sales amount per invoice
    aggregated_df = df.groupby('InvoiceId')['TotalAmount'].sum().reset_index()
    
    # Close the database connection
    conn.close()
    
    return aggregated_df

# Sample call to the function
db_path = 'data/chinook.db'
min_quantity = 1
min_unit_price = 0.99
result = load_and_aggregate_invoice_items(db_path, min_quantity, min_unit_price)
print(result)