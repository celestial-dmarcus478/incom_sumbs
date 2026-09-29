print("Student Grade Files")
celestialclassrecord={"Liza":{"StudID":"5001","Grade":[90,85,86,82,83,80,92]},
                      "Jeremy":{"StudID":"5002","Grade":[72,75,59,80,84,75,85]},
                      "Ronald":{"StudID":"5003","Grade":[90,81,76,95,78,92,80]}}
while True:
    celestialfind=input("Type Student name to find info:\n").title()
    #find student
    if celestialfind in celestialclassrecord:
        print("Student Found,\nNumber: ",celestialclassrecord[celestialfind]["StudID"])
        print("Grades: ",celestialclassrecord[celestialfind]["Grade"])

        for celestialgrade in celestialclassrecord[celestialfind]["Grade"]:

            if celestialgrade<60:
                print("Candidate For intervention")
                break
            else:
                continue
        celestialavg = sum(celestialclassrecord[celestialfind]["Grade"]) / len(celestialclassrecord[celestialfind]["Grade"])
        celestialtop = max(celestialclassrecord[celestialfind]["Grade"])
        celestiallws = min(celestialclassrecord[celestialfind]["Grade"])
        print("Average grade: ", celestialavg)
        print("highest grade: ", celestialtop)
        print("lowest grade: ", celestiallws)
    else:
        print("Student not found")

    again=input("Find another student? (Y/N)").upper()
    if again != "Y":
        print("Thank You")
        break