# Homework 

# 1) Create a store [] with objects : { label : “kit-kat” , price : 200 } , and other by example 

# 2) Register user , and ask how much money user has 

# 3) Take a list of products to user 

# 4) User might buy every products he wants if he had enough money 

# Otherwise we must say : “Sorry , your pockets are empty”

# 5) User can exit in start-menu

def is_exit():
    result = input("Do you wanna quit ? y/n : ")
    return result.lower()

def show_products (list_of_products):
    print("|======Chocolate======|")
    for product in list_of_products:
        for key , value in product.items() :
            print(key + " ====> " + value)
        print("|=====================|")

def registration (login , password , balance=0):
    return {
        "login" : login,
        "password" : password,
        "balance": balance
    }

def auth (login, password, array_of_users) :
    for users in array_of_users :
        if login == user['login'] :
            password = input("Enter your account's password: ")
            
            if password == user['password'] :
                return [users , True]
            else :
                print("Incorrect password")
        else:
            print("Incorrect login")
    
def get_balance (account) :
    print("Balance:",current_user['login'],":", current_user['balance'], "UAH")


def money_transfer (account) :
    card_number = input("Enter your card number : ")
    card_date = input("Enter your card date : ")
    card_cvv = input("Enter your card cvv : ")
    
    if len(card_number) == 19 and "/" in card_date and len(card_cvv) == 3:
        money = input("How much money do you want to send? : ")
        account['balance'] = int(account['balance']) + int(money)
        print(f"Congratulations now your balance is : {str(account['balance'])} UAH")
    else:
        print("Error! Enter correct card details")

def buy (target , list_of_products, number) :
    for product in list_of_products:
        if target.lower() == product['label'].lower():
            sliced_price = product['price'].find("U")
            current_user['balance'] = current_user['balance'] - number*int(product['price'][:sliced_price - 1])
    print(f"After you bought the chacolate there is left {str(current_user['balance'])} on your balance")
    if current_user['balance'] < int(product['price'][:sliced_price - 1]):
        print("Sorry , there is not enought money on your balance. Replenish the balance")


products = [
    {
    "label": "kit-kat",
    "price": "25 UAH"
    },
    {
    "label": "twix",
    "price": "35 UAH"
    },
    {
    "label": "mars",
    "price": "28 UAH"
    },
    {
    "label": "roshen",
    "price": "22 UAH"
    },
    {
    "label": "nuts",
    "price": "30 UAH"
    }
]
is_running = True
is_registred = False
users = []


current_user = {}
while is_running :
    user_choose = input("""
        a) Show products 
        b) Register  
        c) Auth
        d) Balance
        e) Buy product
        q) Quit
    
    Answer : """).lower()
    
    if user_choose == "a" :
        show_products(products)
    
    elif user_choose == "b" :
        login = input("Enter login that you want to use continuously: ")
        password = input("Enter your password: ")
        user = registration(login, password, balance = 0)
        users.append(user)
        print(users)
    
    elif user_choose == "c":
        login = input("Enter your account's login : ")
        result = auth(login, password, users)
        current_user, is_registred = result
        print(current_user)
        print(is_registred)
        
    elif user_choose == "d":
        if not is_registred :
            print("Error!")
            continue
        user_choose = input("""
            1) Look at bill
            2) Transfer by card 
        """)
        if user_choose == "1" :
            if is_registred == True :
                get_balance(current_user)
            else :
                print("You should to have an account to look at balance ")
        elif  user_choose == "2":
            money_transfer(current_user)
           
     
    elif user_choose == "e":
        show_products(products)
        prefer_chocolate = input("Choose chocolate that you want buy: ")
        number = int(input("Enter number of chocolates: "))
        buy(prefer_chocolate, products, number)

    
    elif user_choose == "q":
        result = is_exit()
        if result == "y" :
            is_running = False