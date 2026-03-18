def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("what percentage would ypu like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")
def dollars_to_float(amount):
    amount = amount.replace("$","")
    amount = float(amount)
    return amount

def percent_to_float(amount):
    amount = amount.replace("%","")
    amount = float(amount)/100
    return amount

main()

