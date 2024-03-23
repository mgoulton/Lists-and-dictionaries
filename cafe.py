'''This is a program which calculates the total value of stock of four items that are sold in a cafe'''

# items sold in the cafe
menu = ['hot chocolate','latte','pain au chocolat','cheesecake']


# number of units of stock of each item 
stock = {'hot chocolate': 2840,
         'latte': 5250,
         'pain au chocolat': 145,
         'cheesecake': 96
         }

# price of each individual item on the menu
price = {'hot chocolate': 3.55,
         'latte': 3.50,
         'pain au chocolat': 2.89,
         'cheesecake': 3.20
        }

# total value of stock kept in the cafe, calculated per item
item_value = [round(stock[item]*price[item],2) for item in menu]

#total value of stock kept in the cafe, overall
total_stock = sum(item_value)

print(f"The total stock worth in the cafe is £{total_stock}.")

