#short run test
#how big is a loop in terms of time? crop cycles for farmers, weekly for others (sunday markets)
from tables import mcl_farms
from area import village
village = village()

class agent(object):

	def __init__(self):
		pass


class farmer(agent):

	def __init__(self, village):

		self.fields_owned = 1
		self.field_size = 10 #in acres
		self.output_per_acre = 60 #in pounds of dry grain
		self.field_output = self.field_size * self.output_per_acre
		self.labor_employed = 0 #this should be a function of profitability
		self.farm_output = self.field_output * self.fields_owned

		self.farm_output_meals = self.farm_output * 2 #assumption a meal is worth 1/2 pound of dry grain

	#marginal product of labor table
	cost_of_labor = mcl_farms #labor is a fixed cost by season
	#variable costs
	var_cost_acre = village.var_cost_per_acre #copper pieces
	#irrigation
	#seed
	#maintenance of fields

	#fixed costs
	f_costs_per_acre = village.fixed_cost_per_acre	#rent on farm? cost of mortgage over time? debt?
		#must cover fallow fields
	total_cost_per_acre = f_cost_per_acre + var_cost_per_acre

farmer1 = farmer(village)
print farmer1. total_cost_per_acre
#supply curve
Qs = farmer1
#demand curve
price = 10 #solve for Qd, Qs
Qd = village.food_consumption * village.storage_factor - village.price_change_factor * price

print Qd




