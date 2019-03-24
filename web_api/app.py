#!/bin/python3
from flask import jsonify
from flask import Flask
import pathlib
import random
import json
import os

import functions as fn

# app configuration
app = Flask(__name__)
app.debug = True

# declare global variables
MAP = dict()
POSITION = ''
HIDE_ROOM = ''
HIDE_PLACE = ''

def set_up_game():
    global MAP, POSITION, HIDE_ROOM, HIDE_PLACE
    # read map from the json file
    path = pathlib.Path(os.path.abspath(__file__)).parent
    with open(str(path / 'map.json'), 'r') as f:
        MAP = json.load(f)


    # randomly generate the hideaway
    HIDE_ROOM = random.choice(list(MAP.keys()))
    HIDE_PLACE = random.choice(MAP[HIDE_ROOM])


    # Set the start position
    POSITION = 'corridor'

set_up_game()

@app.route('/')
def hello():
    "Just a little greeting."
    return 'Hello stranger, do you want to play game?'


@app.route('/map')
def show_map():
    "Get the map of our small world."
    other_locs = fn.get_locations(MAP, [POSITION])
    msg = f"Your current location is {POSITION}. There are also {other_locs}."
    return jsonify({'description': msg})


@app.route('/hint')
def hint():
    "Little hint for the admin."
    return f"Item located in {HIDE_ROOM} {HIDE_PLACE}"


@app.route('/details')
def look_around():
    "Description of current location and items aviable for the user."
    return jsonify(fn.description(MAP, POSITION))


@app.route('/details/<location>')
def describe_location(location):
    "Description of location and items aviable for the user."
    return jsonify(fn.description(MAP, location))


@app.route('/move/<direction>')
def move(direction):
    "Move to other location(sirection parameter)."
    global POSITION
    if direction in MAP:
        POSITION = direction
        msg = f'You are now in {direction}. Try to look around.'
    else:
        msg = f'There is no location like {direction}. Use map.'
    return jsonify({'description': msg})


@app.route('/check/<location>/<place>')
def check_move(location, place):
    "Check the hideplace in current location or move+check with two parameters."
    global POSITION
    if location == 'current':
        location = POSITION
    if location in MAP:
        POSITION = location
        if place in MAP[location]:
            if location == HIDE_ROOM and place == HIDE_PLACE:
                set_up_game()
                return jsonify({'description': 'You won! Good job!'})
            else:
                return jsonify({'description': "Not here. Keep looking."})
        else:
            msg = f'There is no such item as {place} here. Look around for details.'
            return jsonify({'description': msg})
    else:
        msg = f'There is no location like {location}. Use map.'
        return jsonify({'description': msg})


if __name__ == "__main__":
    set_up_game()
    app.run(host='0.0.0.0')
