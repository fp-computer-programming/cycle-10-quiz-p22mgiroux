# Author: MOG 2/2/22

from functools import reduce
from itertools import count


prices = [30, 40, 25, 55, 60, 80, 65]
sales = [1, 3, 2, 5, 2, 1, 2]
items = [['tee-shirt','long-sleeved','tanktop'],['quarter-zip','pullover','full-zip','half-zip']]

def find_avg(prices):
    avg = 0
# Add all the prices to "avg" then devide by the length of the prices list, the number of prices
    for x in prices:
        avg += x
    avg /= len(prices)
    return avg


def reduce_prices(prices, reducer = 5):
# Iterate through the indexes in the price list, reducing each price by the reducer variable, 5 by default
    for i in range(len(prices)):
        prices[i] -= reducer
    return prices


def total_sales(prices, sales):
    total = 0
# For every price, multiply the sales by that price in that index, and add it to the total
    for i, x in enumerate(prices):
        total += sales[i] * x
# add the now multiplied sales to the total
    return total


def reduce_more_than(prices, threshold = 40, reducer = 10):
# For every price, if it exceeds the threshold, default 40, then reduce it by the reducer, default 10
    for i, x in enumerate(prices):
        if x > threshold:
            prices[i] -= reducer
    return prices

def item_price(prices, items):
# for every list of items, then for every item in those lists, add the correct price to the corresponding item
    for i, x in enumerate(items):
        for n, y in enumerate(x):
            items[i][n] += " ${}".format(prices[i * len(items) + n])
    return items


def count_to_while(num, interval = 1):
    x = interval
    while x <= num:
        if x % interval == 0:
            print(x)
        x += interval

def count_to_for(num, interval = 1):
    for x in range(interval, num + 1, interval):
        print(x)

print(find_avg(prices))

print(reduce_prices(prices))

print(total_sales(prices,sales))

print(reduce_more_than(prices))

print(item_price(prices, items))

count_to_while(12,3)
count_to_for(12,3)