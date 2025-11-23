import pytest
import json
from project import Asset, Portfolio, estimate_portfolio_value, track_profit_loss, get_current_price

'''
monkeypatch -> temporarily replaces function/objects
tmp_path -> creates temporary directory for file I/O
'''


#------TEST ASSET CLASS------#
def test_asset_creation():
    x = Asset("BTC-USD", 1, 100000)
    assert x.symbol == "BTC-USD"
    assert x.quantity == 1
    assert x.buy_price == 100000
    assert x.asset_type == "Crypto"

def test_profit_loss_calculation(monkeypatch):
    x = Asset("TEST", 4, 100)
    x.current_price = lambda : 120
    assert x.profit_loss() == 80  # (120-100) * 4

def test_current_value_calculation(monkeypatch):
    x = Asset("TEST", 2, 1000)
    x.current_price = lambda : 1500
    assert x.current_value() == 3000

#--------TEST PORTFOLIO CLASS--------#
def test_add_and_value_assets(monkeypatch, tmp_path):
    portfolio = Portfolio()
    #   x and y are two assets
    x = Asset("BTC-USD", 1, 120000)
    y = Asset("AAPL", 2, 200)

    x.current_price = lambda : 125000
    y.current_price = lambda : 220

    portfolio.add_stock(x)
    portfolio.add_stock(y)

    # Total value -> (12500*1) + (220*2) = 125440
    assert round(portfolio.total_value(), 2) == 125440

    #Total Profit/Loss -> [(125000-120000)*1] + [(220-200)*2] = 5040
    assert round(portfolio.total_profit_loss(), 2) == 5040


def test_save_and_load_file(tmp_path, monkeypatch):
    test_file = tmp_path / "portfolio.json"
    portfolio = Portfolio()
    x = Asset("ETH-USD", 1, 2750)
    portfolio.add_stock(x)

    # Save portfolio

    portfolio.save_to_file(test_file)
    assert test_file.exists()


    # Load new portfolio
    new_portfolio = Portfolio()
    new_portfolio.load_from_file(test_file)

    assert len(new_portfolio.holdings) == 1
    assert new_portfolio.holdings[0].symbol == "ETH-USD"
    assert new_portfolio.holdings[0].buy_price == 2750

#-------TEST REQUIRED FUNCTIONS------#

def test_estimate_portfolio_value(monkeypatch):
    portfolio = Portfolio()
    x = Asset("AMZN", 4, 240)
    x.current_price = lambda : 250
    portfolio.add_stock(x)
    assert estimate_portfolio_value(portfolio) == 1000

def test_track_profit_loss(monkeypatch):
    portfolio = Portfolio()
    x = Asset("AAPL", 2, 240)
    x.current_price = lambda : 260
    portfolio.add_stock(x)
    assert track_profit_loss(portfolio) == 40

