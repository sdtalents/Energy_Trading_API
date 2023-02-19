import sqlite3
import pandas as pd

def compute_total_buy_volume (*args, **kwargs) -> float:
    total_buy_volume=args[0]
    df=args[1]
    side_list = df['side'].tolist()
    df['amount'] = df.price * df.quantity
    amount_list = df['amount'].tolist()
    amount_index=0
    for side in side_list:
        if side == "buy":
            total_buy_volume+= amount_list[amount_index]
        amount_index+=1
    #print("total_buy_volume = ",total_buy_volume)
    return total_buy_volume



conn = sqlite3.connect('trades.sqlite')
trades = pd.read_sql('SELECT * FROM epex_12_20_12_13' ,conn)
total_buy_volume= 0.0
total_buy_volume= compute_total_buy_volume(total_buy_volume,trades)
print("total_buy_volume", total_buy_volume)
