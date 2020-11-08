from flask import Flask
from flask import render_template
import random
import json
app = Flask(__name__)

menu = [
	{
		'name': 'burger',
		'pic': 'burger.jpg',
		'price': 1000
	},
	{
		'name': 'pizza',
		'pic': 'pizza.jpg',
		'price': 2000
	},
	{
		'name': 'sushi',
		'pic': 'sushi.jpg',
		'price': 1000
	},
]


@app.route('/')
def hello_world():
	return render_template('food.html')

@app.route('/something/<some>')
def get_something(some):
	return render_template('index.html', variable=some, name='Hiro')

@app.route('/food')
def get_food():
	return random.choice(['pizza', 'burguer', 'sushi', 'ramen'])

@app.route('/put')
def put_food():
	random_food = random.choice(menu)
	return json.dumps(random_food)

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

app.run()
