""" Script to generate sales report using SQL."""
import sqlite3

def main():
    con = sqlite3.connect('sales.db')
    cur = con.cursor()

    cur.execute('''
        SELECT c.customer_id, c.age, i.item_name, SUM(o.quantity)
        FROM Sales as s
        INNER JOIN (
            SELECT customer_id, age
            FROM Customer
            WHERE age >= 18 AND age <= 35
        ) AS c
        ON s.customer_id = c.customer_id
        INNER JOIN (
            SELECT sales_id, item_id, quantity
            FROM Orders
            WHERE quantity is not NULL
        ) as o
        ON s.sales_id = o.sales_id
        INNER JOIN Items as i
        ON o.item_id = i.item_id
        GROUP BY c.customer_id, i.item_id
    ''')

    headers = ['Customer', 'Age', 'Item', 'Quantity']
    data = cur.fetchall()
    with open('report_using_sql.csv', 'w') as f:
        f.writelines(
            '\n'.join([
                ';'.join(headers),
                *[';'.join([str(item) for item in row]) for row in data],
            ])
        )

if __name__ == '__main__':
    main()
