from flask import Flask, render_template, request, jsonify, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

# Flask instance
app = Flask(__name__, static_url_path='/static')

#Add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newest_programs3.db'

#Initialise database
database = SQLAlchemy(app)

# Database model
class Program(database.Model):
    id = database.Column(database.Integer, primary_key = True)
    name = database.Column(database.String(100), nullable = False)
    language = database.Column(database.String(100), nullable = False)
    github_link = database.Column(database.String(255), nullable = False)

    def __repr__(self):
        return '<Name %r>' % {self.name} 

def add_initial_programs():
    existing_programs = Program.query.all()
    if existing_programs:
        print("Programs already exist in the database.")
        return
    
    programs = [
        {'name': 'App', 'language': 'Swift', 'github_link': 'https://github.com/R1cky68/Programs/tree/main/App.xcodeproj'},
        {'name': 'Battle', 'language': 'Python','github_link': 'https://github.com/R1cky68/Programs/blob/main/Battle'},
        {'name': 'Base', 'language': 'Python','github_link': 'https://github.com/R1cky68/Programs/tree/main/Base'},
        {'name': 'Calculator', 'language': 'Python', 'github_link': 'https://github.com/R1cky68/Programs/blob/main/Calculator'},
        {'name': 'Countdown', 'language': 'Python', 'github_link': 'https://github.com/R1cky68/Programs/blob/main/Countdown.py'},
        {'name': 'Diagnosis', 'language': 'C++', 'github_link': 'https://github.com/R1cky68/Programs/blob/main/Diagnosis.cpp'},
        {'name': 'Dodge', 'language': 'Spritekit', 'github_link': 'https://github.com/R1cky68/Programs/tree/main/Dodge.xcodeproj'},
        {'name': 'Downloader', 'language': 'Python', 'github_link': 'https://github.com/R1cky68/Programs/blob/main/Downloader.py'},
        {'name': 'Fall', 'language': 'Spritekit', 'github_link': 'https://github.com/R1cky68/Programs/tree/main/Fall.xcodeproj'},
        {'name': 'Graph', 'language': 'Python', 'github_link': 'https://github.com/R1cky68/Programs/tree/main/Graph'},
        {'name': 'Haircut', 'language': 'C++', 'github_link': 'https://github.com/R1cky68/Programs/blob/main/Haircut.cpp'},
        {'name': 'Hello', 'language': 'C++', 'github_link': 'https://github.com/R1cky68/Programs/blob/main/Hello.cpp'},
        {'name': 'Learn', 'language': 'Python', 'github_link': 'https://github.com/R1cky68/Programs/blob/main/Learn.py'},
        {'name': 'Monitor', 'language': 'C++','github_link': 'https://github.com/R1cky68/Programs/blob/main/Monitor.cpp'},
        {'name': 'Notes', 'language': 'Swift', 'github_link': 'https://github.com/R1cky68/Programs/tree/main/Notes.xcodeproj'},
        {'name': 'Number', 'language': 'Python', 'github_link': 'https://github.com/R1cky68/Programs/blob/main/Number.py'},
        {'name': 'Password', 'language': 'Python', 'github_link': 'https://github.com/R1cky68/Programs/blob/main/Password.py'},
        {'name': 'Placement', 'language': 'Python', 'github_link': 'https://github.com/R1cky68/Programs/blob/main/Placement.py'},
        {'name': 'Pong', 'language': 'Spritekit', 'github_link': 'https://github.com/R1cky68/Programs/tree/main/Pong.xcodeproj'},
        {'name': 'Recipe', 'language': 'Python', 'github_link': 'https://github.com/R1cky68/Programs/tree/main/Recipe%20copy'},
        {'name': 'Showdown', 'language': 'Python', 'github_link': 'https://github.com/R1cky68/Programs/blob/main/Showdown'},
        {'name': 'Snake', 'language': 'Python', 'github_link': 'https://github.com/R1cky68/Programs/blob/main/Snake'},
        {'name': 'Sort', 'language': 'Python', 'github_link': 'https://github.com/R1cky68/Programs/blob/main/Sort'},
        {'name': 'Todo', 'language': 'Swift', 'github_link': 'https://github.com/R1cky68/Programs/tree/main/Todo'},
        {'name': 'Teambuilder', 'language': 'Python', 'github_link': 'https://github.com/R1cky68/Programs/blob/main/Teambuilder'},
        {'name': 'Tracker', 'language': 'Python', 'github_link': 'https://github.com/R1cky68/Programs/blob/main/Tracker'},
        {'name': 'Volkner', 'language': 'C++', 'github_link': 'https://github.com/R1cky68/Programs/blob/main/Volkner'},
        {'name': 'Weather', 'language': 'Python', 'github_link': 'https://github.com/R1cky68/Programs/blob/main/Weather.py'},
        {'name': 'Website', 'language': 'Python', 'github_link': 'https://github.com/R1cky68/Programs/tree/main/Website'},
        {'name': 'Word', 'language': 'Python', 'github_link': 'https://github.com/R1cky68/Programs/blob/main/Word.py'},
        {'name': 'Workout', 'language': 'Python', 'github_link': 'https://github.com/R1cky68/Programs/tree/main/Workout'},
        {'name': 'Writer', 'language': 'Python', 'github_link': 'https://github.com/R1cky68/Programs/blob/main/Writer.py'},
        {'name': 'X', 'language': 'C++', 'github_link': 'https://github.com/R1cky68/Programs/blob/main/X.cpp'},
    ]

    for program in programs:
        new_program = Program(**program)
        database.session.add(new_program)

    database.session.commit()
    print("Initial programs added to database")

# Navigating webpages
@app.route("/")
def homepage():
    return render_template('Homepage.html')

@app.route("/programs")
def programs():
    programs = Program.query.all()
    programs_data = [{'name': program.name, 'language': program.language, 'github_link': program.github_link} for program in programs]
    print(programs_data)
    return render_template('Programs.html', programs=programs_data)
    
@app.route("/contact")
def contact():
    return render_template('Contact.html')

# Filling subscribe form
@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form.get('email', '')
    print(email)
    return jsonify({'message': f'Email {email} subscribed successfully!'}) # Just that email value is not showing up

# Filling contact form
@app.route('/fill', methods=['POST'])
def fill():
    name = request.form.get('name')
    mail = request.form.get('mail')
    message = request.form.get('paragraph')
    print(name)
    print(mail)
    print(message)
    return jsonify({'message': 'Thank you for your message!'})

# Searching programs
@app.route('/search_programs')
def search_programs():
    query = request.args.get('query', '')
    matching_programs = Program.query.filter(
        (Program.name.ilike(f'%{query}%')) | (Program.language.ilike(f'%{query}%'))
        ).all()
    result = [{'name': program.name, 'language': program.language, 'github_link': program.github_link} for program in matching_programs]
    return jsonify(result)

@app.route('/add_program', methods=['POST'])
def add_program():
    data = request.get_json()
    new_program = Program(name=data['name'], language=data['language'], github_link=data['github_link'])
    database.session.add(new_program)
    database.session.commit()
    return redirect('/programs')

if __name__ == '__main__':
    with app.app_context():
        database.drop_all()
        database.create_all()
        add_initial_programs()

    app.run(debug=False)
