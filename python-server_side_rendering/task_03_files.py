#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


# ✅ Lire JSON
def read_json():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except Exception:
        return []


# ✅ Lire CSV
def read_csv():
    data = []
    try:
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # convertir types
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
    except Exception:
        return []
    return data


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    data = []
    error = None

    # ✅ Choix source
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        error = "Wrong source"
        return render_template('product_display.html', error=error)

    # ✅ Filtrer par id
    if product_id:
        try:
            product_id = int(product_id)
            data = [p for p in data if p['id'] == product_id]

            if not data:
                error = "Product not found"
        except ValueError:
            error = "Invalid id"

    return render_template('product_display.html', products=data, error=error)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
