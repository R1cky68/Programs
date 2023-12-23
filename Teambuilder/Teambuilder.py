from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///team5.db'

db = SQLAlchemy(app)

# Database model for teambuilding
class Team(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable= False)
    level = db.Column(db.Integer, nullable = False)
    ability = db.Column(db.String(100), nullable= False)
    item = db.Column(db.String(100), nullable= False)
    moves = db.Column(db.String(200), nullable= False)

# Dictionary to store moves and descriptions
moves_dict = {
    "Thunder": "Electric move with high damage.",
    "Iron Tail": "Steel move with a chance to lower opponent's Defense.",
    "Giga Impact": "Normal move with high power, but requires a turn to recharge.",
    "Cross Chop": "Fighting move with a high critical-hit ratio.",
    "Brutal Swing": "Dark move that hits all adjacent Pokemon.",
    "Brick Break": "Fighting move that breaks through the opponent's Light Screen and Reflect.",
    "Swords Dance": "Normal move that sharply raises the user's Attack.",
    "Final Gambit": "Fighting move that sacrifices the user but deals damage equal to its HP.",
    "Leaf Blade": "Grass move with a high critical-hit ratio.",
    "Dragon Pulse": "Dragon move with medium damage.",
    "Focus Blast": "Fighting move with a chance to lower opponent's Special Defense.",
    "Shed Tail": "Normal move that sharply raises the user's Speed.",
    "Spirit Break": "Fairy move that lowers the opponent's Special Attack.",
    "Shadow Ball": "Ghost move that has a chance to lower opponent's Special Defense.",
    "Bulk Up": "Fighting move that raises the user's Attack and Defense.",
    "Darkest Lariat": "Dark move with high power that ignores opponent's stat changes."
}

# Navigating webpages
@app.route('/')
def home():
    teams = Team.query.all()
    return render_template('home.html', teams=teams)

@app.route('/battle')
def battle():
    return render_template('battle.html')

# Displaying team as inputted
@app.route('/add', methods = ['POST'])
def add():
    name = request.form['name']
    level = request.form['level']
    ability = request.form['ability']
    item = request.form['item']
    moves = request.form['moves']
    
    new_team = Team(name=name, level=level, ability=ability, item=item, moves=moves)
    db.session.add(new_team)
    db.session.commit()

    return redirect(url_for('home'))

# Displaying pokemon and move selected
@app.route('/battle', methods=["GET", "POST"])
def team():
    if request.method == "POST":
        requested_pokemon = request.form.get('pokemon')
        requested_move_description = request.form.get('move')

        # Look up the move name based on the description
        requested_move = None
        for move, description in moves_dict.items():
            if description == requested_move_description:
                requested_move = move
                break

        if requested_move is not None:
            return f"You selected: {requested_pokemon}, using {requested_move}"
        
        else:
            return "Error: Move not found"

    return render_template('battle.html', requested_pokemon=request.form.get('pokemon'), requested_move=request.form.get('move'))
    
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)