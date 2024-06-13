from living_spring import app

from flask import render_template, request


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        # we can process the form data (e.g., save to database)
        # but for understanding of what's going on at the backend, let's print it to the console for now
        print(f'Username: {username}, Email: {email}')
        return "Form submitted!"
    return render_template('signup.html')