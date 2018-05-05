# import Flask class from flask library
# jsonify is used to convert python dictionary into text understood by java script
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# list of stores
stores = [
    {
        'name': 'My store',
        'items': [
            {
                'name': "chair",
                'colour': 'red',
                'price': 7.99
            },
            {
                'name': "chair",
                'colour': 'blue',
                'price': 8.99
            }
        ]

    },
    {
        'name': 'Not my store',
        'items': [
            {
                'name': "chair",
                'colour': 'red',
                'price': 12.99
            }
        ]
     }
]

# when running this we return java script and html code
# from index.html
@app.route('/')
def home():
    return render_template('index.html')


# POST - used to send data
# GET - used to send data back only

# POST /store data:{name:}
# @app.route by default is configured to perform GET
# we need to specify the method which in this case is POST
@app.route('/store', methods=['POST'])
def create_store():
    # the request is made to the end point '/'
    # when the browser sends us the request to create new store
    # the browser also send us json data which in this case is the name of the store
    request_data = request.get_json()
    # now we can create new store which is a dictionary with the name
    # where the name is the request from json
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    # now we need to append our new store
    stores.append(new_store)
    # we return newly created store so that the browser know that it has been created
    return jsonify(new_store)

# GET /store/<string: name>
# name is used as an argument in get_store method
# when we visit http://127.0.0.1:5000/store/some_name
# some_name needs to match the name argument
@app.route('/store/<string:name>')
def get_store(name):
    # iterate over stores
    for store in stores:
        # if match found, return it
        if store['name'] == name:
            return jsonify(store)
        # if nothing found, return error message
        else:
            return jsonify({'message': 'Store not found!'})

# GET /store
@app.route('/store')
def get_stores():
    # we need to convert stores into dictionaries
    # as originally it is a list
    # jsonify can not understand lists
    # we create a dictionary 'stores' with only one key
    # which is the list of stores
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'colour': request_data['colour'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'Store not found!'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    # iterate over stores
    for store in stores:
        # if match found, return it
        if store['name'] == name:
            return jsonify(store['items'])
        # if nothing found, return error message
        else:
            return jsonify({'message': 'Store not found!'})

app.run(port=5000)

# 127.0.0.1 is the ip address reserved for local machine
