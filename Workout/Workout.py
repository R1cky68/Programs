from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workout4.db'

db = SQLAlchemy(app)

class Workout(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    exercise = db.Column(db.String(100), nullable= False)
    reps = db.Column(db.Integer, nullable = False)
    sets = db.Column(db.Integer, nullable = False)
    weight = db.Column(db.Integer, nullable = False)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    
@app.route('/')
def index():
    workouts = Workout.query.order_by(Workout.date.desc()).all()
    return render_template('index.html', workouts=workouts)

@app.route('/add', methods = ['POST'])
def add():
    exercise = request.form['exercise']
    sets = request.form['sets']
    reps = request.form['reps']
    weight = request.form['weight']
    
    new_workout = Workout(exercise=exercise, sets=sets, reps=reps, weight=weight)
    db.session.add(new_workout)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
    app.run(debug=True)