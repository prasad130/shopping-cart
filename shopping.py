product_list = []
quantity_list = []
price_list = []
user_list = []
while True:
    print('SELECT ROLE')
    select = input('admin/user: ')
    if select == 'admin':
        while True:
            print('1. Add Product\n2. Update Product\n3. Remove Product\n4. View Products\n5. View Users\n6. Exit')
            choice = int(input('Enter your choice: '))
            match choice:
                case 1:
                    product = input('Enter product name: ')
                    if product in product_list:
                        print(product,'already exist if you want to update choose option 2')
                    else:
                        qty = int(input(f'Enter {product} quantity: '))
                        price = int(input(f'Enter {product} price: '))
                        product_list.append(product)
                        quantity_list.append(qty)
                        price_list.append(price)
                        print(product,'Added successfully')
                case 2:
                    product = input('Which product do you want to update: ')
                    if product in product_list:
                        idx = product_list.index(product)
                        print('1. Quantity\n2. Price')
                        choice = int(input('Enter your choice: '))
                        if choice == 1:
                            qty = int(input(f'Enter {product} quantity: '))
                            quantity_list[idx] = qty
                            print(product,'quantity is updated')
                        elif choice == 2:
                            price = int(input(f'Enter {product} price: '))
                            price_list[idx] = price
                            print(product,'price is updated')
                    else:
                        print(product,'is not there')
                case 3:
                    product = input('Which product do you want to remove: ')
                    if product in product_list:
                        idx = product_list.index(product)
                        product_list.pop(idx)
                        quantity_list.pop(idx)
                        price_list.pop(idx)
                        print(product,'is removed')
                    else:
                        print(product,'is not there')
                case 4:
                    print('='*24)
                    print('Products Quantity Price')
                    for product,qty,price in zip(product_list,quantity_list,price_list):
                        print(f'{product:<9}{qty:<9}{price:<5}')
                    print('='*24)
                case 5:
                    print('='*20)
                    i = 1
                    print('S.No User')
                    for user in user_list:
                        print(f'{i:<5}{user}')
                        i += 1
                    print('='*20)
                case 6:
                    break
                case _ :
                        print('Invalid Input')
    elif select == 'user':
        cart_list = []
        qty_list = []
        order_list = []
        name = input('Enter username: ')
        while True:
            if name in user_list:
                print('1. View Products\n2. Add to Cart\n3. Remove from Cart\n4. View Cart\n5. Checkout\n6. Exit')
                choice = int(input('Enter your choice: '))
                match choice:
                    case 1:
                        print('='*24)
                        print('Products Quantity Price')
                        i = 1
                        for product,qty,price in zip(product_list,quantity_list,price_list):
                            print(f'{product:<9}{qty:<9}{price:<5}')
                        print('='*24)
                    case 2:
                        select = input('Select product: ')
                        if select in product_list:
                            idx = product_list.index(select)
                            qty = int(input('Enter Quantity: '))
                            if quantity_list[idx] >= qty:
                                cart_list.append(product_list[idx])
                                qty_list.append(qty)
                                print(select,'is Added to cart')
                            else:
                                print(product_list[idx],'is Out of Stock')
                        else:
                            print(select,'not there')
                    case 3:
                        remove_product = input('Which product do you want to remove: ')
                        if remove_product in cart_list:
                            idx = cart_list.index(remove_product)
                            cart_list.pop(idx)
                            qty_list.pop(idx)
                            print(remove_product,'is removed')
                        else:
                            print(remove_product,'is not there')
                    case 4:
                        print('Cart')
                        print('='*17)
                        print('Products Quantity')
                        for p,q in zip(cart_list,qty_list):
                            print(f'{p:<9}{q}')
                        print('='*17)
                    case 5:
                        if not cart_list:
                            print('Cart is Empty')
                        else:
                            check_out = True
                            for p,q in zip(cart_list,qty_list):
                                idx = product_list.index(p)
                                if q>quantity_list[idx]:
                                    print(p,'Insufficent Quantity')
                                    check_out = False
                            if check_out:
                                for p, q in zip(cart_list, qty_list):
                                    idx = product_list.index(p)
                                    quantity_list[idx] -= q
                                    if quantity_list[idx] == 0:
                                        product_list.pop(idx)
                                        quantity_list.pop(idx)
                                        price_list.pop(idx)
                                    print(p, 'ordered successfully')
                                cart_list.clear()
                                qty_list.clear()
                                print('Checkout completed successfully')
                    case 6:
                        break
                    case _ :
                        print('Invalid Input')
            else:
                user_list.append(name)
                print(name,'added successfully....\nNow continue your shopping')
    elif select == 'done':
        break
    else:
        print('Invalid Input')
