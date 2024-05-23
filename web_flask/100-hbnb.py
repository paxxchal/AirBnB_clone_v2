#!/usr/bin/python3
"""
Flask Application
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """
    Remove the current SQLAlchemy Session after each request
    """
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    Display the main HBNB filters and objects
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    states_list = [state.as_dict() for state in states]
    amenities = sorted(list(storage.all("Amenity").values()), key=lambda x: x.name)
    stayings = sorted(list(storage.all("Place").values()), key=lambda x: x.name)
    return render_template(
        "100-hbnb.html", states_list=states_list, amenities=amenities, places=stayings
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
