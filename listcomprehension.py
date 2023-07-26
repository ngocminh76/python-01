# new_list[<action> for <item> in <iterator> if <some condition>]
hello ="Hello world"
for x in hello:
    print(x)
print([char for char in hello ])

print([x for x in range(0,10) if x%2!=0])

list_price =[105,202,131,1520]
def price_product(price):
    return round(price*(1+0.08),2)
print([price_product(price) for price in list_price])