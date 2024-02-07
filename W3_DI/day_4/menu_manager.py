import psycopg2
from psycopg2 import sql
class MenuManager:
    def get_by_name(cls,item_name):
        with psycopg2.connect(
            dbname="your_database_name",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        ) as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM Menu_Items WHERE item_name = %s",
                    (item_name,)
                )
                result = cursor.fetchone()
                if result:
                    item_id, item_name, item_price = result
                    return (item_name, item_price)
                else:
                    return None
    def all_items(cls):
        with psycopg2.connect(
            dbname="your_database_name",
            user="your_username",
            password="your_password",
            host="your_host",
            port="your_port"
        ) as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM Menu_Items")
                items = []
                for item_id, item_name, item_price in cursor.fetchall():
                    items.append((item_name, item_price))
                return items
