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
monthTotal = 0
remainderSalary = 0
yearlyEstimate = 0
salaryPower = 0
randomSaving = 0
option = int(input("Please enter an option: "))

while option != 7 :
    if option == 1 :
        for i in range(3) :
            moneyAllocation[i] = allocation[i] * currentSalary / 100
            
        print(f"In {months[currentMonth]}, you have allocated {moneyAllocation[0]} to savings, {moneyAllocation[1]} to rent and {moneyAllocation[2]} to electricity!" )

    if option == 2 :
        for i in range(3) :
            moneyAllocation[i] = allocation[i] * currentSalary / 100
            monthTotal += moneyAllocation[i]

        print(f"Your combined total spendings for {months[currentMonth]} amount to {monthTotal}")

    option = int(input("Please enter another option: "))

        
