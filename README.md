# Energy_Trading_API
Most important database file named trades.sqlite should be in the same directory where we run python codes as we are reading from this db.
compute_total_buy.py for task1a
compute_total_sell.py for task1b
compute_value-> for PnL caclulcation. This file to be called from the yml file.
get_pnl.yml-> The .yml file. Once we runt this file we will get the strategy with PnL value.
Execution of .yml file can be done in different ways. One way use the following command: 
connexion run get_pnl.yml -v
