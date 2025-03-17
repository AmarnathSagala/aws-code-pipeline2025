from flask import render_template
from . import create_app

app = create_app()

@app.route('/')
def index():
    products = [
        {'name': 'Toy Car', 'price': '$10'},
        {'name': 'Doll', 'price': '$15'},
        {'name': 'Puzzle', 'price': '$8'}
    ]
    return render_template('index.html', products=products)
