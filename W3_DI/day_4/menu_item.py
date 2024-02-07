import psycopg2
from psycopg2 import sql

class MenuItem:
    def __init__(self,item_name,item_price=0):
        self.item_name=item_name
        self.item_price=item_price
    def __str__(self):
        return f"Item:{self.item_name},{self.item_price}"
    def save(self):
        with psycopg2.connect(
            dbname="your_database_name",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
            )as conn:
            with conn.cursor as cursor:
                 cursor.execute(
                    "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s) RETURNING item_id",
                    (self.item_name, self.item_price)
                )
            self.item_id = cursor.fetchone()[0]
    def delete(self):
         with psycopg2.connect(
            dbname="your_database_name",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        ) as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "DELETE FROM Menu_Items WHERE item_id = %s",
                    (self.item_id,)
                )
    def update(self, new_name=None, new_price=None):
        with psycopg2.connect(
            dbname="your_database_name",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        ) as conn:
            with conn.cursor() as cursor:
                update_query = "UPDATE Menu_Items SET"
                update_values = []

                if new_name is not None:
                    update_query += " item_name = %s,"
                    update_values.append(new_name)

                if new_price is not None:
                    update_query += " item_price = %s,"
                    update_values.append(new_price)

                if not update_values:
                    # Nothing to update
                    return

                update_query = update_query.rstrip(',') + " WHERE item_id = %s"
                update_values.append(self.item_id)
                cursor.execute(update_query, update_values)

