"""
    Simple RESTful API code using Flask.
    DB version of `flask_restful_api.py`

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
from flask.views import MethodView
from store.store_factory import get_db_store

# ------------------------------------------------------------------------------
# SECTION :: Static Variables
# ------------------------------------------------------------------------------

app = Flask(__name__)

# ------------------------------------------------------------------------------
class CountriesAPI(MethodView):


    def __init__(self, store_type='cassandra'):
        """
        Initializes Flask API
        """

        self.storage = get_db_store(store_type)


    # --------------------------------------------------------------------------
    # SECTION :: GET Requests
    # --------------------------------------------------------------------------

    def test(self):
        return jsonify(self.storage.retrieve_all())

    # --------------------------------------------------------------------------
    @app.route('/countries', methods=['GET'])
    def get_countries(self):
        """
        Retrieves all countries
        """
        return jsonify({'countries': countries})

    # --------------------------------------------------------------------------
    @app.route('/countries/<string:name>', methods=['GET'])
    def get_country(self, name):
        """
        Retrieves the first country found by name
        :param name: name of country to be retrieved
        """

        for country in countries:
            if country['name'] == name:
                return jsonify(country)


    # --------------------------------------------------------------------------
    # SECTION :: POST Requests
    # --------------------------------------------------------------------------

    @app.route('/countries', methods=['POST'])
    def add_countries(self):
        """
        Adds country to list of countries
        """

        # Retrieve values from request object
        name = request.json['name']

        country = {'name': name}
        countries.append(country)
        return jsonify({'countries': countries})


    # --------------------------------------------------------------------------
    # SECTION :: PUT Requests
    # --------------------------------------------------------------------------

    @app.route('/countries/<string:old_name>', methods=['PUT'])
    def update_country(self, old_name):
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


    # --------------------------------------------------------------------------
    # SECTION :: DELETE Requests
    # --------------------------------------------------------------------------

    @app.route('/countries/<string:name>', methods=['DELETE'])
    def delete_country(self, name):
        """
        delete country given the `name`
        :param name: old name of country to be replaced
        """

        for index, country in enumerate(countries):
            if country['name'] == name:
                # Perform the update
                countries.remove(country)
                return jsonify({'countries': countries})


# ------------------------------------------------------------------------------
# SECTION :: Main
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    country_view = CountriesAPI.as_view('country_api')
    app.add_url_rule('/teset', view_func=country_view, methods=['GET'])
    app.run(debug=True, host='0.0.0.0', port=8080)
