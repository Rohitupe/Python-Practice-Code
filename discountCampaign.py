price = 50

def discountPrice(price,discount):
  """
    get the price after applying the discount percent
    for 0 - 20 = 20%
        20 - 50= 40%
        50 > = 60%
  """ 
  return (price * discount)

if price < 20:
  print(discountPrice(price,0.8))

elif 20 < price <= 50:
  print(discountPrice(price,0.6))

else:
  print(discountPrice(price,0.4))

