
MENU={
'tea': 2,
'cheeseburger': 5,
'chocolate_shake': 5,
'coke': 2,
'salad': 4,
'brownie': 3,
'cookie': 2
}


def restaurant():
    possible_items = set(MENU.keys())
    live_order = True
    order_sum = 0
    user_input = ''
    while live_order:
        user_input = input("What do you want to order? ").strip()
        if not user_input:
            print(f"That's that")
            live_order = False
        else:
            if user_input in possible_items:
                order_sum += MENU[user_input]
                print(f"{user_input} costs {MENU[user_input]}. Order Total: {order_sum}")
            else:
                print("This is not something you order")
                print(f"Pick one of: {possible_items}")
    
    print(f"Total: {order_sum}")

restaurant()
