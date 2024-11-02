import sqlite3

def load_and_filter_aggregate_data_chinook_sequence(db_path, min_seq_value):
    """
    Loads data from the sqlite_sequence table, filters rows based on a minimum seq value,
    and aggregates the total count of sequences greater than the specified value.
    
    Args:
    db_path (str): Path to the SQLite database.
    min_seq_value (int): Minimum sequence value to filter the rows.
    
    Returns:
    dict: A dictionary with filtered data and the total count of sequences.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    query = "SELECT name, seq FROM sqlite_sequence WHERE seq > ?"
    cursor.execute(query, (min_seq_value,))
    
    filtered_data = cursor.fetchall()
    total_count = len(filtered_data)
    
    conn.close()
    
    return {
        "filtered_data": filtered_data,
        "total_count": total_count
    }

# Sample call to the function
result = load_and_filter_aggregate_data_chinook_sequence('data/chinook.db', 100)
print(result)