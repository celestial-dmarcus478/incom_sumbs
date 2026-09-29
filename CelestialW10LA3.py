print("welcome to spelling checker")
while True:
    celestialsearch = input("Spell full name of INCOM: ")
    celestialkey = "intro to computing"

    found=False

    for character in celestialkey:
        if celestialsearch.lower() == celestialkey.lower():
            found=True
            break

    if found:
        print("correct")
    else:
        print("incorrect")

    again = input("Try searching again? (Y/N):")
    if again.upper() != "Y":
        print("Thank you")
        break