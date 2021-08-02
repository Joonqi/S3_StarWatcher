# home_routes.py

from flask import Blueprint, render_template, redirect, url_for
from app import models, db


bp = Blueprint('home', __name__)

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/refresh')
def refresh():
    db.drop_all()
    db.create_all()
    return redirect(url_for('.home'), code = 200)