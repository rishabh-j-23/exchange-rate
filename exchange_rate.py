import os
import requests
import json

class ExchangeRate:
    def __init__(self):
        self.headers= {
            "apikey": "F6xQ7O8umovGHsFqg8WT9oGOa4zEg01M"
            }

    def convert(self, fromCurr: str, toCurr: str, amount):
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={toCurr}&from={fromCurr}&amount={amount}"
        payload = {}
        response = requests.request("GET", url, headers=self.headers, data=payload).json()
        rate = response['result']
        return rate

    def fluctuation(self, curr: str, start_date: str, end_date: str):
        """
        put dates in yyyy-mm-dd format
        """
        url = f"https://api.apilayer.com/exchangerates_data/fluctuation?start_date={start_date}&end_date={end_date}&symbols={curr}"
        payload = {}
        response = requests.request("GET", url, headers=self.headers, data = payload).json()
        base = response['rates']['INR']

        return base['start_rate'], base['end_rate'], base['change'], base['change_pct']

    def latest_rate(self, symbols: str):
        url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}"
        payload = {}
        response = requests.request("GET", url, headers=self.headers, data = payload).json()
        latest = response["rates"]
        return latest[symbols]

    def list_all_symbols(self):
        url = f"https://api.apilayer.com/exchangerates_data/symbols"
        payload = {}
        response = requests.request("GET", url, headers=self.headers, data = payload).json()
    
        return response['symbols']

    def symbol_name(self, symbol: str):
        url = f"https://api.apilayer.com/exchangerates_data/symbols"
        payload = {}
        response = requests.request("GET", url, headers=self.headers, data = payload).json()
        return response['symbols'][symbol]

    def get_data_between_dates(self, start_date, end_date, symbol):
        url = f"https://api.apilayer.com/exchangerates_data/timeseries?start_date={start_date}&end_date={end_date}&symbols={symbol}"
        payload = {}
        response = requests.request("GET", url, headers=self.headers, data = payload).json()
        dates = response['rates']
        print("Date             Rate")
        for date in dates:
            print(f"{date}      {dates[date][symbol]}")


    