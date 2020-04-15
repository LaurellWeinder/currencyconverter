import urllib.request
import json
from typing import Dict



class CurrencyConverter:
    def __init__(self, url: str):
        req = urllib.request.Request(url, headers={'User-Agent':'*'})
        data = urllib.request.urlopen(req).read()
        self.data = json.loads(data.decode('utf-8'))
        self.rates = self.data['rates']

    def convert(self, from_currency: str, to_currency: str, amount: str) -> Dict[str, str]:
        if from_currency == 'RUB':
            answer = {'from_currency': from_currency,
                      'to_currency': to_currency,
                      'amount': amount,
                      'result': round(int(amount) * self.rates[to_currency], 2)}
            return answer
        elif from_currency == 'USD':
            answer = {'from_currency': from_currency,
                      'to_currency': to_currency,
                      'amount': amount,
                      'result': round(int(amount) / self.rates[from_currency], 2)}
            return answer
