# Add your Code below
import datetime as dt
from decimal import Decimal
from random import randint
from random import choice
import custom_module
date = dt.date.today()
time = dt.datetime.now().time()
print('The current date is', date, 'at', time)
current_year = date.year
target_year = randint(2026, 2050)
base_cost = Decimal('1000.00')
cost_multiplier = Decimal(str(abs(current_year - target_year)))
final_cost = base_cost * cost_multiplier
destinations = ['Florida', 'New York', 'London', 'Japan', 'Niger', 'Brazil', 'Texas', 'France', 'Italy']
destination = choice(destinations)
print(custom_module.generate_time_travel_message(target_year, destination, final_cost))
