""" Script to setup the database and tables necessary for the project."""
import sqlite3


def main():
    con = sqlite3.connect('sales.db')
    cur = con.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Customer(
            customer_id int NOT NULL PRIMARY KEY,
            age int NOT NULL
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Sales(
            sales_id int NOT NULL PRIMARY KEY,
            customer_id int NOT NULL
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Items(
            item_id int NOT NULL PRIMARY KEY,
            item_name varchar(255) NOT NULL
        )
    ''')
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Orders(
            order_id int NOT NULL PRIMARY KEY,
            sales_id int NOT NULL,
            item_id int NOT NULL,
            quantity int
        )
    ''')

    con.commit()


if __name__ == '__main__':
    main()
