from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/hello_world')
def hello_world():
    return 'Hello, World!'

@app.route('/just_hello')
def just_hello():
    return 'Just hello'

@app.route('/projects/')
def projects():
    return 'User are a the projects page'

@app.route('/about')
def about():
    return 'U are at the about page'

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('profile', username = 'Chirag Dabgar'))
    

@app.route('/hello/<name>')
def user_hello(name=None):
    return render_template('hello.html',name=name)

if __name__ == '__main__':
    app.run(port=5000, debug = True)