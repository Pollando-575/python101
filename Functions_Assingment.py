def birthday_message(name, age): 
    print("Hello, " + name + "! I hear you are " + str(age) + "today!" + "Congratulations")

name = "Max"
age = "29"
print(birthday_message(name, age))


def order_drink(size, drink_type):
    order ="You ordered a " + size + " " + drink_type + "."
    return order
size = "large"
drink_type = "beer"
print(order_drink(size, drink_type))


def withdraw_cash(pin, balance, pin_attempt, amount):
    if pin_attempt == pin:
        if amount <= balance:
            balance -= amount
            print("Cash is being dispensed...please wait")
            print("New balance:", balance)
        else:
            print("Insufficient funds. Unable to withdraw.")
    else:
        print("Incorrect PIN. Transaction cancelled.")

def main():
    pin = 1138
    balance = 10000
    pin_attempt = int(input("Enter your PIN: "))
    amount = float(input("Enter the amount to withdraw: "))
    withdraw_cash(pin, balance, pin_attempt, amount)

if __name__ == "__main__":
    main()


favroute_sports = ['Football', 'Baskeball', 'Tennis', 'Cricket']
print("Original List:", favroute_sports)
favroute_sports.append('Hockey')
print("After Adding Hockey:", favroute_sports)
first_four_elements = favroute_sports[:4]
print("First 4 Elements:", first_four_elements)
favroute_sports[favroute_sports.index('Hockey')] = 'Ice Hockey'
print("After Replacing Hockey with Ice Hockey:", favroute_sports)
favroute_sports.reverse()
print("Reversed List:", favroute_sports)
favroute_sports.sort
print("Sorted List:", favroute_sports)
favroute_sports.pop(favroute_sports.index('Ice Hockey'))
favroute_sports.clear()
print("Clear List:", favroute_sports)

