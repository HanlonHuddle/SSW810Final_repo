"""
    Testing Flask installation
"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world! This is Flask!"
    
@app.route('/Goodbye')
def see_ya():
    return "See you later!"

app.run(debug=True)
