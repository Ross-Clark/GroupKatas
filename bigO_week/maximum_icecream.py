def maxIceCream(costs, coins):

    ice_creams = 0
    costs.sort(reverse=True)

    while costs and (coins - costs[-1]) >= 0:
        coins = coins - costs.pop(-1)
        ice_creams += 1

    return ice_creams
