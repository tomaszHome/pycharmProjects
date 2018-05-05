# import Flask class from flask library
from flask import Flask

# create an app from Flask class
# __name__ give each file unique name
app = Flask(__name__)

# we need to tell our app what request it needs to understand
# for this we use the decorator
# '/' means homepage i.e for google homepage http://www.google.com/
@app.route('/')
def home():
    return "Hello World! What's up?"
# we need to tell app to start running.
# port is the area of the computer where app will
# receive requests and returning the responses
# computers have many of these areas
# if receive error that port is in use just change the number i.e 4999
app.run(port=5000)

# 127.0.0.1 is the ip address reserved for local machine
