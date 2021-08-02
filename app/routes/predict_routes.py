# predict_routes.py

from flask import Blueprint, render_template, request
import pandas as pd
from app.services import api
from app import models

bp = Blueprint('predict', __name__)

@bp.route('/predict', methods = ['GET', 'POST'])
def import_list():
    watchlist = models.get_table()
    recommend = []

    if request.method == 'GET':
        return render_template('predict.html', watchlist=watchlist, recommend=recommend), 200

    target = request.form.get('target', None)
    
    if request.method == 'POST':
        if target is None:
            return "400 error", 400
    result = api.get_forecast(target)
    recom = api.get_recommend(target)
    recommend = list(recom.iterrows())


    if result[2] > 0:
        color = 'table-danger table-hover'
    elif result[2] <= 0:
        color = 'table-primary table-hover'


    return render_template('predict.html', watchlist=watchlist, color=color, forecast=result, recommend=recommend) 
