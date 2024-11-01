list_tuple = [(1, "Walkers", 0.50), (2, "McCoys", 0.50), (3, "KitKat", 0.75), (4, "Flipz", 0.85), (5, "Haribo", 0.40), (6, "Chewits", 0.60), (7, "BLT sandwich", 1.20), (8, "Panini", 1.40), (9, "Pepsi", 0.95), (10, "Gatorade", 1.50)]


def print_list():
    for i in list_tuple:
        print(f"{i[0]}| {i[1]} : £{i[2]:.2f}")

def vending_machine():
    selected_item = None
    money = 0
    
    #present list
    while True:
        print_list()

        max_item = len(list_tuple)

        #item selection
        while selected_item is None:
            try:
                pick_item = int(input(f"\nPlease select an item (1-{max_item}): "))
                if 1 <= pick_item <= 10:
                    selected_item = list_tuple[pick_item - 1]
                    print(f"\nSelected Item: \"{selected_item[1]}\", which costs £{selected_item[2]:.2f}")
                    break
                else:
                    print(f"Invalid item, please enter a number between 1 and {max_item}.")
            except ValueError:
                print("Invalid Input. Please enter a number.")

        #money input
        while True:
            try:
                money = float(input("\nEnter an amount of money: £"))
                if 0 < money < 100:
                    print(f"Current balance: £{money:.2f}")
                elif money > 100:
                    print("\nThe limit is £100. Please try again.") 
                    continue
                else: 
                    print("Invalid input. Please try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter an amount of money.")    
                continue
                
              #not enough money      
            while money < selected_item[2]:
                try:
                    item_change = str(input("\nInsufficient funds, would you like to (a)| add money (b)| change items (c)| exit? (a/b/c): "))
                    if item_change == "b":
                        selected_item = None
                        print("\nBalance has been refunded. Please pick an item.")
                        return vending_machine()
                    
                        #need to fix the balance issue cos do we reset the balance or do we keep the balance
                    elif item_change == "c":
                        print(f"Your £{money:.2f} has been refunded. Exiting...")
                        return
                    elif item_change == "a":
                        try:
                            money_added = float(input("\nPlease enter an amount of money you'd like to add: £"))
                            if money_added > 0:
                                money += money_added
                                print(f"New Balance: £{money:.2f}")
                            else: 
                                print("Please enter a valid amount.")
                        except ValueError:
                            print("Invalid input. Please enter an amount of money.")
                    else:
                        raise ValueError("\nInvalid input. Please enter 'a', 'b', or 'c'.")       
                except ValueError as e:
                    print(e)            
             #money is enough           
            while money >= selected_item[2]:
                try:
                    confirm_item = input("Would you like to confirm this item? (y/n): ")
                    if confirm_item == "y":
                        #calculate change
                        change = money - selected_item[2]                    
                        print(f"\n\"{selected_item[1]}\" has been confirmed. Thank you for your purchase!")
                        if change > 0:
                            print(f"Your change is: £{change:.2f}")
                        
                        #Error handling for keep buying
                        while True:
                            try:
                                keep_buying = input("\nWould you like to purchase another item? (y/n): ")
                                if keep_buying == "y":
                                    print("\nYour balance has been reset. Please pick an item.")
                                    return vending_machine()
                                elif keep_buying == "n":
                                    print("\nThank you for purchase!")
                                    return
                                else:
                                    raise ValueError("\nInvalid input. Please enter 'y' or 'n'.")
                            except ValueError as e:
                                print(e)
                                
                    elif confirm_item == "n":
                            return vending_machine() 
                    else:
                        raise ValueError("\nInvalid input. Please enter 'y' or 'n'.")
                                        
                except ValueError as e:
                    print(e)
                    
                     
vending_machine()

            


