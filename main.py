#Gold rate calculator/converter
print("Welcome to the GOLD converter/calculator")
print("If you wish to convert from 24k to 22k type '24k' ")
print("If you wish to convert from 22k to 24k type '22k'")

choice =  input("What type (24k/22k)")

#this if conditoin portion converts 24k to 22k according to the rate. Standard of Gold dealers in PK
if choice == "24k":
    tola_amnt_gold_24k = float(input("Please input the amount of tolas : "))
    rate = float(input("Please input today's rate of 24k : "))
    rate = (rate/24)*22
    tot_gold_price = tola_amnt_gold_24k * rate
    print ("Total Gold price (22k): ",tot_gold_price)


elif choice == "22k":
    tola_amnt_gold_22k = float(input("Please input the amount of tolas : "))
    rate = float(input("Please input today's rate of 22k : "))
    rate = (rate/22)*24
    tot_gold_price = tola_amnt_gold_22k * rate
    print ("Total Gold price (24k): ",tot_gold_price)

else:
    print("Invalid input. Please try again")
