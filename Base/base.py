from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    @app.route('/')
    def home():
        users = User.query.all()
        return render_template('home.html', users=users)

    @app.route('/add_user', methods=['GET', 'POST'])
    def add_user(): 
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']

            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                return "Email already exists. Choose a different email."

            new_user = User(username=username, email=email)
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('home'))
    
        return render_template('add_user.html')

    @app.route('/users')
    def show_users():
        users = User.query.all()
        usernames = [user.username for user in users]
        return f"Usernames: {', '.join(usernames)}"

    app.run(debug=True)
