"""
    API REST using Python 3 and SQLite 3
    Goal: Learn a bit of python, flask and API hosting
"""
from flask import Flask, jsonify, request
from create_tables import create_tables
import ideas_controller
app = Flask(__name__)

@app.route('/')
def example():
    print("Hello")
    return 'The value of __name__ is {}'.format(__name__)

@app.route('/ideas', methods=["GET"])
def get_ideas():
    try:
        ideas = ideas_controller.get_ideas()
        print('Get ideas')
        return jsonify(ideas)
    except Exception as er:
        print(er)

@app.route("/idea", methods=["POST"])
def insert_idea():
    try:
        idea_details = request.get_json()
        print(idea_details)
        value = idea_details["value"]
        maturityLevel = idea_details["maturityLevel"]
        FullText = idea_details["FullText"]
        result = ideas_controller.insert_idea(value, maturityLevel, FullText)
        return jsonify(result)
    except Exception as er:
        print(er)

@app.route("/idea", methods=["PUT"])
def update_idea():
    try:
        idea_details = request.get_json()
        print(idea_details)
        ideaId = idea_details["id"]
        value = idea_details["value"]
        maturityLevel = idea_details["maturityLevel"]
        FullText = idea_details["FullText"]
        result = ideas_controller.update_idea(ideaId, value, maturityLevel, FullText)
        return jsonify(result)
    except Exception as er:
        print(er)

@app.route("/idea/<id>", methods=["DELETE"])
def delete_idea(id):
    result = ideas_controller.delete_idea(id)
    return jsonify(result)

if __name__ == "__main__":
    create_tables()
    print("tables created?")
    app.run(host='0.0.0.0', port=8000, debug=True)