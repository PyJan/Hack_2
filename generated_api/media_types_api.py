import sqlite3

def load_and_filter_media_types(db_path, filter_keyword):
    """
    Loads data from the media_types table in the specified SQLite database,
    filters rows based on the provided keyword, and returns the filtered data.
    
    Parameters:
    db_path (str): Path to the SQLite database file.
    filter_keyword (str): Keyword to filter the media types by name.
    
    Returns:
    list of tuples: Filtered rows from the media_types table.
    """
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    query = "SELECT * FROM media_types WHERE Name LIKE ?"
    cursor.execute(query, ('%' + filter_keyword + '%',))
    
    filtered_data = cursor.fetchall()
    
    conn.close()
    
    return filtered_data

# Sample call to the function
filtered_media_types = load_and_filter_media_types('data/chinook.db', 'audio')
print(filtered_media_types)