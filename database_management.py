```python
import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
        self.connection.execute(query)

    def insert_data(self, table_name, data):
        placeholders = ', '.join(['?' for _ in range(len(data))])
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        self.connection.execute(query, data)
        self.connection.commit()

    def select_data(self, table_name, columns=None):
        if columns:
            query = f"SELECT {', '.join(columns)} FROM {table_name}"
        else:
            query = f"SELECT * FROM {table_name}"
        cursor = self.connection.execute(query)
        return cursor.fetchall()

    def update_data(self, table_name, column, value, condition):
        query = f"UPDATE {table_name} SET {column} = ? WHERE {condition}"
        self.connection.execute(query, (value,))
        self.connection.commit()

    def delete_data(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.connection.execute(query)
        self.connection.commit()
```
