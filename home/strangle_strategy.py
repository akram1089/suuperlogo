import pandas as pd
import yfinance as yf
import numpy as np

def fetch_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data

def strangle_backtest(stock_data, call_strike, put_strike, expiration_date, initial_capital):
    # Check if the expiration_date is in the stock_data DataFrame
    if expiration_date not in stock_data.index:
        raise ValueError(f"Expiration date {expiration_date} is not available in the stock_data.")

    # Buy the call and put options at the specified strike prices and expiration date
    call_option = stock_data.loc[stock_data.index == expiration_date, 'Open'].values[0] - call_strike
    put_option = put_strike - stock_data.loc[stock_data.index == expiration_date, 'Open'].values[0]

    # Calculate total investment cost
    total_cost = call_option + put_option

    # Compute the profit/loss for each trading day
    stock_data['Strangle_PnL'] = stock_data['Open'] - (stock_data['Open'].shift(1) + total_cost)

    # Calculate cumulative PnL
    stock_data['Cumulative_PnL'] = stock_data['Strangle_PnL'].cumsum()

    # Calculate the number of contracts we can buy with initial capital
    num_contracts = int(initial_capital // total_cost)

    # Calculate the final PnL
    final_pnl = num_contracts * stock_data.iloc[-1]['Strangle_PnL']

    # Calculate max profit and max loss
    max_profit = np.inf if call_strike > stock_data['Open'].max() else final_pnl
    max_loss = -total_cost

    # Calculate breakeven points
    breakeven_upper = call_strike + total_cost
    breakeven_lower = put_strike - total_cost

    # Calculate reward-risk ratio
    reward_risk_ratio = max_profit / abs(max_loss)

    return stock_data, final_pnl, max_profit, max_loss, breakeven_upper, breakeven_lower, reward_risk_ratio
