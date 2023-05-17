prices = [7, 1, 5, 3, 6, 4]

# sell = 1
# buy = 0
# profit = 0
# for i in range(0, len(prices)):
#     if prices[i] > prices[sell] and i > buy:
#          sell = i
#     profit = max(profit, sell - buy)
#     if prices[i] < prices[buy] and i < sell:
#         buy = i
l = 0
r = 1
profit = 0
while r < len(prices):
    if prices[r] < prices[l]:
        # profit = max(profit, prices[r] - prices[l])
        l = r
        # r += 1
    else:
        profit = max(profit, prices[r] - prices[l])
        # r += 1
    r+=1

print(l)
print(r)
print(profit)
