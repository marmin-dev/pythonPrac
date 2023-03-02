# 1
inventory = {"메로나":{"가격:300","재고:20"},"비비빅":{"가격:300","재고:20"},"메로나":{"가격:300","재고:20"}}

# 2
inventory = {"메로나": [300, 20],
              "비비빅": [400, 3],
              "죠스바": [250, 100]}

print(inventory["메로나"][0])

# 3
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
keys = list(icecream.keys())
print(keys)

# 4
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
val = list(icecream.values())
print(sum(val))

# 5
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

# 6
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
date_price = dict(zip(date, close_price))
print(date_price)
