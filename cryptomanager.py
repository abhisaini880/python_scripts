from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import requests
import json
import sqlite3

# connecting database
con = sqlite3.connect('crypto.db')
cursor = con.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS  coin(id INTEGER PRIMARY KEY, symbol TEXT, quantity INTEGER, price REAL)')
con.commit()

cursor.execute('CREATE TABLE IF NOT EXISTS  coin_symbol(id INTEGER PRIMARY KEY, symbol TEXT)')
con.commit()

# creating root window
crypto = Tk()
crypto.title("Crypto Manager")
crypto.resizable(False, False)

# Icon for app
crypto.iconbitmap('Icons/crypto_o2.ico')

# font color for profit/loss amount
def font_color(amount, mark):
    if( amount >= mark):
        return "#299c17"
    else:
        return "#d12115"

class Placeholder_State(object):
     __slots__ = 'normal_color', 'normal_font', 'placeholder_text', 'placeholder_color', 'placeholder_font', 'with_placeholder'

def add_placeholder_to(entry, placeholder, color="grey", font=None):
    normal_color = entry.cget("fg")
    normal_font = entry.cget("font")
    
    if font is None:
        font = normal_font

    state = Placeholder_State()
    state.normal_color=normal_color
    state.normal_font=normal_font
    state.placeholder_color=color
    state.placeholder_font=font
    state.placeholder_text = placeholder
    state.with_placeholder=True

    def on_focusin(event, entry=entry, state=state):
        if state.with_placeholder:
            entry.delete(0, "end")
            entry.config(fg = state.normal_color, font=state.normal_font)
        
            state.with_placeholder = False

    def on_focusout(event, entry=entry, state=state):
        if entry.get() == '':
            entry.insert(0, state.placeholder_text)
            entry.config(fg = state.placeholder_color, font=state.placeholder_font)
            
            state.with_placeholder = True

    entry.insert(0, placeholder)
    entry.config(fg = color, font=font)

    entry.bind('<FocusIn>', on_focusin, add="+")
    entry.bind('<FocusOut>', on_focusout, add="+")
    
    entry.placeholder_state = state

    return state

def reset():
    for widgets in crypto.winfo_children():
        widgets.destroy()
    
    app_header()
    crypto_cal()    

def delete_all():
    cursor.execute("DELETE from coin")
    con.commit()

    reset()

