from flask import Flask, render_template
import sqlite3
import pandas as pd
import os

app = Flask(__name__)

def get_data():
    conn = sqlite3.connect('data/sales.db')
    df = pd.read_sql_query("SELECT * FROM sales", conn)
    conn.close()
    return df

@app.route('/')
def dashboard():
    df = get_data()

    total_revenue      = f"${df['total_amount'].sum():,.2f}"
    total_transactions = f"{len(df):,}"
    avg_order_value    = f"${df['total_amount'].mean():,.2f}"

    region_data  = df.groupby('region')['total_amount'].sum().round(2).to_dict()
    product_data = df.groupby('product')['total_amount'].sum().round(2).to_dict()
    payment_data = df.groupby('payment_method')['total_amount'].sum().round(2).to_dict()

    return render_template('dashboard.html',
        total_revenue      = total_revenue,
        total_transactions = total_transactions,
        avg_order_value    = avg_order_value,
        region_data        = region_data,
        product_data       = product_data,
        payment_data       = payment_data,
    )

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)