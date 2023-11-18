import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt

def omega_ratio(returns, required_return=0.0):
    return_threshold = (1 + required_return) ** (1/252) - 1
    returns_less_thresh = returns - return_threshold

    numer = sum(returns_less_thresh[returns_less_thresh > 0.0]) 
    denom = -1.0 * sum(returns_less_thresh[returns_less_thresh < 0.0])

    if denom > 0.0:
        return (numer / denom)
    else:
        return np.nan

ticker = "CVNA"
start_date = "2023-01-01"
end_date = "2023-10-31"
data = yf.download(ticker,start=start_date,end=end_date)

returns = data["Adj Close"].pct_change()

returns.hist(bins=50)
print(omega_ratio(returns, 0.07))
plt.show()
