# Flask is a microservcie that implements web-aware features
# we can specify URL paths and web page responses
from flask import Flask # may need to pip install flask
from flask import render_template

# CAREFUL changes will only take effect when the server is re-started

# we begin by declaring a flask server
app = Flask(__name__) # convention

# we declare functions that will handle each type of request from the client (a web browser)





if __name__ == '__main__':
    app.run(host='127.0.0.1') # localhost