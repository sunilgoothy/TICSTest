from flask import Blueprint, jsonify, request
from app import table_builder
from pprint import pprint 

tables = Blueprint('tables', __name__, url_prefix='/tables')


@tables.route("/clientside_table", methods=['GET'])
def clientside_table_content():
    data = table_builder.collect_data_clientside()
    return jsonify(data)


@tables.route("/serverside_table", methods=['GET'])
def serverside_table_content():
    data = table_builder.collect_data_serverside(request)
    pprint(data)
    return jsonify(data)
