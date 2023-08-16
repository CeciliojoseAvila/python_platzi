"""
main2.py and my_functions.py
"""
import my_functions
def get_total(orders):
    
  total = my_functions.get_totals(orders)
  Sum = my_functions.calc_total(total)
  return Sum;

orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

total = get_total(orders)
print(total)