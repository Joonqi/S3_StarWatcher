# graph_routes.py

from flask import Blueprint, render_template, make_response
from app.services import api
from app import models

from functools import wraps, update_wrapper
from datetime import datetime, date


bp = Blueprint('graph', __name__)

def nocache(view):
    @wraps(view)
    def no_cache(*args, **kwargs):
        response = make_response(view(*args, **kwargs))
        response.headers['Last-Modified'] = datetime.now()
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '-1'
        
        return response      
    
    return update_wrapper(no_cache, view)


@bp.route('/graph', methods=['GET', 'POST'])
def graph():

    watchlist = models.get_table()

    return render_template('graph.html', watchlist=watchlist), 200



@bp.route('/graph/')
@bp.route('/graph/<ticker>')
@nocache
def make_graph(ticker=None):
    
    img = api.plot_graph(ticker)
    name = models.Firm.query.filter(models.Firm.ticker==ticker).first().name

    return render_template('graph.html', name=name, image=img)
