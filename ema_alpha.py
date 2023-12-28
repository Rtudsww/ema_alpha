import yfinance as yf

list=['ADANIENT.NS', 'ADANIPORTS.NS', 'APOLLOHOSP.NS', 'ASIANPAINT.NS', 'AXISBANK.NS', 'BAJAJ-AUTO.NS', 'BAJFINANCE.NS', 'BAJAJFINSV.NS', 'BPCL.NS', 'BHARTIARTL.NS', 'BRITANNIA.NS', 'CIPLA.NS', 'COALINDIA.NS', 'DIVISLAB.NS', 'DRREDDY.NS', 'EICHERMOT.NS', 'GRASIM.NS', 'HCLTECH.NS', 'HDFCBANK.NS', 'HDFCLIFE.NS', 'HEROMOTOCO.NS', 'HINDALCO.NS', 'HINDUNILVR.NS', 'ICICIBANK.NS', 'ITC.NS', 'INDUSINDBK.NS', 'INFY.NS', 'JSWSTEEL.NS', 'KOTAKBANK.NS', 'LTIM.NS', 'LT.NS', 'M&M.NS', 'MARUTI.NS', 'NTPC.NS', 'NESTLEIND.NS', 'ONGC.NS', 'POWERGRID.NS', 'RELIANCE.NS', 'SBILIFE.NS', 'SBIN.NS', 'SUNPHARMA.NS', 'TCS.NS', 'TATACONSUM.NS', 'TATAMOTORS.NS', 'TATASTEEL.NS', 'TECHM.NS', 'TITAN.NS', 'UPL.NS', 'ULTRACEMCO.NS', 'WIPRO.NS']

# Create empty lists to store stocks in uptrend and downtrend
stocks_in_uptrend = []
stocks_in_downtrend = []


for ticker_symbol in list:
    #Ticker object for the stock
    stock = yf.Ticker(ticker_symbol)
    # Fetchig historical data for the stock
    historical_data = stock.history(period="1", interval="15m")


    # Calculate the 20-day, 50-day, 100-day, and 200-day  (EMA)
    historical_data['EMA_20'] = historical_data['Close'].ewm(span=20, adjust=False).mean()
    historical_data['EMA_50'] = historical_data['Close'].ewm(span=50, adjust=False).mean()
    historical_data['EMA_100'] = historical_data['Close'].ewm(span=100, adjust=False).mean()
    historical_data['EMA_200'] = historical_data['Close'].ewm(span=200, adjust=False).mean()

    # Determining if the stock is in an uptrend or downtrend
    is_in_uptrend = (
        (historical_data['Close']   > historical_data['EMA_50'] )&
         (historical_data['EMA_50'] > historical_data['EMA_100']) &
        (historical_data['EMA_100'] > historical_data['EMA_200']))

    is_in_downtrend = (
        (historical_data['Close'] < historical_data['EMA_50']) &
         (historical_data['EMA_50'] < historical_data['EMA_100']) &
        (historical_data['EMA_100'] < historical_data['EMA_200']))

    # Checking the most recent data point to determine the current trend
    if is_in_uptrend.iloc[-1]:
        stocks_in_uptrend.append(ticker_symbol)
    elif is_in_downtrend.iloc[-1]:
        stocks_in_downtrend.append(ticker_symbol)


# Print the list of stocks in uptrend and downtrend
print("Stocks in Uptrend:", stocks_in_uptrend)
print("Stocks in Downtrend:", stocks_in_downtrend)