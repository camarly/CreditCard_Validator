

# Employee PaySlip
#Question 9
count=0
while count <= 10:

    # Question 1
    # Get inputs from user.
    Employee_ID=int(input("Enter Employee ID number: "))
    Employee_Name=input("Enter Employee Name: ")
    Total_Hours_Worked=float(input("Enter Total Hours Worked: "))

    Pay_Rate=float(input("Enter your pay rate: "))

    # Question 2
    print("Play Slip Headings")
    print("Employee_ID\tEmployee_Name\tTotal_Hours_Worked\tGross_Pay\tIncome_Tax\tNIS_Tax\tNHT_Tax\tNet_Pay")

    # Question 3
    Gross_Pay=Total_Hours_Worked * Pay_Rate

    # Question 4

    NIS_Tax=Gross_Pay * 0.025
    if NIS_Tax>1000:
        NIS_Tax=1000

    # Question 5
    NHT_Tax=Gross_Pay * 0.025

    # Question 6
    Income_Tax=0
    if Gross_Pay>20000:
        Income_Tax=(Gross_Pay * 0.15) - NIS_Tax

    # Question 7
    Net_Pay=(Gross_Pay - (NIS_Tax + NHT_Tax + Income_Tax))

    count=count + 1
    #print("Employee_ID\tEmployee_Name\tTotal_Hours_Worked\tGross_Pay\tIncome_Tax\tNIS_Tax\tNHT_Tax\tNet_Pay")
    #print ({},(Employee_ID,Employee_Name,Employee_ID,Employee_ID)
    
    # 
    payslip = "{:<15} | {:<20} | {:<20} | {:<15} | {:<15} | {:<15} | {:<15} | {:<15}".format(Employee_ID, Employee_Name, Total_Hours_Worked, Gross_Pay, Income_Tax, NIS_Tax, NHT_Tax, Net_Pay)
    print(payslip)
    # Question 8 and # Question 9 - Question 9 also starts at the top for looping purposes.
#print("Employee_ID\tEmployee_Name\tTotal_Hours_Worked\tGross_Pay\tIncome_Tax\tNIS_Tax\tNHT_Tax\tNet_Pay")