cost = 50
while cost > 0:
    print("Amount Due:",cost)
    coin = int(input("Insert coin: "))
    if coin in [5,10,25]:
        cost -= coin

print("Change Owed:",abs(cost))
