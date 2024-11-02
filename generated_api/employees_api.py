import sqlite3
import pandas as pd

def load_and_aggregate_employees_data_from_chinook_db(db_path='data/chinook.db'):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    
    # Load data from the employees table
    query = "SELECT * FROM employees"
    df = pd.read_sql_query(query, conn)
    
    # Close the connection
    conn.close()
    
    # Filter employees who are Sales Support Agents
    sales_support_agents = df[df['Title'] == 'Sales Support Agent']
    
    # Aggregate data: count of employees per city
    city_employee_count = sales_support_agents.groupby('City').size().reset_index(name='EmployeeCount')
    
    return city_employee_count

# Sample call to the function
result = load_and_aggregate_employees_data_from_chinook_db()
print(result)