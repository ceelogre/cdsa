# python3

import optparse
from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    remaining_capacity = capacity
    weight_price_dict = {}
    opt_price = 0

    for i in range(len(prices)):
        weight_price_dict[prices[i]] = weights[i]

    # sort the prices
    prices.sort(reverse=True)

    #take as much weight as possible of the highest price
    for i in range(0, len(prices)):
        if remaining_capacity <= 0:
            return opt_price
        price_per_w = prices[i] / weight_price_dict[prices[i]]
        item_weight = 0
        while item_weight <= weight_price_dict[prices[i]]:
            if price_per_w <= remaining_capacity:
                opt_price += price_per_w
                remaining_capacity = capacity - opt_price
                item_weight += price_per_w
            else: break
    
    return opt_price


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    print(data)
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
