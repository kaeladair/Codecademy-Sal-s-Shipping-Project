# Function calculates the cost of ground shipping
def ground_shipping_cost(weight):

  if weight <= 2:
    price_per_pound = 1.50
  elif weight <= 6:
    price_per_pound = 3.00
  elif weight <= 10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75

  return 20 + price_per_pound * weight

# Test
print(ground_shipping_cost(10))

# Cost of premium ground shipping
premium_ground_shipping = 125.00

# Function calculates the cost of drone shipping
def drone_shipping_cost(weight):

  if weight <= 2:
    price_per_pound = 4.50
  elif weight <= 6:
    price_per_pound = 9.00
  elif weight <= 10:
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25

  return price_per_pound * weight

# Fuction determines which method of shipping is the cheapest along with the final price
def print_best_shipping(weight):
  
  ground = ground_shipping_cost(weight)
  premium = premium_ground_shipping
  drone = drone_shipping_cost(weight)

  if ground < premium and ground < drone:
    method = "ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium"
    cost = premium
  else:
    method = "drone"
    cost = drone

  print( "The cheapest option available is $%.2f with %s" % (cost, method))
  
print_best_shipping(4.8)
print_best_shipping(41.5)