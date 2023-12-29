# This web application will allow the user to input recipes per their choosing, search for new ones based on database and log into it
from flask import Flask, render_template, request, url_for, redirect, jsonify
from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipefour.db'

db = SQLAlchemy(app)

# Models for holding information
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    difficulty = db.Column(db.String(100), nullable = False)
    time = db.Column(db.Integer, nullable = False)
    ingredients = db.Column(db.String(200), nullable = False)
    steps = db.Column(db.String(200), nullable = False)

class Info(db.Model):
    __tablename__ = 'info'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(100), nullable = False)

# For all recipes
def search_all():
    all_recipes= [
    {'name': 'scrambled eggs and toast', 'difficulty': 'easy', 'time': '5', 'ingredients': 'eggs, bread, butter, salt, pepper', 'steps': 'heat up toast with butter, scramble eggs, season'},
    {'name': 'protein shake', 'difficulty': 'easy', 'time': '5', 'ingredients': 'protein powder, milk, peanut butter, chia seeds, greek yoghurt', 'steps': 'blend ingredients until smooth'},
    {'name': 'fried rice', 'difficulty': 'medium', 'time': '30', 'ingredients': 'rice, egg, chicken, capsicum, beans, garlic, lime, chilli, soy sauce, siracha, peanut oil, spices (paprika, salt, pepper, onion powder)', 'steps': 'cut all vegetables, season chicken, oil pan, stir fry garlic and vegetables, cook chicken and egg, add cooked rice, mix and season'},
    {'name': 'grilled cheese', 'difficulty': 'easy', 'time': '5', 'ingredients': 'bread, butter, cheese, oil', 'steps': 'heat up bread in pan, add cheese, flip until melted'},
    {'name': 'tomato garlic pasta', 'difficulty': 'medium', 'time': '40', 'ingredients': 'pasta sauce, tomato paste, garlic, basil leaves, meat, seasonings (paprika, salt, pepper), cheese, tomatoes', 'steps': 'cook pasta, create sauce by mixing garlic, basil, pasta sauce, tomato paste, mix with pasta, season'},
    {'name': 'basil pesto pasta', 'difficulty': 'medium', 'time': '40', 'ingredients': 'pasta, basil pesto sauce, meat, parmesan cheese, basil leaves, salt, pepper', 'steps': 'cook pasta in pot, add sauce, seasonings, top with cheese'}
    ]

    for recipe in all_recipes:
        new_recipe = Recipe(**recipe)
        db.session.add(new_recipe)

    db.session.commit()
    print("Recipes are in?")

# Webpages
@app.route('/')
def login():
    information = Info.query.all()
    return render_template('login.html', information=information)

# Login form
@app.route('/log', methods= ['GET','POST'])
def confirm():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
            
        new_login = Info(username=username, password=password)
        db.session.add(new_login)
        db.session.commit()

    information = Info.query.all()
    return render_template('login.html', information=information)

# Other webpages
@app.route('/add')
def add():
    recipes = Recipe.query.all()
    return render_template('add.html', recipes=recipes)

@app.route('/search')
def search():
    return render_template('search.html')

# Displaying form results
@app.route('/append', methods = ['GET','POST'])
def append():
    if request.method == "POST":
        name = request.form['name']
        difficulty = request.form['difficulty']
        time = request.form['time']
        ingredients = request.form['ingredients']
        steps = request.form['steps']

        new_recipe = Recipe(name=name, difficulty=difficulty, time=time, ingredients=ingredients, steps=steps)
        db.session.add(new_recipe)
        db.session.commit()

    recipes = Recipe.query.all()
    return render_template('add.html', recipes=recipes)

# Searching recipes
@app.route('/filter')
def filter():
    query = request.args.get('query', '')
    matching_recipes = Recipe.query.filter(
        (func.lower(Recipe.name).ilike(f'%{query}%')) | 
        (func.lower(Recipe.difficulty).ilike(f'%{query}%'))| 
        (func.lower(Recipe.time).ilike(f'%{query}%')) | 
        (func.lower(Recipe.ingredients).ilike(f'%{query}%'))
    ).all()

    print("recipe searching!")
    result = [{'name': recipe.name, 'difficulty': recipe.difficulty, 'time': recipe.time, 'ingredients': recipe.ingredients, 'steps': recipe.steps} for recipe in matching_recipes]
    print(result)
    return render_template('search.html', recipes=matching_recipes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Tables created!")

    app.run(debug=True)
