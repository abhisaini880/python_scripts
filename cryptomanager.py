from tkinter import *
import requests
import json


crypto = Tk()
crypto.title("Crypto Manager")

crypto.iconbitmap('Icons/crypto_o2.ico')


def font_color(amount, mark):
    if( amount >= mark):
        return "#299c17"
    else:
        return "#d12115"


def crypto_cal():
    api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")

    api = json.loads(api_request.content)

    coins = [
        {
            "symbol":"BTC",
            "coins_owned":2,
            "price_per_coin":3200
        },
        {
            "symbol":"XRP",
            "coins_owned": 400,
            "price_per_coin": 1
        },
        {
            "symbol":"ETH",
            "coins_owned": 20,
            "price_per_coin": 100
        },
        {
            "symbol":"LTC",
            "coins_owned": 50,
            "price_per_coin": 80
        }
    ]

    total_PL = 0
    row_count = 1
    total_invest = 0

    for i in range(50):
        for coin in coins:
            if(api[i]["symbol"] == coin["symbol"]):

                total_coins = coin["coins_owned"]
                total_amount_paid = coin["price_per_coin"] * total_coins
                current_value = float(api[i]["price_usd"]) * total_coins
                total_pl_per_coin = float(api[i]["price_usd"]) - coin["price_per_coin"]
                total_pl = total_pl_per_coin * total_coins
                total_PL+= total_pl
                total_invest += total_amount_paid

                name = Label(crypto, text=api[i]["name"], bg="#F5F4EB", fg="black", font="Bitner 12", padx="5", pady="5", borderwidth="2", relief="groove")
                name.grid(row=row_count, column=0, sticky=N+E+S+W)

                price = Label(crypto, text="{0:.2f}".format(float(api[i]['price_usd'])), bg="#F5F4EB", fg="black", font="Bitner 12", padx="5", pady="5", borderwidth="2", relief="groove")
                price.grid(row=row_count, column=1, sticky=N+E+S+W)

                no_coins = Label(crypto, text=total_coins, bg="#F5F4EB", fg="black", font="Bitner 12", padx="5", pady="5", borderwidth="2", relief="groove")
                no_coins.grid(row=row_count, column=2, sticky=N+E+S+W)

                amount_paid = Label(crypto, text=total_amount_paid, bg="#F5F4EB", fg="black", font="Bitner 12", padx="5", pady="5", borderwidth="2", relief="groove")
                amount_paid.grid(row=row_count, column=3, sticky=N+E+S+W)

                current_val = Label(crypto, text="{0:.2f}".format(current_value), bg="#F5F4EB", fg=font_color(float("{0:.2f}".format(current_value)),float(total_amount_paid)), font="Bitner 12", padx="5", pady="5", borderwidth="2", relief="groove")
                current_val.grid(row=row_count, column=4, sticky=N+E+S+W)

                pl_per_coin = Label(crypto, text="{0:.2f}".format(total_pl_per_coin), bg="#F5F4EB", fg="black", font="Bitner 12", padx="5", pady="5", borderwidth="2", relief="groove")
                pl_per_coin.grid(row=row_count, column=5, sticky=N+E+S+W)

                total_pl = Label(crypto, text="{0:.2f}".format(total_pl), bg="#F5F4EB", fg=font_color(float("{0:.2f}".format(total_pl)),0), font="Bitner 12", padx="5", pady="5", borderwidth="2", relief="groove")
                total_pl.grid(row=row_count, column=6, sticky=N+E+S+W)

                row_count+=1
    
    all_total_pl = Label(crypto, text="{0:.2f}".format(total_PL), bg="#F5F4EB", fg=font_color(float("{0:.2f}".format(total_PL)),float(total_invest)), font="Bitner 12", padx="5", pady="5", borderwidth="2", relief="groove")
    all_total_pl.grid(row=row_count, column=6, sticky=N+E+S+W)

    refresh = Button(crypto, text="Refresh", bg="#FFE361", fg="#000000", command=crypto_cal, font="Zefani 12 bold", padx="5", pady="5", borderwidth="2", relief="groove")
    refresh.grid(row=row_count+1, column=6, sticky=N+E+S+W)   
# refesh = Label(crypto, text="{0:.2f}".format(total_PL), bg="#F5F4EB", fg=font_color(float("{0:.2f}".format(total_PL)),float(total_invest)), font="Bitner 12", padx="5", pady="5", borderwidth="2", relief="groove")
# refresh.grid(row=row_count+1, column=6, sticky=N+E+S+W)    

name = Label(crypto, text="Currency Name", bg="#FFE361", fg="#000000", font="Zefani 12 bold", padx="5", pady="5",borderwidth="2", relief="groove")
name.grid(row=0, column=0, sticky=N+E+S+W)

price = Label(crypto, text="Price", bg="#FFE361", fg="#000000", font="Zefani 12 bold", padx="5", pady="5",borderwidth="2", relief="groove")
price.grid(row=0, column=1, sticky=N+E+S+W)

no_coins = Label(crypto, text="Coins Owned", bg="#FFE361", fg="#000000", font="Zefani 12 bold", padx="5", pady="5",borderwidth="2", relief="groove")
no_coins.grid(row=0, column=2, sticky=N+E+S+W)

amount_paid = Label(crypto, text="Amount Invested", bg="#FFE361", fg="#000000", font="Zefani 12 bold", padx="5", pady="5",borderwidth="2", relief="groove")
amount_paid.grid(row=0, column=3, sticky=N+E+S+W)

current_val = Label(crypto, text="Current Value", bg="#FFE361", fg="#000000", font="Zefani 12 bold", padx="5", pady="5",borderwidth="2", relief="groove")
current_val.grid(row=0, column=4, sticky=N+E+S+W)

pl_per_coin = Label(crypto, text="Profit/Loss per Coin", bg="#FFE361", fg="#000000", font="Zefani 12 bold", padx="5", pady="5",borderwidth="2", relief="groove")
pl_per_coin.grid(row=0, column=5, sticky=N+E+S+W)

total_pl = Label(crypto, text="Total Profit/Loss", bg="#FFE361", fg="#000000", font="Zefani 12 bold", padx="5", pady="5",borderwidth="2", relief="groove")
total_pl.grid(row=0, column=6, sticky=N+E+S+W)


crypto_cal()

crypto.mainloop()