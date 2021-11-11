import pandas as pd
import numpy as np
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
x = 1
i = 0
while i < len(df):
    while x < len(df):
        first = df["Price"][i]
        next = df["Price"][x]
        first += next
        print(first)
        x += 1
    i += 1