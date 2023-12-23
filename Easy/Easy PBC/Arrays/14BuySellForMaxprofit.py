# 14 Stock Buy Sell to Maximize Profit

# The cost of a stock on each day is given in an array. Find the maximum profit that you can make by buying and selling on those days. 
# If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.

# Input: arr[] = {100, 180, 260, 310, 40, 535, 695}
# Output: 865
# Explanation: Buy the stock on day 0 and sell it on day 3 => 310 – 100 = 210
#                       Buy the stock on day 4 and sell it on day 6 => 695 – 40 = 655
#                       Maximum Profit  = 210 + 655 = 865

# Input: arr[] = {4, 2, 2, 2, 4}
# Output: 2
# Explanation: Buy the stock on day 1 and sell it on day 4 => 4 – 2 = 2
#                       Maximum Profit  = 2


# maxProfit = 0
# if price[i] > price[i – 1]
# maxProfit = maxProfit + price[i] – price[i – 1]

def buy_sell_to_maximize_profit(prices, day):
  profit=0
  for i in range(1, day):
    if prices[i] > prices[i-1]: 
      profit += prices[i] - prices[i-1]
  return profit
  

print(buy_sell_to_maximize_profit([100, 180, 260, 310, 40, 535, 695], 7)) 
print(buy_sell_to_maximize_profit([4, 2, 2, 2, 4], 5)) 

# ([100, 180, 260, 310, 40, 535, 695], 7)
# 1 0 80
# 2 1 160
# 3 2 210
# 5 4 705
# 6 5 865

# Time Complexity: O(N), Traversing over the array of size N.
# Auxiliary Space: O(1)
