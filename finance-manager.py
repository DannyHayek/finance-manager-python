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
        currentMonth = tempMonth
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


