# star_routes.py

from flask import Blueprint, render_template, request, redirect, url_for, Response
from app import models

bp = Blueprint('star', __name__)

@bp.route('/star', methods=['GET', 'POST'])
def add_list():

    models.get_tickers()

    if request.method=='GET':

        watch_list = models.get_table()
        return render_template('watchlist.html', watch_list=watch_list), 200

    if request.method=='POST':
        company = request.form.get('company', None).upper()
        ticker = request.form.get('ticker', None).upper()
        memo = request.form.get('memo', None)

        result = models.add_list(name=company, ticker=ticker, memo=memo)
        
        if None in result:
            return result[0], 404
        
        return redirect(url_for('.add_list'), code = 200)
     
    
@bp.route('/star/')
@bp.route('/star/<ticker>')
def delete_star(ticker=None):
    if ticker is None:
        return "400 error", 400

    delete = models.delete_list(ticker)
    if delete is None:
        return "404 error", 404
    
    else:
        return redirect(url_for('.add_list'), code=200)
