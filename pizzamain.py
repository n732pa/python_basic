import pizzaOrder as p

pizza_menu={'페페로니 피자':3000,'치즈 피자':3200,'콤비네이션 피자':3500,'불고기 피자':3600,'해산물 피자':3800}
drink_menu={'콜라':1500,'사이다':1500,'생수':1000}

order_pizza= p.select(pizza_menu,'피자')
print(order_pizza)
order_drink= p.select(drink_menu,'음료')
print(order_drink)

# 계산
tot_pizza = p.money_calc(order_pizza,pizza_menu, '피자')
tot_drink = p.money_calc(order_drink,drink_menu, '음료')

print(f'전체가격: 피자 + 음료: {tot_pizza + tot_drink}')

# print(select())