class village(object):
    def __init__(self):
        self.population = 100
        self.food_consumption = self.population * 3
        self.storage_factor = 1.25 #storage_factor: the propensity to stockpile food, ideally this would create a stockpile of x months of food (varies by region) where x is the months in which new food is not produced
        self.price_change_factor = 3 #price_change_factor: the change in demand based on change in price, shows the sensitivity of demand to changes in price
        self.var_cost_per_acre = 10 #copper pieces
        self.fixed_cost_per_acre = 100

