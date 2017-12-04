"""
    Student Repository Website
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world! This is Flask!"

@app.route('/Goodbye')
def see_ya():
    return "See you later!"

@app.route('/sample_template')
def template_demo():
    return render_template('parameters.html',
                           title='Stevens Repository',
                           my_param='My custom parameter')

app.run(debug=True)





