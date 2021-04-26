class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        remaining_coins = coins
        num_of_ice_creams = 0
        ice_creams = sorted(costs)
        for ice_cream in ice_creams:
            if ice_cream <= remaining_coins:
                remaining_coins -= ice_cream
                num_of_ice_creams += 1
        return num_of_ice_creams
