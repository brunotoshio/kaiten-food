from flask import Flask
from flask import render_template
import random
import json
app = Flask(__name__)

@app.route('/')
def hello_world():
	return ''

@app.route('/something/<some>')
def get_something(some):
	return render_template('index.html', variable=some, name='Hiro')

@app.route('/food')
def get_food():
	return random.choice(['pizza', 'burguer', 'sushi', 'ramen'])

@app.route('/menu')
def get_menu():
	menu = {
		'drinks': [
			'juice',
			'water',
			'soda'
		],
		'pizzas': [
			'margherita',
			'mozzarela',
			'pepperoni'
		]
	}
	return json.dumps(menu)
