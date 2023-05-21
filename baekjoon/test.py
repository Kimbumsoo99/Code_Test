def coin_change(n, coins):
    coins.sort(reverse=True)
    result = []
    for coin in coins:
        while n >= coin:
            result.append(coin)
            n -= coin
    return result


N = int(input())
print(coin_change(N, [10, 50, 100, 500]))
