# models.py

from app import db
import datetime
import os
import csv

class Firm(db.Model):
    __tablename__ = "firm"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ticker = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Firm {self.name}"


class Watchlist(db.Model):
    __tablename__ = "watchlist"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    ticker = db.Column(db.String)
    date = db.Column(db.DateTime, nullable=True, default=datetime.date.today().strftime('%Y-%m-%d'))
    memo = db.Column(db.Text)
    firm_id = db.Column(db.Integer, db.ForeignKey('firm.id'))

    firms = db.relationship("Firm", backref="watchlist")

    def __repr__(self):
        return f"{self.name} information"

def get_tickers():
    if len(Firm.query.all()) == 0:
        krpath = os.path.join(os.getcwd(), 'KOSPI_symbol.csv')
        with open(krpath, encoding='cp949') as f:
            reader = csv.DictReader(f)
            for each in reader:
                firm = Firm(
                    ticker = str(each['code'].zfill(6)) + '.KS',
                    name = str(each['engname'].upper())
                )
                db.session.add(firm)
        db.session.commit()

        enpath = os.path.join(os.getcwd(), 'NASDAQ.txt')
        with open (enpath, encoding='utf8') as f:
            for each in f:
                one = each.strip().split('\t')
                firm = Firm(
                    ticker = one[0],
                    name = one[1].upper()
                )
                db.session.add(firm)
        db.session.commit()
        

    return "List Uploaded"

def get_table():

    return Watchlist.query.all()


def add_list(name=None, ticker=None, date=None, memo=None):

    if (name == '') & (ticker == '') :
        return "Name or Code needed", None
    
    if ticker != '':
        new = Firm.query.filter(Firm.ticker==ticker).first()
    elif name != '':
        new = Firm.query.filter(Firm.name.like('%{}%'.format(name))).first()
    
    if new is None:
        return "No such a firm", None
    
    
    new_firm = Watchlist(
        name = new.name,
        ticker = new.ticker,
        date = date,
        memo = memo)

    existing = Watchlist.query.filter(Watchlist.ticker == new_firm.ticker).first()

    if existing is not None:
        db.session.delete(existing)
        db.session.add(new_firm)
        db.session.commit()
        return "List updated", True

    elif existing is None:
        db.session.add(new_firm)
        db.session.commit()
        return "Created on list", True

def delete_list(ticker):
    firm = Watchlist.query.filter(Watchlist.ticker==ticker).first()
    if firm is None:
        return None
    db.session.delete(firm)
    db.session.commit()
    return True

