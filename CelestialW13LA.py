print("Welcome to employee checker")
celestialemply={"E100":{"Name":"Liane Uy","Rank":"JO 5","DutyHours":(42,43,40,40),"RequiredHours":160,"Basicpay":29000},
                "E105":{"Name":"Robert Santos","Rank":"Manager 1","DutyHours":(30,35,31,30),"RequiredHours":120,"Basicpay":60000},
"E107":{"Name":"Gideon","Rank":"Mason 9","DutyHours":(29,33,31,30),"RequiredHours":140,"Basicpay":24000}
                }


while True:
    celestialidsearch=input("Please enter the employee ID to view: \n").upper()
    celestialratehr= celestialemply[celestialidsearch]["Basicpay"]/celestialemply[celestialidsearch]["RequiredHours"]
    celestialovrhr= sum(celestialemply[celestialidsearch]["DutyHours"]) - celestialemply[celestialidsearch]["RequiredHours"]
    celestialovrtm= celestialratehr * 1.5 * celestialovrhr
    celestialgross= celestialemply[celestialidsearch]["Basicpay"] + celestialovrtm
    if celestialidsearch in celestialemply:
        print("="*25)
        print("Name: ",celestialemply[celestialidsearch]["Name"],
        "\nJob Rank: ",celestialemply[celestialidsearch]["Rank"],
        "\nDuty Hours: ",*celestialemply[celestialidsearch]["DutyHours"],
        "\nBasic Pay: ", celestialemply[celestialidsearch]["Basicpay"],
              "\nRate Per Hour: ",celestialratehr,
              "\nGross Pay:",celestialgross

              )
        if sum(celestialemply[celestialidsearch]["DutyHours"]) > celestialemply[celestialidsearch]["RequiredHours"]:
            print("\nExcess Hours: ", celestialovrhr)
        print("=" * 25)


    else:
        print("Employee ID not found.")
    again=input("Find another ID? (Y/N)").upper()
    if again != "Y":
            print("Thank You")
            break