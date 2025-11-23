import yfinance as yf
from tabulate import tabulate
import json
import os

#_________________STOCK / CRYPTO CLASS__________________#
class Asset:

    def __init__(self, symbol, quantity, buy_price):

        self.symbol = symbol.upper()
        self.quantity = quantity
        self.buy_price = buy_price
        self.asset_type = self._detect_asset_type()

    def _detect_asset_type(self):

        #Cheking if it's stock or crypto

        if "-USD" in self.symbol :
            return "Crypto"
        return "Stocks"

    def current_price(self):

        #Fetching current stock/crypto price using yfinance

        ticker = yf.Ticker(self.symbol)
        data = ticker.history(period = "1d")

        if data.empty:
            raise ValueError(f"Not able to fetch data for {self.symbol}")
        return round(data["Close"].iloc[-1], 2)

    def current_value(self):

        #Returns total current value

        return round(self.quantity * self.current_price(), 2)

    def profit_loss(self):

        #Calculates profit and loss

        return round((self.current_price() - self.buy_price) * self.quantity, 2)

    def to_dict(self):
        return {
            "symbol" : self.symbol,
            "quantity" : self.quantity,
            "buy_price" : self.buy_price
        }

    @staticmethod
    def from_dict(data):
        return Asset(data["symbol"], data["quantity"], data["buy_price"])



# _________________PORTFOLIO CLASS_________________#
class Portfolio:

    def __init__(self):
        self.holdings = []

    def add_stock(self, stock):
        self.holdings.append(stock)
        self.save_to_file()

    def remove_stock(self, symbol):
        symbol = symbol.upper()
        for s in self.holdings:
            if s.symbol == symbol:
                self.holdings.remove(s)
                self.save_to_file()
                print(f"🗑️ {symbol} removed successfully!!")
                return
        print("⚠️ Asset not found in your portfolio")

    def total_value(self):
       t1 = 0
       for stock in self.holdings:
           t1 += stock.current_value()
       return t1

    def total_profit_loss(self):
        t2 = 0
        for stock in self.holdings:
            t2 += stock.profit_loss()
        return t2


    def list_assets(self):

        #List assets in tabular form

        stocks = [s for s in self.holdings if s.asset_type == "Stocks"]
        cryptos = [s for s in self.holdings if s.asset_type == "Crypto"]

        print("\n 📊  Your Portifolio Breakdown  📊")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        def display_table(title, assets):
            if not assets:
                return
            rows = []
            for s in assets:
                try:
                    rows.append([
                        s.symbol,
                        f"{s.quantity}",
                        f"${s.buy_price:.2f}",
                        f"${s.current_price():.2f}",
                        f"${s.profit_loss():.2f}",
                    ])
                except Exception:

                        rows.append([
                            s.symbol,
                            s.quantity,
                            s.buy_price(),
                            "N/A",
                            "N/A"

                        ])

            print(f"\n{title}")
            print(tabulate(
                rows,
                headers=["Symbol", "Quantity", "Buy Price", "Current Price", "Profit/Loss"],
                tablefmt = "rounded_grid"
            ))

        if stocks:
            display_table("📈  STOCKS", stocks)
        if cryptos:
            display_table("🪙  CRYPTOS", cryptos)
        if not stocks and not cryptos:
            print("No Holdings Yet")

        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

#----------SAVE / LOAD FILE----------#
    def save_to_file(self, filename= "portfolio.json"):
        data = [s.to_dict() for s in self.holdings]
        with open(filename, "w") as f:
            json.dump(data, f, indent = 4)

    def load_from_file(self,filename = "portfolio.json"):
        if not os.path.exists(filename):
            return
        with open(filename, "r") as f:
            data = json.load(f)
            self.holdings  = [Asset.from_dict(d) for d in data]


#--------------Required Functions---------------#
def estimate_portfolio_value(portfolio):
    return portfolio.total_value()

def track_profit_loss(portfolio):
    return portfolio.total_profit_loss()

def get_current_price(symbol):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period="1d")
    if data.empty:
        raise ValueError(f"Could not fetch data for {symbol}")
    return round(data["Close"].iloc[-1], 2)




#----------------------MAIN-----------------------#

def main():
    print("Welcome to Portfolio Tracker  📊")
    portfolio = Portfolio()

    while True:

        print("\n Options")
        print("1️⃣ Add Asset (Stock/Crypto)")
        print("2️⃣ Estimate Portfolio Value")
        print("3️⃣ Track Profit/Loss")
        print("4️⃣ Show Portfolio Breakdown")
        print("5️⃣ Get Current Price")
        print("6️⃣ Remove Asset")
        print("7️⃣ Exit\n")

        choice = (input("Enter your choice [1-6]: "))

        if choice == "1":
            symbol = input("Enter symbol of asset: ").upper()
            quantity = float(input("Enter quantity of asset: "))
            buy_price = float(input("Enter buy price: "))
            asset = Asset(symbol, quantity, buy_price)
            portfolio.add_stock(asset)
            print(f"✅   {asset.symbol} ({asset.asset_type}) added successfully!")


        elif choice == "2":
            try:
                total_value = estimate_portfolio_value(portfolio)
                print(f"💰  Your Portfolio Value: ${total_value:.2f}")
            except Exception as e:
                print("Error", e)

        elif choice == "3":
            try:
                profit_loss = track_profit_loss(portfolio)
                print(f" Total Profit/Loss: ${profit_loss:.2f}")
            except Exception as e:
                print("Error", e)

        elif choice == "4":
            portfolio.list_assets()

        elif choice == "5":
            symbol = input("Enter symbol of your asset: ").upper()
            try:
                price = get_current_price(symbol)
                print(f"Current Price of {symbol}: ${price}")
            except Exception as e:
                print("Error", e)

        elif choice == "6":
            symbol = input("Enter the symbol to remove: ")
            portfolio.remove_stock(symbol)


        elif choice == "7":
            print("Exiting........Goodbye👋")
            break

        else:
            print("Invalid Choice. Try Again!!")

if __name__ == "__main__":
    main()