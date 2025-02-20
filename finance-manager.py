currentSalary = 0
currentMonth = 0
allocation = []
allocOptions = ["savings", "rent", "electricity"]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
stopSingle = True             #boolean for error handling user input
stopMonths = ""
monthsList = []
monthStorage = {}


print("Hello Nabiha! Welcome to your finance manager.")
stopMonths = input("\nWould you like to start adding data to the manager? (Y/n) ")

while stopMonths != "n":

    stopSingle = True

    while stopSingle:
        allocation = []

        tempMonth = int(input("\nPlease input the current month (1-12): "))
        if 0 < tempMonth < 13:
            currentMonth = tempMonth - 1    #For indexing
        else :
            print("That is not a valid month! Restarting!")
            continue
        


        currentSalary = int(input("\nPlease input your salary for the month: $"))
        if currentSalary < 0 :
            print("Your salary cannot be negative! (Unless things are REALLY bad but at that point you need a lot more than a simple finance manager.)")
            continue
        
        
        for i in range(3):
            allocation.append(int(input(f"\nPlease input your percentage salary allocation for {allocOptions[i]}: %")))

        sum = allocation[0] +  allocation[1] + allocation[2]
        if sum < 102 :             #Small error interval for human error
            stopSingle = False

        else :
            print("You have overallocated funds! Restarting!")

        monthStorage = {
            "month" : currentMonth,
            "salary" : currentSalary,
            "allocations" : allocation
        }

        monthsList.append(monthStorage)
    
    stopMonths = input("\nWould you like to add any more data? (Y/n) ")
    

operations = input("\nWould you like to perform any operations on a month's salary? (Y/n) ")
validMonth = False

while operations != "n" :
    workingMonth = int(input("\nWhich month would you like to work on (1-12): ")) - 1

    if 0 < workingMonth < 13 :
        for i in range(len(monthsList)) :
            if monthsList[i]["month"] == workingMonth :
                currentSalary = monthsList[i]["salary"]
                allocation = monthsList[i]["allocations"]
                validMonth = True

        if validMonth :
            moneyAllocation = [0, 0, 0]
            for i in range(3) :
                moneyAllocation[i] = allocation[i] * currentSalary / 100

            monthTotal =  moneyAllocation[0] + moneyAllocation[1] + moneyAllocation[2]

            remainderSalary = currentSalary - monthTotal

            yearlyRent = moneyAllocation[1] * 12
            yearlyElec = moneyAllocation[2] * 12

            yearlyEstimate = yearlyRent + yearlyElec

            salaryPower = currentSalary ** 2

            extraSaving = 0
            extraDivided = 0

            print(f"\nMangaging finances for {months[workingMonth]}.")
            print(f"Salary for current month: ${currentSalary}, allocated {allocation[0]}/{allocation[1]}/{allocation[2]} for savings, rent and electricity.")
            print("\n1: Spendings on savings, rent and electricity")
            print("2: Your combined total spendings")
            print("3: What will remain after your spendings")
            print(f"4: Yearly estimates for rent and electricity based on {months[workingMonth]}")
            print("5: Your salary to the power of 2")
            print("6: If you'd like to add a specific amount to savings")
            print("7: Quit the interface.")

            option = int(input("\nPlease enter an option: "))

            while option != 7 :
                monthTotal =  moneyAllocation[0] + moneyAllocation[1] + moneyAllocation[2]
                remainderSalary = currentSalary - monthTotal
                if option == 1 :
                    print(f"\nIn {months[workingMonth]}, you have allocated ${moneyAllocation[0]} to savings, ${moneyAllocation[1]} to rent and ${moneyAllocation[2]} to electricity!" )

                elif option == 2 :
                    monthTotal =  moneyAllocation[0] + moneyAllocation[1] + moneyAllocation[2]
                    print(f"\nYour combined total spendings for {months[workingMonth]} amount to ${monthTotal}.")

                elif option == 3 :
                    print(f"\nYou have ${remainderSalary} left in {months[workingMonth]}.")

                elif option == 4 :
                    print(f"\nYour yearly estimate for rent is ${yearlyRent}.")
                    print(f"Your yearly estimate for electricity is ${yearlyElec}.")
                    print(f"Your combined yearly estimate for rent and electricity is ${yearlyEstimate}.")


                elif option == 5 :
                    print(f"\nYour salary to the power of 2 would be ${salaryPower}.")

                elif option == 6 :
                    extraSaving = int(input("\nPlease enter the extra savings: $"))

                    moneyAllocation[0] += extraSaving

                    print(moneyAllocation[0])
                    if moneyAllocation[0] != 0 :
                        extraDivided = extraSaving / moneyAllocation[0]
                    print(f"The result of this operation is: ${extraDivided}")

                else :
                    print("\nPlease enter a valid option!")

                option = int(input("\nPlease enter another option: "))
            
            validMonth = False
            
        else :
            print("You have not entered data for that month, pick another month to work on!")

    else :
        print("That is not a valid input for month! Restarting!")
    
    operations = input("\nWould you like to perform any operations on another month's salary? (Y/n) ")


print("\nSee you next month!\n")

        
