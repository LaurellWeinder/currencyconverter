#!/usr/bin/env python
import cgi
import html
from currencyconverter import *

CUR_URL = 'https://api.exchangeratesapi.io/latest?base=RUB'


def main():
    form = cgi.FieldStorage()
    amount = form.getvalue('amount', 0)
    from_currency = form.getvalue('from_currency', 'RUB')
    to_currency = form.getvalue('to_currency', 'USD')
    amount = html.escape(amount)
    from_currency = html.escape(from_currency)
    to_currency = html.escape(to_currency)
    converter = CurrencyConverter(CUR_URL)
    answer = converter.convert(from_currency, to_currency, amount)
    json_answer = json.dumps(answer)
    process_input(answer, json_answer)


def process_input(answer: dict, json_answer: json):
    print('Content-type: text/html\n')
    print('''<!DOCTYPE HTML>
            <html>
            <head>
                <meta charset="utf-8">
                <title>Конвертатор валют</title>
            </head>
            <body>''')
    print('<h1>Результат: </h1>')
    print(f'<p>{answer["amount"]} {answer["from_currency"]} = {answer["result"]} {answer["to_currency"]}</p>')
    print(f'<p>{json_answer}')
    print('''</body>
            </html>''')


if __name__ == '__main__':
    main()
