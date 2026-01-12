stock = [7,3,2,5,8,4]
n = len(stock)
minprice = float("inf")
maxprofit = float("-inf")

for i in range(0 , n):
    minprice = min(stock[i] , minprice)
    
    profit = stock[i] - minprice
    maxprofit = max(profit , maxprofit)


print(maxprofit)


#why we have taken min price because the minimun the price for buying then the higher will be profity . if we sell for naytjing . 
#here wll update the min price , and then try to get the profit . 
