# omega_ratio
This script allows you to calculate the Omega ratio of an asset or portfolio, which is a popular risk-return metric to measure performance. Being the probability weighted ratio of gains versus losses for some threshold return target, the Omega ratio considers all momements of the return distribution, whereas the far more common Sharpe ratio only considers the first two moments of the return distribution. 
 
The script will pull data for a stock, calculate the omega ratio of the stock, then plot the daily returns on a histogram. Substituting the stock's daily returns for your portfolio's daily returns would make for a more realistic exercise, however for the purposes of this script, daily return data for $CVNA is used.
 
A high Omega ratio indicates that an asset/portfolio has a low probability of making an extreme loss. In other words, risk-adjusted performance is good if the ratio is greater than 1; it suggests the portfolio has a higher chance of achieving returns above the target level and a lower probability of incurring significant losses. 
