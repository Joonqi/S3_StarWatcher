# api.py

from app.models import Firm, Watchlist
import yfinance as yf
from pmdarima.arima import auto_arima
from datetime import date, timedelta
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt



def plot_graph(ticker):
    
    new_file = f'img{ticker}_{str(date.today()).split(" ")[0]}.png'
    name = Firm.query.filter(Firm.ticker==ticker).first().name
    price = get_prices(ticker)
    plt.plot(price)
    plt.ylim(ymin=0)
    plt.title(f"{name}")
    plt.grid(True, axis='y')
    plt.savefig('app/static/' + new_file, dpi=400)
    plt.close('all')
    
    return new_file

def get_prices(ticker):
    target = yf.Ticker(ticker)
    prices = target.history(start='2015-01-01')

    return prices['Close']

def get_recommend(ticker):
    target = yf.Ticker(ticker)
    recommend = target.recommendations[-10:]

    return recommend

def get_forecast(ticker):
    target = get_prices(ticker)
    returns = 100 * target.pct_change().dropna()
    lastday = returns.index[-1]
    name = Firm.query.filter(Firm.ticker==ticker).first().name

    model = auto_arima(returns, start_p=0, start_q=0)
    forecast = model.predict(n_periods=1)

    today = lastday + timedelta(days=1)
    td = today.strftime('%Y-%m-%d')

    return td, name, round(float(forecast), 6)
