import requests
import json

class ExchangeRate:
    def __init__(self):
        self.headers= {
            "apikey": "F6xQ7O8umovGHsFqg8WT9oGOa4zEg01M"
            }
        self.api = "https://api.apilayer.com/exchangerates_data"


    def convert(self, fromCurr: str, toCurr: str, amount):
        url = f"{self.api}/convert?to={toCurr}&from={fromCurr}&amount={amount}"
        payload = {}
        response = requests.request("GET", url, headers=self.headers, data=payload).json()
        rate = response['result']
        return rate

    def fluctuation(self, curr: str, start_date: str, end_date: str):
        """
        put dates in yyyy-mm-dd format
        """
        url = f"{self.api}/fluctuation?start_date={start_date}&end_date={end_date}&symbols={curr}"
        payload = {}
        response = requests.request("GET", url, headers=self.headers, data = payload).json()
        base = response['rates']['INR']

        return base['start_rate'], base['end_rate'], base['change'], base['change_pct']

    def latest_rate(self, symbols: str):
        url = f"{self.api}/latest?symbols={symbols}"
        payload = {}
        response = requests.request("GET", url, headers=self.headers, data = payload).json()
        latest = response["rates"]
        return latest[symbols]

    def list_all_symbols(self):
        url = f"{self.api}/symbols"
        payload = {}
        response = requests.request("GET", url, headers=self.headers, data = payload).json()
    
        return response['symbols']

    def symbol_name(self, symbol: str):
        symbol = symbol.capitalize()
        url = f"{self.api}/symbols"
        payload = {}
        try:
        
            response = requests.request("GET", url, headers=self.headers, data = payload).json()
            return response['symbols'][symbol]
        except:
            return "Symbol doesnt Exists"
    
    def get_data_between_dates(self, start_date, end_date, symbol):
        url = f"{self.api}/timeseries?start_date={start_date}&end_date={end_date}&symbols={symbol}&base=USD"
        payload = {}
        response = requests.request("GET", url, headers=self.headers, data = payload).json()
        dates = response['rates']
        print("Date             Rate")
        d = []
        r = []    
        for date in dates:
            d.append(date)
            r.append(dates[date][symbol])
            print(f"{date}      {dates[date][symbol]}")
        
        return d, r


    