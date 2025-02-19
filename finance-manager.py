currentSalary = 0
currentMonth = 0
allocation = [33, 33, 33]
allocOptions = ["savings", "rent", "electricity"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
stop = True             #boolean for error handling user input

print("Hello Nabiha! Welcome to your finance manager.")

while stop:
    currentSalary = int(input("\nPlease input your salary for the month: "))

    tempMonth = int(input("\nPlease input the current month (1-12): "))
    if 0 < tempMonth < 13:
        currentMonth = tempMonth - 1    #For indexing
    else :
        print("That is not a valid month! Restarting!")
        continue
    
    for i in range(3):
        allocation[i] = int(input(f"\nPlease input your percentage salary allocation for {allocOptions[i]}: %"))

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

salaryPower = currentSalary ** 2

randomSaving = 0

print(f"\nMangaging finances for {months[currentMonth]}.")
print(f"Salary for current month: {currentSalary}, allocated {allocation[0]}/{allocation[1]}/{allocation[2]} for savings, rent and electricity.")
print("\n1: Spendings on savings, rent and electricity")
print("2: Your combined total spendings")
print("3: What will remain after your spendings")
print(f"4: Yearly estimate for rent and electricity based on {months[currentMonth]}")
print("5: Your salary to the power of 2 (YOU WISH)")
print("6: ")
print("7: Quit the interface.")


option = int(input("\nPlease enter an option: "))

while option != 7 :
    if option == 1 :
        print(f"\nIn {months[currentMonth]}, you have allocated {moneyAllocation[0]} to savings, {moneyAllocation[1]} to rent and {moneyAllocation[2]} to electricity!" )

    if option == 2 :
        print(f"\nYour combined total spendings for {months[currentMonth]} amount to {monthTotal}.")

    if option == 3 :
        print(f"\nYou have {remainderSalary} left in {months[currentMonth]}.")

    if option == 4 :
        print(f"\nYour yearly estimate for rent and electricity amounts to {yearlyEstimate}.")

    if option == 5 :
        print(f"\nYour salary to the power of 2 would be {salaryPower}.")


    option = int(input("\nPlease enter another option: "))

print("\nSee you next month!\n")

        
