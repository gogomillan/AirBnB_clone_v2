#!/usr/bin/python3
"""
Python script that starts a Flask web application:
- Uses storage for fetching data from the storage engine
- /states_list: display a HTML page: (inside the tag BODY) UL states
- /cities_by_states: display a HTML page: (inside the tag BODY) states->cities
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(obj):
    """
    Teardown application context
    """
    storage.close()


@app.route('/states/')
def states():
    """
    Function associated to the '/states/' path
    """
    return render_template('7-states_list.html',
                           states=storage.all(State).values())


@app.route('/states/<id>')
def states_id():
    """
    Function associated to the '/states/<id>' path
    """
    flag = 0
    states = None
    states_all = storage.all(State).values()
    for state in states_all:
        if id in state.id:
            flag = 1
            states = state
            break
    return render_template('9-states.html', states=states, flag=flag)


@app.route('/states_list/')
def states_list():
    """
    Function associated to the '/states_list/' path
    """
    return render_template('7-states_list.html',
                           states=storage.all(State).values())


@app.route('/cities_by_states')
def cities_by_states():
    """
    Function associated to the '/cities_by_states/' path
    """
    return render_template('8-cities_by_states.html',
                           states=storage.all(State).values())


if __name__ == "__main__":
    app.run()
