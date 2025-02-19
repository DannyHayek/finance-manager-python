currentSalary = 0
currentMonth = 0
allocation = [33, 33, 33]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
stop = True             #boolean for error handling user input

print("Hello Nabiha!")

while stop:
    currentSalary = int(input("Please input your salary for the month: "))

    tempMonth = int(input("Please input the current month (1-12): "))
    if 0 < tempMonth < 13:
        currentMonth = tempMonth - 1    #For indexing
    else :
        print("That is not a valid month! Restarting!")
        continue
    
    for i in range(3):
        allocation[i] = int(input("Please input your salary allocations (Savings/Rent/Electricity): "))

    sum = allocation[0] +  allocation[1] + allocation[2]
    if sum < 102 :             #Small error interval for human error
        stop = False
    else :
        print("You have overallocated funds! Restarting!")
    

moneyAllocation = [0, 0, 0]
for i in range(3) :
    moneyAllocation[i] = allocation[i] * currentSalary / 100

monthTotal =  moneyAllocation[0] + moneyAllocation[1] + moneyAllocation[2]

remainderSalary = currentSalary - monthTotal

yearlyEstimate = (moneyAllocation[1] + moneyAllocation[2]) * 12

salaryPower = 0
randomSaving = 0
option = int(input("Please enter an option: "))

while option != 7 :
    if option == 1 :
        print(f"In {months[currentMonth]}, you have allocated {moneyAllocation[0]} to savings, {moneyAllocation[1]} to rent and {moneyAllocation[2]} to electricity!" )

    if option == 2 :
        print(f"Your combined total spendings for {months[currentMonth]} amount to {monthTotal}.")

    if option == 3 :
        print(f"You have {remainderSalary} left in {months[currentMonth]}.")

    if option == 4 :
        print(f"Your yearly estimate for rent and electricity amounts to {yearlyEstimate}.")

    option = int(input("Please enter another option: "))

        
