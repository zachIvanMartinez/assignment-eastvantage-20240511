""" Script to add test data to the sales db."""
import sqlite3

def main():
    con = sqlite3.connect('sales.db')
    cur = con.cursor()

    customer_data = [
        {'customer_id': 1, 'age': 21},
        {'customer_id': 2, 'age': 23},
        {'customer_id': 3, 'age': 35},
        {'customer_id': 4, 'age': 17},
    ]
    cur.executemany('''
        INSERT INTO Customer VALUES (:customer_id, :age)
    ''', customer_data)

    items_data = [
        {'item_id': 1, 'item_name': 'x'},
        {'item_id': 2, 'item_name': 'y'},
        {'item_id': 3, 'item_name': 'z'},
    ]
    cur.executemany('''
        INSERT INTO Items VALUES (:item_id, :item_name)
    ''', items_data)

    sales_data = [
        {'sales_id': 1, 'customer_id': 1},
        {'sales_id': 2, 'customer_id': 1},
        {'sales_id': 3, 'customer_id': 1},
        {'sales_id': 4, 'customer_id': 1},
        {'sales_id': 5, 'customer_id': 2},
        {'sales_id': 6, 'customer_id': 2},
        {'sales_id': 7, 'customer_id': 2},
        {'sales_id': 8, 'customer_id': 3},
        {'sales_id': 9, 'customer_id': 3},
        {'sales_id': 10, 'customer_id': 1},
        {'sales_id': 11, 'customer_id': 4},
    ]
    cur.executemany('''
        INSERT INTO Sales VALUES (:sales_id, :customer_id)
    ''', sales_data)

    orders_data = [
        {'order_id': 1, 'sales_id': 1, 'item_id': 1, 'quantity': 1},
        {'order_id': 2, 'sales_id': 2, 'item_id': 1, 'quantity': 2},
        {'order_id': 3, 'sales_id': 3, 'item_id': 1, 'quantity': 3},
        {'order_id': 4, 'sales_id': 4, 'item_id': 1, 'quantity': 4},
        {'order_id': 5, 'sales_id': 5, 'item_id': 1, 'quantity': 1},
        {'order_id': 6, 'sales_id': 6, 'item_id': 2, 'quantity': 1},
        {'order_id': 7, 'sales_id': 7, 'item_id': 3, 'quantity': 1},
        {'order_id': 8, 'sales_id': 8, 'item_id': 3, 'quantity': 1},
        {'order_id': 9, 'sales_id': 9, 'item_id': 3, 'quantity': 1},
        {'order_id': 10, 'sales_id': 10, 'item_id': 2, 'quantity': None},
        {'order_id': 11, 'sales_id': 11, 'item_id': 2, 'quantity': 5},
    ]
    cur.executemany('''
        INSERT INTO Orders VALUES (:order_id, :sales_id, :item_id, :quantity)
    ''', orders_data)

    con.commit()


if __name__ == '__main__':
    main()
