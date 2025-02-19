currentSalary = 0
currentMonth = 0
allocation = [33, 33, 33]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

print("Hello Nabiha!")

currentSalary = int(input("Please input your salary for the month: "))
currentMonth = int(input("Please input the current month (1-12): "))
for i in range(3):
    allocation[i] = int(input("Please input your salary allocations (Savings/Rent/Electricity): "))
    

