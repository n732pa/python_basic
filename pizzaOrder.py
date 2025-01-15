def pizza_select():
    pizza_menu={'페페로니 피자':'3000','치즈 피자':'3200','콤비네이션 피자':'3500','불고기 피자':'3600','해산물 피자':'3800'}
    order_pizza={}

    for name,price in pizza_menu.items():
        print(f'{name} ({price})원')

    while True:
        p_name=input('메뉴 이름을 입력하세요.(종료:exit) ')
        if p_name == '0':
            pass
        elif p_name in pizza_menu:
            count=int(input('수량을 입력하세요'))
            order_pizza[p_name]=count                  # 딕셔너리에 데이터 삽입
            print('주문 완료')
        elif p_name == 'exit':
            break
    return order_pizza, pizza_menu

def drink_select():
    drink_menu={'콜라':'1500','사이다':'1500','생수':'1000'}
    order_drink={}
    for name,price in drink_menu.items():
        print(f'{name} ({price})원')

    while True:
        d_name=input('음료수 이름을 입력하세요.(종료:exit)  ')
        if d_name == '0':
            pass
        elif d_name in drink_menu:
            count=int(input('수량을 입력하세요'))
            order_drink[d_name]=count                  # 딕셔너리에 데이터 삽입
            print('주문 완료')
        elif d_name == 'exit':
            break
    return order_drink, drink_menu

    
if __name__=='__main__':
    print(pizza_select())
    print(drink_select())