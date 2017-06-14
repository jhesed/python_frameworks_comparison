"""
    Simple RESTful API code using Flask
    :Author: Jhesed Tacadena
    :Date: 2017-06-14

    :Notes:
        - GET: Retrieve
        - POST: Insert
        - PUT: Update
        - DELETE: remove

    :Comments:
        - Postman is a good tool for testing APIs
        - No DB Manipulation done here for testing purpose only
"""

# ------------------------------------------------------------------------------
# SECTION :: IMPORTS
# ------------------------------------------------------------------------------

from flask import Flask, jsonify, request


# ------------------------------------------------------------------------------
# SECTION :: Static Variables
# ------------------------------------------------------------------------------

app = Flask(__name__)
countries = [{'name': 'Philippines'}, {'name': 'Python'}]


# ------------------------------------------------------------------------------
# SECTION :: GET Requests
# ------------------------------------------------------------------------------

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message': 'It works!'})

# ------------------------------------------------------------------------------
@app.route('/countries', methods=['GET'])
def get_countries():
    """
    Retrieves all countries
    """
    return jsonify({'countries': countries})

# ------------------------------------------------------------------------------
@app.route('/countries/<string:name>', methods=['GET'])
def get_country(name):
    """
    Retrieves the first country found by name
    :param name: name of country to be retrieved
    """

    for country in countries:
        if country['name'] == name:
            return jsonify(country)


# ------------------------------------------------------------------------------
# SECTION :: POST Requests
# ------------------------------------------------------------------------------

@app.route('/countries', methods=['POST'])
def add_countries():
    """
    Adds country to list of countries
    """

    # Retrieve values from request object
    name = request.json['name']

    country = {'name': name}
    countries.append(country)
    return jsonify({'countries': countries})


# ------------------------------------------------------------------------------
# SECTION :: PUT Requests
# ------------------------------------------------------------------------------

@app.route('/countries/<string:old_name>', methods=['PUT'])
def update_country(old_name):
    """
    Updates country given the `name`
    :param old_name: old name of country to be replaced
    """

    # Retrieve values from json
    new_name = request.json['name']

    for index, country in enumerate(countries):
        if country['name'] == old_name:
            # Perform the update
            countries[index]['name'] = new_name
            return countries


# ------------------------------------------------------------------------------
# SECTION :: DELETE Requests
# ------------------------------------------------------------------------------

@app.route('/countries/', methods=['DELETE'])
def delete_country():
    """
    delete country given the `name`
    :param name: old name of country to be replaced
    """

    # Retrieve values from json
    name = request.json['name']

    for index, country in enumerate(countries):
        if country['name'] == name:
            # Perform the update
            countries.remove(country)
            return countries


# ------------------------------------------------------------------------------
# SECTION :: Main
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True, port=8080)