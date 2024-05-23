#!/usr/bin/python3
"""Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """base route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def Cee(text):
    """/c/<text> route"""
    return 'C {}'.format(' '.join(text.split('_')))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def mypy(text='is cool'):
    """/python/<text> route"""
    return 'Python {}'.format(' '.join(text.split('_')))


@app.route('/number/<int:n>', strict_slashes=False)
def check_num(n):
    """/c/<text> route"""
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