def crypto_cal():
    api_request = requests.get("https://api.coinmarketcap.com/v1/ticker/")

    api = json.loads(api_request.content)

    def insert_coin():
        cursor.execute("INSERT INTO coin(symbol,quantity,price) VALUES(?,?,?)", (entry_1.get(), entry_2.get(), entry_3.get()))
        con.commit()
        reset()

    def insert_symbol(symbol):
        cursor.execute("INSERT INTO coin_symbol(symbol) VALUES(?)", (symbol,))
        con.commit()

    def delete_coin():
        cursor.execute("DELETE from coin where id=?",(entry_4.get(),))
        con.commit()
        reset()

    def delete_symbol():
        cursor.execute("DELETE from coin_symbol ")
        con.commit()

    cursor.execute("select * from coin")
    coins = cursor.fetchall()

    total_PL = 0
    row_count = 1
    total_invest = 0

    delete_symbol()
    for i in range(10):
        
        insert_symbol(api[i]["symbol"])

    for i in range(50):

        for coin in coins:
            if(api[i]["symbol"] == coin[1]):

                total_coins = coin[2]
                total_amount_paid = coin[3] * total_coins
                current_value = float(api[i]["price_usd"]) * total_coins
                total_pl_per_coin = float(api[i]["price_usd"]) - coin[3]
                total_pl = total_pl_per_coin * total_coins
                total_PL+= total_pl
                total_invest += total_amount_paid
                
                id = Label(crypto, text=coin[0], bg="#F5F4EB", fg="black", font="Bitner 12", padx="5", pady="5", borderwidth="2", relief="groove")
                id.grid(row=row_count, column=0, sticky=N+E+S+W)

                name = Label(crypto, text=api[i]["name"], bg="#F5F4EB", fg="black", font="Bitner 12", padx="5", pady="5", borderwidth="2", relief="groove")
                name.grid(row=row_count, column=1, sticky=N+E+S+W)

                price = Label(crypto, text="{0:.2f}".format(float(api[i]['price_usd'])), bg="#F5F4EB", fg="black", font="Bitner 12", padx="5", pady="5", borderwidth="2", relief="groove")
                price.grid(row=row_count, column=2, sticky=N+E+S+W)

                no_coins = Label(crypto, text=total_coins, bg="#F5F4EB", fg="black", font="Bitner 12", padx="5", pady="5", borderwidth="2", relief="groove")
                no_coins.grid(row=row_count, column=3, sticky=N+E+S+W)

                amount_paid = Label(crypto, text=total_amount_paid, bg="#F5F4EB", fg="black", font="Bitner 12", padx="5", pady="5", borderwidth="2", relief="groove")
                amount_paid.grid(row=row_count, column=4, sticky=N+E+S+W)

                current_val = Label(crypto, text="{0:.2f}".format(current_value), bg="#F5F4EB", fg=font_color(float("{0:.2f}".format(current_value)),float(total_amount_paid)), font="Bitner 12", padx="5", pady="5", borderwidth="2", relief="groove")
                current_val.grid(row=row_count, column=5, sticky=N+E+S+W)

                pl_per_coin = Label(crypto, text="{0:.2f}".format(total_pl_per_coin), bg="#F5F4EB", fg="black", font="Bitner 12", padx="5", pady="5", borderwidth="2", relief="groove")
                pl_per_coin.grid(row=row_count, column=6, sticky=N+E+S+W)

                total_pl = Label(crypto, text="{0:.2f}".format(total_pl), bg="#F5F4EB", fg=font_color(float("{0:.2f}".format(total_pl)),0), font="Bitner 12", padx="5", pady="5", borderwidth="2", relief="groove")
                total_pl.grid(row=row_count, column=7, sticky=N+E+S+W)

                row_count+=1
    
    
    cursor.execute('select symbol from coin_symbol')
    symbol_data = cursor.fetchall()

    all_total_pl = Label(crypto, text="{0:.2f}".format(total_PL), bg="#F5F4EB", fg=font_color(float("{0:.2f}".format(total_PL)),float(total_invest)), font="Bitner 12", padx="5", pady="5", borderwidth="2", relief="groove")
    all_total_pl.grid(row=row_count, column=7, sticky=N+E+S+W)

    refresh = Button(crypto, text="Refresh", bg="#FFE361", fg="#000000", command=reset, font="Zefani 12 bold", padx="5", pady="5", borderwidth="2", relief="groove")
    refresh.grid(row=row_count+1, column=7, sticky=N+E+S+W)

    add_btn = Button(crypto, text="ADD", bg="#FFE361", fg="#000000", command=insert_coin, font="Zefani 12 bold", padx="5", pady="5", borderwidth="2", relief="groove")
    add_btn.grid(row=row_count+1, column=0, sticky=N+E+S+W) 

    del_btn = Button(crypto, text="DELETE", bg="#FFE361", fg="#000000", command=delete_coin, font="Zefani 12 bold", padx="5", pady="5", borderwidth="2", relief="groove")
    del_btn.grid(row=row_count+2, column=0, sticky=N+E+S+W) 


    entry_1 = ttk.Combobox(crypto, values=symbol_data)
    entry_1.grid(row=row_count+1, column=1, sticky=N+E+S+W)

    entry_2 = Entry(crypto, bd=1, bg="white", highlightbackground="#bebebe", highlightthickness=1)
    entry_2.grid(row=row_count+1, column=2, sticky=N+E+S+W)
    add_placeholder_to(entry_2, 'Coins Owned')

    entry_3 = Entry(crypto, bd=1, bg="white", highlightbackground="#bebebe", highlightthickness=1)
    entry_3.grid(row=row_count+1, column=3, sticky=N+E+S+W)
    add_placeholder_to(entry_3, 'Amount spent')

    entry_4 = Entry(crypto, bd=1, bg="white", highlightbackground="#bebebe", highlightthickness=1)
    entry_4.grid(row=row_count+2, column=1, sticky=N+E+S+W)
    add_placeholder_to(entry_4, 'Coin ID')

def app_header(): 
    
    menubar = Menu(crypto)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="clear all", command=delete_all)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=crypto.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    crypto.config(menu=menubar)

    id = Label(crypto, text="Coin ID", bg="#FFE361", fg="#000000", font="Zefani 12 bold", padx="5", pady="5",borderwidth="2", relief="groove")
    id.grid(row=0, column=0, sticky=N+E+S+W)

    name = Label(crypto, text="Currency Name", bg="#FFE361", fg="#000000", font="Zefani 12 bold", padx="5", pady="5",borderwidth="2", relief="groove")
    name.grid(row=0, column=1, sticky=N+E+S+W)

    price = Label(crypto, text="Price", bg="#FFE361", fg="#000000", font="Zefani 12 bold", padx="5", pady="5",borderwidth="2", relief="groove")
    price.grid(row=0, column=2, sticky=N+E+S+W)

    no_coins = Label(crypto, text="Coins Owned", bg="#FFE361", fg="#000000", font="Zefani 12 bold", padx="5", pady="5",borderwidth="2", relief="groove")
    no_coins.grid(row=0, column=3, sticky=N+E+S+W)

    amount_paid = Label(crypto, text="Amount Invested", bg="#FFE361", fg="#000000", font="Zefani 12 bold", padx="5", pady="5",borderwidth="2", relief="groove")
    amount_paid.grid(row=0, column=4, sticky=N+E+S+W)

    current_val = Label(crypto, text="Current Value", bg="#FFE361", fg="#000000", font="Zefani 12 bold", padx="5", pady="5",borderwidth="2", relief="groove")
    current_val.grid(row=0, column=5, sticky=N+E+S+W)

    pl_per_coin = Label(crypto, text="Profit/Loss per Coin", bg="#FFE361", fg="#000000", font="Zefani 12 bold", padx="5", pady="5",borderwidth="2", relief="groove")
    pl_per_coin.grid(row=0, column=6, sticky=N+E+S+W)

    total_pl = Label(crypto, text="Total Profit/Loss", bg="#FFE361", fg="#000000", font="Zefani 12 bold", padx="5", pady="5",borderwidth="2", relief="groove")
    total_pl.grid(row=0, column=7, sticky=N+E+S+W)


app_header()

crypto_cal()

crypto.mainloop()

# close database connection
cursor.close()
con.close()