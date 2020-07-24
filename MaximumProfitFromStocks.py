"""
You are given an array. 
Each element represents the price of a stock on that particular day. 
Calculate and return the maximum profit you can make from buying and selling that stock only once.

For example: [9, 11, 8, 5, 7, 10]

Here, the optimal trade is to buy when the price is 5, and sell when it is 10, so the return value should be 5 (profit = 10 - 5 = 5).

Here's your starting point:

def buy_and_sell(arr):
  #Fill this in.
  
print buy_and_sell([9, 11, 8, 5, 7, 10])
# 5
"""
def buy_and_sell(arr):
    #Fill this in.
    # sell at max (after buy) and buy at min
    profit = 0
    for i in range(len(arr)):
        buy = arr[i]
        sell = max(arr[i:])
        # print("buy at:", buy, "sell at:", sell)
        if sell - buy > profit:
            profit = sell - buy
    return profit
  
print(buy_and_sell([9, 11, 8, 5, 7, 10]))
# 5