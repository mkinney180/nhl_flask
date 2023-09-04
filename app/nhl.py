import random

from flask import (
    Blueprint, render_template, send_file
)
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from os import environ

from app.db import get_db

bp = Blueprint('nhl', __name__)

volume_path = environ['VOLUME_SAVE'] if 'VOLUME_SAVE' in environ else "/home/studpufffin/data/"
save_path = environ['LOCAL_SAVE'] if 'LOCAL_SAVE' in environ else "/plots/"

@bp.route('/')
def index():
    games = load_active_games()
    return render_template('nhl/index.html', games=games)

def load_active_games():
    return ['1', '2', '3']

@bp.route('/images/<game_id>')
def images(game_id):
    return render_template("nhl/images.html", img_name=game_id)

@bp.route('/fig/<game_id>')
def fig(game_id):
    # load plotting information for the game
    last_game_line, game_data = load_volume_data(game_id)

    saved_last_line, current_plot = load_local_data(game_id)

    if last_game_line == saved_last_line:
        # load saved plot
        pass
    else:
        # plot the probabilities
        pass

    # convert to html

    # return image

    # automatically reloading page: https://stackoverflow.com/questions/8470431/what-is-the-best-way-to-implement-a-forced-page-refresh-using-flask
    #  https://flask.palletsprojects.com/en/2.1.x/patterns/javascript/
    plt.close()
    c = random.choice(['b', 'r', 'k'])
    if img_name == '1':
        fig = plt.plot([1,2,3,4], [1,2,3,4], c)
    elif img_name == '2':
        fig = plt.plot([5,6,7,8], [5,6,7,8], c)
    elif img_name == '3':
        fig = plt.plot([9, 10, 11, 12], [9, 10, 11, 12], c)
    else:
        raise NotImplementedError

    img = BytesIO()
    plt.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')


def load_volume_data(game_id):
    pass


def load_local_data(game_id):
    pass
