from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# TODO: create route logic for signup
@app.route('/signup')
def signup():
    return render_template('signup.html')


# TODO: create route logic for login
@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)