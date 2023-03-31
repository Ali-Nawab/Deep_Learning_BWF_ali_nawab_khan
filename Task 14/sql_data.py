import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="elliot54102",
    database="game"
)

# SQL query to fetch the data from the database
query = "SELECT * FROM customer;"

# Load the data into a pandas DataFrame
df = pd.read_sql(query, conn)

# Close the database connection
conn.close()

# Print the loaded data
print(df)