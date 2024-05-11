""" Script to generate sales report using Pandas."""
import sqlite3
import pandas as pd

def main():
    con = sqlite3.connect('sales.db')

    customer_df = _read_customer(con)
    orders_df = _read_orders(con)
    items_df = _read_items(con)
    sales_df = _read_sales(con)

    joined_df = (
        sales_df
        .join(customer_df, how='inner')
        .join(orders_df, how='inner')
        .join(items_df, how='inner')
    )

    report_df = (
        joined_df
        .groupby(['customer_id', 'age', 'item_id', 'item_name'])
        .agg({'quantity': 'sum'})
        .reset_index()
        .rename(columns={
            'customer_id': 'Customer',
            'age': 'Age',
            'item_name': 'Item',
            'quantity': 'Quantity',
        })
    )

    report_df.to_csv(
        'report_using_pandas.csv',
        columns=['Customer', 'Age', 'Item', 'Quantity'],
        index=False,
        sep=';'
    )


def _read_customer(con):
    customer_df = (
        pd.read_sql('SELECT * FROM Customer', con)
        .set_index('customer_id')
    )

    customer_df = (
        customer_df
        .where(
            (customer_df['age'] >= 18)
            & (customer_df['age'] <= 35)
        )
        .dropna(subset='age')
    )

    customer_df = customer_df.astype({'age': int})

    return customer_df


def _read_orders(con):
    orders_df = (
        pd.read_sql('SELECT * FROM Orders', con)
        .set_index(['order_id', 'sales_id', 'item_id'])
    )

    orders_df = (
        orders_df
        .dropna(subset='quantity')
    )

    orders_df['quantity'] = orders_df['quantity'].astype(int)

    return orders_df


def _read_items(con):
    items_df = (
        pd.read_sql('SELECT * FROM Items', con)
        .set_index('item_id')
    )
    return items_df


def _read_sales(con):
    sales_df = (
        pd.read_sql('SELECT * FROM Sales', con)
        .set_index(['sales_id', 'customer_id'])
    )
    return sales_df


if __name__ == '__main__':
    main()
