stock_prices = [('AAPL',200),('GOOG',400),('MSFT',100)]
for item in stock_prices:
    print(item)
for ticker, price in stock_prices:
    print(price + (0.1*price))

work_hours = [('ABBY',100),('Billy',400),('Cassie',800)]
def find_best_worker(workhours):

    current_max = 0
    employ_of_month=""

    for employee, hours in workhours:
        if hours > current_max:
            current_max = hours
            employ_of_month = employee
        else:
            pass
    #return
    return (employ_of_month,current_max)

print(find_best_worker(work_hours))
name, hours = find_best_worker(work_hours)
print(name ,' ',hours) # tuple 변수할당