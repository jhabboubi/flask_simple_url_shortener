"""
    importing flask
    importing render_template
    importing request
"""
from types import CodeType
from flask import Flask, render_template, request
import sys

# __name__ name of the module
app = Flask(__name__)
# prints the name variable on console
# print(__name__)
"""
    when the user hit URL localhost:5000/ on a browser
    this function will be executed
    rendering html page located in templates folder
"""


@app.route('/')
def home():
    # return render_template('home.html', name='jafer')
    return render_template('home.html')


"""
    form receives URL and short code
    to refer to the shorten website
    request can be use to get back
    the get or post request via the
    args dictionary and passing it the 
    name="code" that was provided in html input 
    GET request use request.args['code']
    POST request use request.form['code'] 
"""


@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        return render_template('your_url.html', code=request.form['code'])
    else:
        return render_template('404.html', err='NOT ALLOWED GET REQUEST')


"""
    function execute once user
    visit localhost:5000/about
    name of function and route don't need to match!
"""


@app.route('/about')
def about():
    return 'This is a url shortener'
