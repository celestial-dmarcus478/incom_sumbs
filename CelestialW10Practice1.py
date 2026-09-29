print("Half-Month payroll calculator")
while True:
     celestialname=str(input("Enter the employee name: ")).title()
     celestialjob=str(input("Enter employee's job: ")).title()
     celestialhrs=float(input("Enter the employee's actual hours worked: "))
#job determine

     match celestialjob:
        case "Janitor":
            celestialslr=18000
        case"Clerk":
            celestialslr=22000
        case"Cashier":
            celestialslr=24000
        case"Manager":
            celestialslr=40000
        case _:
            print("Invalid job input")
#formulas
     celestialhfslr=celestialslr/2
     celestialhrate=celestialhfslr/88
     celestialabehr=0
     celestialovrhr=0
     celestialabdedu=0
     if(celestialhrs<88):
         celestialabehr=88-celestialhrs
     elif(celestialhrs>88):
         celestialovrhr=celestialhrs-88
     else:
         print("Unelgible hours")
     celestialabdedu=celestialabehr*celestialhrate
     celestialovrrate=celestialhrate*celestialovrhr
     celestialovrpay=celestialovrhr*celestialovrrate
     celestialnethmslr=celestialhfslr-celestialabdedu+celestialovrpay
#prints
     print("Name: ",celestialname)
     print("Position: ",celestialjob)
     print("Actual hours worked: ",celestialhrs)
     print("Monthly Salary: "f"{celestialslr:,}")
     print("Half-Month Salary: "f"{celestialhfslr:,}")
     print("Hourly rate: ",celestialhrate)
#calcs
     print("Hours absent: ",celestialabehr ,"Absence Deduction:" ,celestialabdedu)
     print("Overtime Hours: ",celestialovrhr,"Overtime Pay: ",celestialovrpay)
     print("Net Salary: "f"{celestialnethmslr:,}")

     again = input("Do you want to enter again? (Y/N): ")
     if again.upper() != "Y":
                print("Program ended.")
                break