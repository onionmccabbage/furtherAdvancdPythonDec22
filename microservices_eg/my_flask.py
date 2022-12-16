# Flask is a microservcie that implements web-aware features
# we can specify URL paths and web page responses
from flask import Flask # may need to pip install flask
from flask import render_template
from weather import getWeather 
import numpy as np
import pandas as pd

# CAREFUL changes will only take effect when the server is re-started

# we begin by declaring a flask server
app = Flask(__name__) # convention

# we declare functions that will handle each type of request from the client (a web browser)

@app.route('/') # this is the entry point for our Flask server
def root(): # by convention, we define the 'root' of our server i.e. the entry point
    return 'hello'

@app.route('/map') # we cana invent any woutes we like
def map():
    return 'here is a map of Athlone in deep snow'

@app.route('/info') # capture alternative names
@app.route('/about')
@app.route('/aboot') # capture common mis-spellings
def about():
    return '<h2>This is the ABOUT page</h2>'

@app.route('/greet')
@app.route('/greet/') # we might want to also allow for trailing slashes (not common practice)
@app.route('/greet/<name>') # all these routes will run the SAME function
@app.route('/greet/<name>/<sname>') 
def greet(name=None, sname=None): # we expect a parameter for 'name', but we provide a default
    greeting = 'Hello'
    if name != None:
        if sname != None:
            return f'<h3>{greeting} {name} {sname}</h3>'
        else:
            return f'<h3>{greeting} {name}</h3>'
    else:    
        return 'Generic Greeting to all citizens'

@app.route('/menu')
def menu():
    link1 = '<a href="/">Home</a>'
    link2 = '<a href="/about">About</a>'
    link3 = '<a href="/greet">Greeting</a>'
    link4 = '<a href="/map">Map</a>'
    return f' {link1} | {link2} | {link3} | {link4}'

# we can handle parameters and respond with a full web page
@app.route('/service')
@app.route('/service/<comms>') # pass ONE parameter
@app.route('/service/<comms>/<equipment>') # pass TWO parameters
def service(comms=None, equipment=None):
    # send back an entire web page (NB Flask assumes the web pages will be in the 'templates' folder)
    return render_template('service.html', comms = comms, equipment=equipment)

# the strategy is to go from simple paths to more complex paths. Flask will handle the FIRST matching route
@app.route('/drinks')
def drinks():
    return 'Available beverages: water, juice, tea, coffee'

@app.route('/lunch')
@app.route('/lunch/<desert>')
def lunch(desert=None):
    return render_template('lunch.html', desert=desert)

@app.route('/weather/<city>')
def weather(city='Athlone'):
    # call our weather service
    w = getWeather(city)
    return w.encode()

@app.route('/flights')
def flights():
    df = pd.read_csv('http://rcs.bu.edu/examples/python/data_analysis/flights.csv')
    # ust show the number of unique aircraft
    n = f'there are {df.tailnum.nunique()} unique aircraft in this data set'
    return str(n).encode()

# all other routes will end up with a default 404 response from Flask

if __name__ == '__main__':
    app.run(host='127.0.0.1') # localhost