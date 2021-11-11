import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#2
cup_cakes = open('Cupcakeinvoices.csv')
#3
for cup_cake in cup_cakes:
    print(cup_cake)


#4
col_list = ["FirstName","LastName","Type","Quantity","Price"]
df = pd.read_csv("Cupcakeinvoices.csv", usecols=col_list)
print(df["Type"])

#5
#float(x)
quantity = df["Quantity"]
price = df["Price"]
inv_total = quantity * price
print(quantity * price)

#6
# x = 1
i = 0
# while i < len(df):
#     while x < len(df):
#         first = df["Price"][i]
#         next = df["Price"][x]
#         first += next
#         print(first)
#         x += 1
#     i += 1


choc_price = 0
van_price = 0
straw_price = 0

# print(df["Type"][0])

while i < len(df):
    if df["Type"][i] == "Chocolate":
        choc_price += (df["Quantity"][i] * df["Price"][i])
        print(choc_price)
    elif df["Type"][i] == "Vanilla":
        van_price += (df["Quantity"][i] * df["Price"][i])
    elif df["Type"][i] == "Strawberry":
        straw_price += (df["Quantity"][i] * df["Price"][i])
    i += 1

x = ["Chocolate", "Vanilla", "Strawberry"]

y = [choc_price,van_price,straw_price]

plt.plot(x, y)

plt.xlabel('Type')

plt.ylabel('Total Price')

plt.title('Prices')

plt.show()


