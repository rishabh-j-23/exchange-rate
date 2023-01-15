from exchange_rate import ExchangeRate
import json

rate = ExchangeRate()

run_menu = 1
while run_menu == 1:
    print("1. Convert Currency")
    print("2. Curreny Fluctuations")
    print("3. Latest Currency Rate")
    print("4. List all Symbols")
    print("5. Search for Symbol name")
    print("6. Print data between dates")

    res = int(input("Response : "))

    if res == 1:
        fromCurr = input("From Currency : ")
        toCurr = input("To Currency : ")
        amount = float(input("Amount : "))
        convert = rate.convert(fromCurr, toCurr, amount)
        print(f"{amount} {fromCurr} to {toCurr} : {convert}")

    elif res == 2:
        curr = input("Currency : ")
        start_date = input("Start Date (yyyy-mm-dd) : ")
        end_date = input("End Date (yyyy-mm-dd) : ")
        start_rate, end_rate, change, change_pct = rate.fluctuation(curr, start_date, end_date)
        print(f"""
        Start rate : {start_rate}
        End rate : {end_rate}
        Change : {change}
        %Change : {change_pct}
        """)
    
    elif res == 3:
        curr = input("Currency : ")
        print("Latest rate : ", rate.latest_rate(curr))

    elif res == 4:
        print(rate.list_all_symbols())

    elif res == 5:
        symbol = input("Symbol to search : ")
        print(f"{symbol} : {rate.symbol_name(symbol)}")
    
    elif res == 6:
        symbol = input("Currency : ")
        start_date = input("Start Date (yyyy-mm-dd) : ")
        end_date = input("End Date (yyyy-mm-dd) : ")
        rate.get_data_between_dates(start_date, end_date, symbol)

    run_menu = int(input("Go back to menu? (1/0) : "))