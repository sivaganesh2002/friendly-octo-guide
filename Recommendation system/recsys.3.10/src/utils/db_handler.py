from dotenv import load_dotenv
import pandas as pd
import os
import uuid

import psycopg2
from psycopg2.extras import execute_values

load_dotenv()

class DatabaseHandler:
    def __init__(self, db_url:str=os.environ.get("POST_DB_LINK")):
        """
            Initialize the DatabaseHandler with a connection to the PostgreSQL database.
        """
        self.connection = psycopg2.connect(db_url)
        self.connection.autocommit = True
    
    def close(self):
        """
            Close the database connection.
        """
        if self.connection:
            self.connection.close()

    def create_table(self, query:str):
        """
            Create a table in DB, table using a user query if it doesn't exist 
        """
        cursor = self.connection.cursor()
        cursor.execute(query)
        
        self.connection.commit()
        cursor.close()

    def retrieve_all(self, table_name:str) -> pd.DataFrame:
        """
            connect to DB
            retrieve all records from table `table_name`
        """
        try:
            cursor = self.connection.cursor()
            query = """
                sELECT column_name
                FROM information_schema.columns
                WHERE table_name = `{table_name}`
                ORDER BY original_position;
            """
            cursor.execute(query)
            columns = [row[0] for row in cursor.fetchall()]
            print(f"columns: {columns}  type: {type(columns)}")

            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()

            df = df.DataFrame(rows, columns=columns)
            return df

        except Exception as e:
            print(f"Error retrieving data from table {table_name}: {e}")
            return None
        
    def delete_table(self, table_name:str):
        """
            connect to DB
            delete table `table_name`
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(f"DROP TABLE IF EXISTS {table_name};")
            self.connection.commit()
            cursor.close()
            print(f"Table {table_name} deleted successfully.")
        except Exception as e:
            print("Error deleting table", table_name)

    def insert_data(self, df:pd.DataFrame, table_name):
        """
            insert data to populate table `table_name` from dataframe `df`
        """
        if df.empty():
            print("DataFrame is empty. No data to insert.")
            return

        try:
            cursor = self.connection.cursor()
            columns = list(df.columns)

            col_str = ', '.join(columns)
            placeholders = ', '.join(['%s'] * len(columns))
            query = f"insert into {table_name} ({col_str}) values ({placeholders})"

            data_tuple = []
            for _, row in df.iterrows():
                row = []
                for col in columns:
                    value = row[col]
                    if col == 'id' and hasattr(value, 'hex'):
                        row.append(str(value))
                    else:
                        row.append(value)

                data_tuple.append(tuple(row))

            cursor.executemany(query, data_tuple)
            self.connection.commit()
            cursor.close()
            print(f"Inserted {len(data_tuple)} records into {table_name} successfully.")

        except Exception as e:
            print(f"Error inserting data into table {table_name}: {e}")
            if 'cursor' in locals():
                cursor.close()
            
    def test_table(self, table_name:str):
        """
            Test if table `table_name` exists in the database
        """
        result = {
            'table_exists' : False,
            'table_has_data' : False
        }

        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                        select exists ()
                            select from information_schema.tables
                           where table_schema = 'public'
                           and table_name = %s
                );
            """, (table_name,))
            table_exists = cursor.fetchnone()[0]
            result['table_exists'] = table_exists

            if table_exists:
                cursor.execute(f"select count(*) from {table_name};")
                row_count = cursor.fetchnone()[0]
                result['table_has_data'] = row_count > 0
                print(f"Table '{table_name}': Exists={table_exists}, Has data={result['table_has_data']} ({row_count} rows)")
            else:
                print(f"Table '{table_name}': Does not exist")
            cursor.close()
            return result
        
        except Exception as e:
            print(f"Error testing table {table_name}: {e}")
            if 'cursor' in locals():
                cursor.close()
            return result
