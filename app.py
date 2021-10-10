# Import the Flask dependency

from flask import Flask

# Create a new Flask app instance

app = Flask(__name__)

# Create Flask Routes

@app.route('/')

# Create a function to run in the route just created

def hello_world():
    return 'Hello World'

# Add another route

@app.route('/second')
def second():
    return('this is a branch of the first route')